from package import Package
from permute import permute
from typing import Union
from _time import Time
import functools


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
    current_location: str
    all_delivery_locations: [tuple]
    all_distance_matrix: [[float]]
    trip_delivery_locations_priority: [tuple]
    trip_delivery_locations_regular: [tuple]
    trip_distance_matrix_priority: [[float]]
    trip_distance_matrix_regular: [[float]]

    def __init__(self, number: int, regular_packages: [Package], all_delivery_locations, priority_packages=None):

        self.time = Time(8, 0, 'AM')
        self.number = number
        self.priority_packages = priority_packages
        self.regular_packages = regular_packages
        self.distance_traveled = 0
        self.current_location = 'HUB'
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

        self.__set_delivery_locations()

    def load_package(self, package: Package, type: str):
        if type == 'regular':
            self.regular_packages.append(package)
        if type == 'priority':
            self.priority_packages.append(package)

        self.__set_delivery_locations()

    def deliver_packages(self):
        if self.priority_packages == None:

            # Helper function to calculate path length
            def path_len(path):
                print('path: ', path)
                return sum(self.trip_distance_matrix_regular[i][j] for i, j in zip(path, path[1:]))

            # Set of all nodes to visit
            to_visit = set(range(len(self.trip_distance_matrix_regular)))

            # Current state {(node, visited_nodes): shortest_path}
            state = {(i, frozenset([0, i])): [0, i]
                     for i in range(1, len(self.trip_distance_matrix_regular[0]))}

            for _ in range(len(self.trip_distance_matrix_regular) - 2):
                next_state = {}
                for position, path in state:
                    print(position, path, state[(position, path)])

                    current_node, visited = position, path

                    # Check all nodes that haven't been visited so far
                    for node in to_visit - visited:
                        new_path = state[(position, path)] + [node]
                        new_pos = (node, frozenset(new_path))

                        # Update if (current node, visited) is not in next state or we found shorter path
                        if new_pos not in next_state or path_len(new_path) < path_len(next_state[new_pos]):
                            next_state[new_pos] = new_path

                state = next_state

            # Find the shortest path from possible candidates
            print(state)
            # shortest = []
            # for item in state:
            #     print(state[item])
            #     shortest = min(state[item], key=path_len)
            shortest = min((path + [0] for path in state.values()), key=path_len)
            print('path: {0}, length: {1}'.format(shortest, path_len(shortest)))
        else:
            def __build_distance_map(iterable, package_type, start_from='HUB', end_at='HUB'):
                map_array = []

                for each in iterable:
                    map = ()

                    # Distance from hub to first package
                    if start_from == 'HUB':
                        first_package_address_info = each[0].get_address_info()
                        first_package_index = None
                        for i, address in enumerate(self.all_delivery_locations):
                            if str(first_package_address_info[3]) in address[2] and first_package_address_info[0] in address[2]:
                                first_package_index = i

                        distance_between_HUB_and_first_package = self.all_distance_matrix[0][first_package_index]
                        map += (distance_between_HUB_and_first_package,)

                    # Distances between each package
                    for i, package in enumerate(each):
                        if i + 1 != len(each):
                            package1_address_info = package.get_address_info()
                            package2_address_info = each[i + 1].get_address_info()
                            package1_index = None
                            package2_index = None

                            delivery_locations = self.trip_delivery_locations_priority if package_type == 'priority' else self.trip_delivery_locations_regular
                            for address in delivery_locations:
                                if str(package1_address_info[3]) in address[2] and package1_address_info[0] in address[2]:
                                    package1_index = address[0]
                                if str(package2_address_info[3]) in address[2] and package2_address_info[0] in address[2]:
                                    package2_index = address[0]

                            trip_distance_matrix = self.trip_distance_matrix_priority if package_type == 'priority' else self.trip_distance_matrix_regular
                            distance_between_package1_and_package2 = trip_distance_matrix[package1_index][package2_index]
                            map += (distance_between_package1_and_package2,)

                    if end_at == 'HUB':
                        last_package_address_info = each[len(each) - 1].get_address_info()
                        last_package_index = None
                        for i, address in enumerate(self.all_delivery_locations):
                            if str(last_package_address_info[3]) in address[2] and last_package_address_info[0] in address[2]:
                                last_package_index = i

                        distance_between_HUB_and_last_package = self.all_distance_matrix[0][last_package_index]
                        map += (distance_between_HUB_and_last_package,)

                    map_array.append(map)

                return map_array

            # Priority packages
            priority_package_permutations = []
            for permutation in permute(self.priority_packages):
                priority_package_permutations.append(permutation)

            priority_distance_map = __build_distance_map(priority_package_permutations, 'priority', end_at=None)
            priority_package_permutations = [('HUB',) + elem for elem in priority_package_permutations]
            priority_combined = [[priority_distance_map[x], priority_package_permutations[x]] for x in range(len(priority_distance_map))]

            # Regular packages
            regular_package_permutations = []
            for permutation in permute(self.regular_packages):
                regular_package_permutations.append(permutation)

            regular_distance_map = __build_distance_map(regular_package_permutations, 'regular', start_from=None)
            regular_package_permutations = [elem + ('HUB',) for elem in regular_package_permutations]
            regular_combined = [[regular_distance_map[x], regular_package_permutations[x]] for x in range(len(regular_distance_map))]

            def __calculate_minutes_travel(distance: int) -> float:
                return distance / (18 / 60)

            for x, path in enumerate(priority_combined):
                test_time = self.time.clone()
                delivered_at = [test_time.clone()]
                total_distance = 0
                for i, distance in enumerate(path[0]):
                    destination_a = path[1][i]
                    destination_b = path[1][i + 1]

                    mins_traveled = __calculate_minutes_travel(distance)
                    test_time.add_time(minute=int(mins_traveled), fractions_of_a_minute=mins_traveled - int(mins_traveled))
                    delivered_at.append(test_time.clone())

                    total_distance += distance

                priority_combined[x].append(tuple(delivered_at))
                priority_combined[x].append(total_distance)

            def __sort_combined(a, b):
                if a[3] > b[3]:
                    return 1
                elif a[3] < b[3]:
                    return -1
                else:
                    return 0

            priority_combined.sort(key=functools.cmp_to_key(__sort_combined))

            priority_path_length = 0
            time_elapsed = None
            for path in priority_combined:
                onto_next = False
                for i, package in enumerate(path[1]):
                    if package == 'HUB':
                        continue

                    if not package.delivery_deadline.minutes_from_8 > path[2][i].minutes_from_8:
                        onto_next = True
                        break
                if not onto_next:
                    priority_path_length = path[3]
                    time_elapsed = __calculate_minutes_travel(priority_path_length)
                    break

            print()

    def __set_delivery_locations(self):
        good_rows_columns = []

        # priority
        if self.priority_packages != None and len(self.priority_packages) > 0:
            for package in [*self.priority_packages]:
                for row in self.all_delivery_locations:
                    if str(package.delivery_zip) in row[2] and package.delivery_address.lower() in row[2].lower():
                        if row[0] not in good_rows_columns:
                            good_rows_columns.append(row[0])
                            self.trip_delivery_locations_priority.append(
                                list(row))

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

        if self.priority_packages == None:
            temp = []
            for location in self.trip_delivery_locations_regular:
                temp.append([location[0] + 1, location[1:]])

            self.trip_delivery_locations_regular = temp
            self.trip_delivery_locations_regular.insert(0, [0, [*self.all_delivery_locations[0][1:]]])
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
