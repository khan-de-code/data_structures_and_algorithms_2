from importer import import_packages, import_distances
from truck import Truck
from package import Package


def main():
    print('Setting up...')

    packages = import_packages()
    distances = import_distances()

    def __simplify(packages: [int]):
        return [packages.find(str(package)) for package in packages]

    truck1 = Truck(1, __simplify([2, 4, 5, 7, 8, 19]), distances, __simplify([13, 14, 15, 16, 20, 1, 34, 29, 30, 31]))
    truck1.deliver_packages()

    print('Finished setting up', end='\n\n')

    print('You can now query for the status of all packages at various times througout the day. To do so, please enter the time you would like to query below.')

    while True:
        userInput = input('Time: ')


if __name__ == '__main__':
    main()
