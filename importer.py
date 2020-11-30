import csv
from hash_table import HashTable
from package import Package


def import_packages():
    """Imports the packages from a csv file.

    Returns:
        HashTable: Returns a hash table with all packages from the csv in it.

    Space & Time Complexity:
        Time Complexity:
            Big-O(N^2)
        Space Complexity:
            Big-O(N^2)
    """

    packages = []

    with open('WGUPS Package File.csv', encoding='utf-8-sig', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')

        for row in csv_reader:
            package = []
            for col in row:
                if col != '':
                    package.append(col.strip())

            packages.append(tuple(package))

    package_hash = HashTable()
    for package in packages:
        package_hash.add(str(package[0]), Package(*package))

    return package_hash


def import_distances():
    """Imports the distance matrix for each package destination.

    Returns:
        [[Union[str, float]]]: The matrix of package destinations.

    Space & Time Complexity:
        Time Complexity:
            Big-O(N^2)
        Space Complexity:
            Big-O(N^2)
    """

    distances = []

    with open('WGUPS Distance Table.csv', encoding='utf-8-sig', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')

        for row in csv_reader:
            row_stuff = []
            for col in row:
                row_stuff.append(col.strip())

            distances.append(tuple(row_stuff))

        return distances
