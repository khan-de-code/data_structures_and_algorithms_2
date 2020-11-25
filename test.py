from hash_table import HashTable
from package import Package
from graph import Graph, Vertex
from permute import permute
from _time import Time
from typing import Union

graph = Graph()
vertex0 = Vertex('vertex0')
vertex1 = Vertex('vertex1')
vertex2 = Vertex('vertex2')
vertex3 = Vertex('vertex3')
start = Vertex('start')
goal = Vertex('goal')
vertexes = [vertex0, vertex1, vertex2, vertex3]

graph.add_vertex(vertex0)
graph.add_vertex(vertex1)
graph.add_vertex(vertex2)
graph.add_vertex(vertex3)
graph.add_vertex(start)

graph.add_undirected_edge(start, vertex0, 1)
graph.add_undirected_edge(start, vertex1, 2)
graph.add_undirected_edge(start, vertex2, 3)
graph.add_undirected_edge(start, vertex3, 2)

graph.add_undirected_edge(vertex0, vertex1, 6)
graph.add_undirected_edge(vertex0, vertex2, 4)
graph.add_undirected_edge(vertex0, vertex3, 8)

graph.add_undirected_edge(vertex1, vertex2, 1)
graph.add_undirected_edge(vertex1, vertex3, 7)

graph.add_undirected_edge(vertex2, vertex3, 5)

print()


def nearest_neighbor(graph: Graph, start_vertex: Vertex, end_vertex: Union[Vertex, str]):
    """Finds the greedy shortest path

    Args:
        graph (Graph)
        start_vertex (Vertex): The vertex to start at
        end_vertex (Union[Vertex, str]): Could either be a vertex to stop at or the a string. If string equals 'round trip', will calculate a round trip. If string equals 'one way' will calculate one way 

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
        distance_traveled += distance

        vertecies_yet_to_visit.remove(current_vertex)
        vertecies_visited.append(current_vertex)

    if end_vertex == 'round trip':
        distance_traveled += graph.edge_weights.find((current_vertex, start_vertex))
        vertecies_visited.append(start_vertex)

    elif end_vertex != 'round trip' and end_vertex != 'one way':
        distance_traveled += graph.edge_weights.find((current_vertex, end_vertex))
        vertecies_visited.append(end_vertex)

    return distance_traveled, tuple(vertecies_visited)


distance_traveled, visiting_order = nearest_neighbor(graph, start, 'one way')
print()


# def dijkstra_shortest_path(graph, start_vertex):
#     unvisited_vertecies = []

#     for current_vertex in graph.adjacency_list:
#         unvisited_vertecies.append(current_vertex)

#     start_vertex.distance = 0

#     while len(unvisited_vertecies) > 0:
#         smallest_index = 0

#         for i in range(1, len(unvisited_vertecies)):
#             if unvisited_vertecies[i].distance < unvisited_vertecies[smallest_index].distance:
#                 smallest_index = i
#         current_vertex = unvisited_vertecies.pop(smallest_index)

#         for adjacent_vertex in graph.adjacency_list.find(current_vertex):
#             edge_weight = graph.edge_weights.find(
#                 (current_vertex, adjacent_vertex))
#             alternative_path_distance = current_vertex.distance + edge_weight

#             if alternative_path_distance < adjacent_vertex.distance:
#                 adjacent_vertex.distance = alternative_path_distance
#                 adjacent_vertex.predecessor_vertex = current_vertex


# def get_shortest_path(start_vertex, end_vertex):
#     path = ''
#     current_vertex = end_vertex
#     path_length = 0

#     while current_vertex is not start_vertex:
#         path = ' -> ' + str(current_vertex.name) + path
#         path_length += current_vertex.distance
#         current_vertex = current_vertex.predecessor_vertex
#     path = start_vertex.name + path
#     return path + f'| Distance: {path_length}'


# dijkstra_shortest_path(graph, vertex0)
# print(get_shortest_path(vertex0, vertex3))
# for vertex in vertexes:
#     print(vertex, end='\n\n')

# for x in permute([1, 2, 3]):
#     print(x)
