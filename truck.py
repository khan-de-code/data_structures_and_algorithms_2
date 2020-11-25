from package import Package
from permute import permute
from typing import Union
from _time import Time
from hash_table import HashTable
import functools
from graph import Graph, Vertex


class Truck:
    """Initilizes a truck

    Args:
        number (int): The number of the truck
        regular_packages ([Package]):
        all_delivery_locations ([[str, int]]): [description]
        priority_packages ([Package], optional): [description]. Defaults to None.
    """

    time: Time
    number: int
    priority_packages: [Package]
    regular_packages: [Package]
    distance_traveled: float
    all_delivery_locations: [tuple]
    all_distance_matrix: [[float]]
    trip_delivery_locations_priority: [tuple]
    trip_delivery_locations_regular: [tuple]
    trip_distance_matrix_priority: [[float]]
    trip_distance_matrix_regular: [[float]]

    def __init__(self, number: int, regular_packages: [Package], all_delivery_locations, priority_packages=None, departure_time='default'):

        if departure_time == 'default':
            self.time = Time(8, 0, 'AM')
        else:
            self.time = departure_time
        self.number = number
        self.priority_packages = priority_packages
        self.regular_packages = regular_packages
        self.distance_traveled = 0
        self.trip_delivery_locations_priority = []
        self.trip_delivery_locations_regular = []
        self.trip_distance_matrix_priority = []
        self.trip_distance_matrix_regular = []

        self.all_delivery_locations = []
        for i, row in enumerate(all_delivery_locations):
            j = 0
            while j < len(row) - 1:
                if i == 0 or j > 1:
                    break
                elif j == 0:
                    self.all_delivery_locations.append((i - 1, row[0], row[1]))
                    j += 2

        self.all_distance_matrix = []
        for i, row in enumerate(all_delivery_locations):
            temp = []
            for j, col in enumerate(row):
                if i == 0:
                    break
                elif j == 0 or j == 1:
                    continue
                else:
                    temp.append(col)

            if len(temp) > 0:
                self.all_distance_matrix.append(temp)

        for i, row in enumerate(self.all_distance_matrix):
            for j, col in enumerate(row):
                if i != j and j > i:
                    self.all_distance_matrix[i][j] = self.all_distance_matrix[j][i]

        for i, row in enumerate(self.all_distance_matrix):
            for j, col in enumerate(row):
                self.all_distance_matrix[i][j] = float(self.all_distance_matrix[i][j])

        if len(self.regular_packages) != 0:
            self.__set_delivery_locations()

    def load_packages(self, packages: [Package], type: str):
        if type == 'regular':
            for package in packages:
                self.regular_packages.append(package)
        if type == 'priority':
            for package in packages:
                self.priority_packages.append(package)

        self.__set_delivery_locations()

    def deliver_packages(self):
        def __calculate_minutes_travel(distance: float) -> float:
            return distance / (18 / 60)

        def nearest_neighbor(graph: Graph, start_vertex: Vertex, end_vertex: Union[Vertex, str], packages: [Package]):
            """Finds the greedy shortest path

            Args:
                graph (Graph)
                start_vertex (Vertex): The vertex to start at
                end_vertex (Union[Vertex, str]): Could either be a vertex to stop at or a string. If string equals 'round trip', will calculate a round trip. If string equals 'one way' will calculate one way 

            Returns:
                (int, tuple[Vertex]): Returns the distance traveled and a tuple of the order of visited vertecies
            """

            distance_traveled = 0
            vertecies_visited = [start_vertex]
            vertecies_yet_to_visit = list(filter(lambda x: x != start_vertex, graph.vertecies_in_graph))

            current_vertex = start_vertex

            def shortest_edge(from_vertex):
                current_vertex_neighbors = graph.adjacency_list.find(current_vertex)
                shortest_edge_length = float('inf')
                shortest_to_vertex = None

                for to_vertex in current_vertex_neighbors:
                    length = graph.edge_weights.find((from_vertex, to_vertex))

                    if length < shortest_edge_length and to_vertex not in vertecies_visited:
                        if end_vertex != 'round trip' and end_vertex != 'one way' and to_vertex == end_vertex:
                            continue
                        else:
                            shortest_edge_length = length
                            shortest_to_vertex = to_vertex

                return shortest_to_vertex, shortest_edge_length

            while len(vertecies_yet_to_visit) != 0:
                if end_vertex != 'round trip' and end_vertex != 'one way' and len(vertecies_yet_to_visit) == 1:
                    break
                current_vertex, distance = shortest_edge(current_vertex)
                delivered_packages: [Package] = list(filter(lambda package: str(package.delivery_zip)
                                                            in current_vertex.name[2] and package.delivery_address in current_vertex.name[2], packages))

                travel_time = __calculate_minutes_travel(distance)
                self.time.add_time(minutes_with_fractions=travel_time)
                for package in delivered_packages:
                    package.delivered(self.time.clone())

                distance_traveled += distance

                vertecies_yet_to_visit.remove(current_vertex)
                vertecies_visited.append(current_vertex)

            if end_vertex == 'round trip':
                distance = graph.edge_weights.find((current_vertex, start_vertex))
                distance_traveled += distance
                vertecies_visited.append(start_vertex)

                travel_time = __calculate_minutes_travel(distance)
                self.time.add_time(minutes_with_fractions=travel_time)

            elif end_vertex != 'round trip' and end_vertex != 'one way':
                distance = graph.edge_weights.find((current_vertex, end_vertex))
                distance_traveled += distance
                vertecies_visited.append(end_vertex)

                travel_time = __calculate_minutes_travel(distance)
                self.time.add_time(minutes_with_fractions=travel_time)

                if (end_vertex.name[2] != 'HUB'):
                    delivered_package: Package = list(filter(lambda package: str(package.delivery_zip)
                                                             in current_vertex.name[2] and package.delivery_address in current_vertex.name[2], [end_vertex]))[0]
                    delivered_package.delivered(self.time.clone())

            self.distance_traveled += distance_traveled

            return distance_traveled, tuple(vertecies_visited)

        def generate_graph(addresses: [str], distances: [float]) -> Graph:
            graph = Graph()
            vertecies = []
            for address in addresses:
                vertex = Vertex(address)
                vertecies.append(vertex)
                graph.add_vertex(vertex)

            while len(vertecies) > 0:
                current_address = vertecies.pop()
                current_address_index = addresses.index(current_address.name)
                for address in vertecies:
                    address_index = addresses.index(address.name)
                    distance = distances[current_address_index][address_index]

                    graph.add_undirected_edge(current_address, address, distance)

            return graph

        priority_graph = generate_graph(self.trip_delivery_locations_priority, self.trip_distance_matrix_priority)
        regular_graph = generate_graph(self.trip_delivery_locations_regular, self.trip_distance_matrix_regular)

        if len(priority_graph.vertecies_in_graph) == 0:
            hub_vertex = None
            for vertex in regular_graph.vertecies_in_graph:
                if vertex.name[2] == 'HUB':
                    hub_vertex = vertex

            result = nearest_neighbor(regular_graph, hub_vertex, 'round trip', self.regular_packages)

        elif len(regular_graph.vertecies_in_graph) == 0:
            hub_vertex = None
            for vertex in priority_graph.vertecies_in_graph:
                if vertex.name[2] == 'HUB':
                    hub_vertex = vertex

            result = nearest_neighbor(priority_graph, hub_vertex, 'round trip', self.priority_packages)

        else:
            hub_vertex_priority_start = None
            for vertex in priority_graph.vertecies_in_graph:
                if vertex.name[2] == 'HUB':
                    hub_vertex_priority_start = vertex

            hub_vertex_regular_end = None
            for vertex in regular_graph.vertecies_in_graph:
                if vertex.name[2] == 'HUB':
                    hub_vertex_regular_end = vertex

            result_priority = nearest_neighbor(priority_graph, hub_vertex_priority_start, 'one way', self.priority_packages)

            last_priority_vertex = result_priority[1][-1]

            all_locations_last_priority_index = list(
                filter(lambda x: last_priority_vertex.name[1] == x[1], self.all_delivery_locations))[0][0]
            all_loacations_regular_index = []
            for regular_vertex in regular_graph.vertecies_in_graph:
                for location in self.all_delivery_locations:
                    if regular_vertex.name[1] == location[1]:
                        all_loacations_regular_index.append(location[0])

            regular_graph.add_vertex(last_priority_vertex)
            for i, vertex in enumerate(regular_graph.vertecies_in_graph):
                if vertex != regular_graph.vertecies_in_graph[-1]:
                    regular_graph.add_undirected_edge(
                        last_priority_vertex, vertex, self.all_distance_matrix[all_locations_last_priority_index][all_loacations_regular_index[i]])

            hub_end = list(filter(lambda x: x.name[2] == 'HUB', regular_graph.vertecies_in_graph))[0]

            result_regular = nearest_neighbor(regular_graph, last_priority_vertex, hub_end, self.regular_packages)

        self.priority_packages = []
        self.regular_packages = []
        self.trip_delivery_locations_priority = []
        self.trip_delivery_locations_regular = []
        self.trip_distance_matrix_priority = []
        self.trip_distance_matrix_regular = []

    def __set_delivery_locations(self):
        self.trip_delivery_locations_regular = []
        self.trip_distance_matrix_regular = []
        self.trip_delivery_locations_priority = []
        self.trip_distance_matrix_priority = []

        good_rows_columns = []

        # priority
        if self.priority_packages != None and len(self.priority_packages) > 0:
            for package in [*self.priority_packages]:
                for row in self.all_delivery_locations:
                    if str(package.delivery_zip) in row[2] and package.delivery_address.lower() in row[2].lower():
                        if row[0] not in good_rows_columns:
                            good_rows_columns.append(row[0])
                            self.trip_delivery_locations_priority.append(list(row))

            if (len(self.priority_packages) > 0):
                self.trip_delivery_locations_priority.insert(0, [0, *self.all_delivery_locations[0][1:]])
                good_rows_columns.insert(0, 0)

            for i, row in enumerate(self.all_distance_matrix):
                temp = []
                if i not in good_rows_columns:
                    continue

                for j, col in enumerate(row):
                    if j not in good_rows_columns:
                        continue

                    temp.append(col)

                self.trip_distance_matrix_priority.append(temp)

            temp = []
            for i, location in enumerate(self.trip_delivery_locations_priority):
                location[0] = i
                temp.append(tuple(location))

            self.trip_delivery_locations_priority = temp
        else:
            self.trip_delivery_locations_priority = []
            self.trip_distance_matrix_priority = []

        # regular
        good_rows_columns = []

        packages = [*self.regular_packages]
        for row in self.all_delivery_locations:
            for package in packages:
                if str(package.delivery_zip) in row[2] and package.delivery_address.lower() in row[2].lower():
                    if row[0] not in good_rows_columns:
                        good_rows_columns.append(row[0])
                        self.trip_delivery_locations_regular.append(list(row))
                        packages.remove(package)

        if len(self.regular_packages) > 0:
            self.trip_delivery_locations_regular.insert(0, [0, *self.all_delivery_locations[0][1:]])
            good_rows_columns.insert(0, 0)

        for i, row in enumerate(self.all_distance_matrix):
            temp = []
            if i not in good_rows_columns:
                continue

            for j, col in enumerate(row):
                if j not in good_rows_columns:
                    continue

                temp.append(col)

            self.trip_distance_matrix_regular.append(temp)

        temp = []
        for i, location in enumerate(self.trip_delivery_locations_regular):
            location[0] = i
            temp.append(tuple(location))

        self.trip_delivery_locations_regular = temp
