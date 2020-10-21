from package import Package


class Truck:
    number: int
    priority_packages: [Package]
    regular_packages: [Package]
    distance_traveled: float
    current_location: str
    all_delivery_locations: [tuple]
    all_distance_matrix: [[float]]
    trip_delivery_locations: [tuple]
    trip_distance_matrix: [[float]]

    def __init__(self, number: int, regular_packages: [Package], all_delivery_locations, priority_packages=None):
        self.number = number
        self.priority_packages = priority_packages
        self.regular_packages = regular_packages
        self.distance_traveled = 0
        self.current_location = 'HUB'
        self.trip_delivery_locations = []
        self.trip_distance_matrix = []

        self.all_delivery_locations = []
        for i, row in enumerate(test):
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
                self.all_distance_matrix[i][j] = float(
                    self.all_distance_matrix[i][j])

        self.set_delivery_locations()

    def load_package(self, package):
        self.packages.append(package)

    def deliver_packages(self):
        if self.current_location == 'HUB' and priority_packages == None:

        else:

    def set_delivery_locations(self):
        good_rows_columns = []

        for package in self.packages:
            for row in self.all_delivery_locations:
                if str(package.delivery_zip) in row[2] and package.delivery_address in row[2].lower():
                    if row[0] not in good_rows_columns:
                        good_rows_columns.append(row[0])
                        self.trip_delivery_locations.append(list(row))

        for i, row in enumerate(self.all_distance_matrix):
            temp = []
            if i not in good_rows_columns:
                continue

            for j, col in enumerate(row):
                if j not in good_rows_columns:
                    continue

                temp.append(col)

            self.trip_distance_matrix.append(temp)
