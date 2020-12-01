# Created By: Dawson Batz 001111079

from importer import import_packages, import_distances
from truck import Truck
from package import Package
from _time import Time


def main():
    print('Setting up...', end='\n\n')

    packages = import_packages()
    distances = import_distances()

    def __simplify(items: [int]):
        return [packages.find(str(package)) for package in items]

    print('Delivering packages on Truck 1')
    delivery = __simplify([15, 16, 34, 20, 21, 13, 39, 19, 4, 40, 1, 14, 27, 35, 2, 33])
    truck1 = Truck(1, delivery, distances)
    truck1.deliver_packages()

    print('Delivering packages on Truck 2')
    delivery2 = __simplify([5, 37, 38, 8, 30, 25, 26, 24, 9, 3, 31, 32, 6, 17, 29, 7])
    truck2 = Truck(2, delivery2, distances, departure_time=Time(9, 5, 'AM'))
    truck2.deliver_packages()

    print('Delivering packages on Truck 2, round 2')
    delivery3 = __simplify([10, 22, 23, 12, 28, 11, 18, 36])
    truck2.load_packages(delivery3, 'regular')
    truck2.deliver_packages()

    print(f'\nDistance Travled By Truck 1: {round(truck1.distance_traveled, 2)}')
    print(f'Distance travled by Truck 2: {round(truck2.distance_traveled, 2)}')
    print(f'Total distance travled by all trucks: {round(truck1.distance_traveled + truck2.distance_traveled, 2)}')

    print('\nFinished setting up', end='\n\n')

    print('You can now query for the status of all packages at various times througout the day. To do so, please enter the time you would like to query below.')

    while True:
        print('\nTime: ')

        hour = int(input('hour: '))
        minute = int(input('minute: '))
        am_pm = input('AM or PM: ')

        if hour > 12 or hour < 0:
            print('The hour provided was not a valid hour. Please retry.')
            continue

        if minute > 59 or minute < 0:
            print('The minute provided was not a valid minute. Please retry.')
            continue

        if am_pm != 'AM' and am_pm != 'PM':
            print("AM or PM was not provided as 'AM' or 'PM'. Please retry.")
            continue

        time_to_check = Time(hour, minute, am_pm)

        for package in packages:
            package = packages.find(package)
            if package.delivered_time > time_to_check:
                print(f'Package: {package} Status: in route')
            elif package.delivered_time <= time_to_check:
                print(f'Package: {package} Status: delivered')


if __name__ == '__main__':
    main()
