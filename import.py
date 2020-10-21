import csv
from hash_table import HashTable
from package import Package


def import_packages():
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
        package_hash.add(int(package[0]), Package(*package))

    return package_hash


print(import_packages().find(25))


def import_distances():
    distances = []

    with open('WGUPS Distance Table.csv', encoding='utf-8-sig', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')

        for row in csv_reader:
            row_stuff = []
            for col in row:
                row_stuff.append(col.strip())

            distances.append(tuple(row_stuff))

        return distances
