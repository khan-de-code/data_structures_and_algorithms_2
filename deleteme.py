from importer import import_packages, import_distances
from truck import Truck
from package import Package
from _time import Time

packages = import_packages()
distances = import_distances()

for package in packages:
    package = packages.find(package)
    if package.delivery_address == '5383 South 900 East #104':
        package.delivery_address = '5383 S 900 East #104'

# truck1 = Truck(1, [packages.find('1')], distances, [
#                packages.find('2'), packages.find('3')])

# truck1 = Truck(1, [packages.find('2'), packages.find('3')], distances, [packages.find('1'), packages.find('6'), packages.find('13')])


def __simplify(items: [int]):
    return [packages.find(str(package)) for package in items]


def print_it(truck, delivery, final_delivery):
    final_delivery = final_delivery + tuple(delivery)
    print(f'Truck{truck.number}')
    for package in delivery:
        spacing = ''
        if package.delivery_deadline == 'EOD':
            spacing = '        |   '
        else:
            spacing = '   |   '
        print(package.delivered_time, '   |   ', package.delivery_deadline, spacing, package.package_id)
    print(len(delivery))
    print(truck.distance_traveled, truck.time, end='\n\n\n')

    return final_delivery


final_delivery = tuple()
# truck1 = Truck(1, __simplify([2, 4, 5, 7, 8, 10, 19]), distances, __simplify([13, 14, 15, 16, 20, 1, 34, 29, 30]))
# truck1 = Truck(1, __simplify([15, 16, 34, 20, 21, 13, 39, 37, 14, 19, 10, 22, 1, 11, 17, 12]), distances, __simplify([3, 4]))
delivery = __simplify([15, 16, 34, 20, 21, 13, 39, 19, 4, 40, 1, 14, 27, 35, 2, 33])
truck1 = Truck(1, delivery, distances)
truck1.deliver_packages()
final_delivery = print_it(truck1, delivery, final_delivery)

delivery2 = __simplify([5, 37, 38, 8, 30, 25, 26, 24, 9, 3, 31, 32, 6, 17, 29, 7])
truck2 = Truck(2, delivery2, distances, departure_time=Time(9, 5, 'AM'))
truck2.deliver_packages()
final_delivery = print_it(truck2, delivery2, final_delivery)

delivery3 = __simplify([10, 22, 23, 12, 28, 11, 18, 36])
truck2.load_packages(delivery3, 'regular')
truck2.deliver_packages()
final_delivery = print_it(truck2, delivery3, final_delivery)


# delivery3 = __simplify([10, 22, 23, 12, 11])
# truck1.load_packages(delivery3, 'regular')
# truck1.deliver_packages()
# print_it(truck1, delivery3, final_delivery)

# delivery4 = __simplify([8, 16, 28])
# truck2.load_packages(delivery4, 'regular')
# truck2.deliver_packages()
# print_it(truck2, delivery4, final_delivery)


final_delivery = list(final_delivery)
for i, each in enumerate(final_delivery):
    if i+1 < len(final_delivery) - 1 and each in final_delivery[i+1:]:
        print(f'You fucked up. {each} Is duplicated.')

print(truck1.distance_traveled + truck2.distance_traveled)

for package in packages:
    package = packages.find(package)
    if package.status != 'delivered':
        print(package)
else:
    print('all delivered')
# print('Finished first route for truck1', truck1.distance_traveled, truck1.time)
# for each in __simplify([15, 16, 34]):
#     print(each.delivered_time)

# truck1.load_packages(__simplify([33, 35, 39, 23, 24, 26, 27, 22]), 'regular')
# truck1.deliver_packages()
# print('Finished second route for truck1', truck1.distance_traveled, truck1.time)

# package_9 = packages.find('9')
# package_9.delivery_address = '410 S State St'
# package_9.delivery_city = 'Salt Lake City'
# package_9.delivery_state = 'UT'
# package_9.delivery_zip = 84111

# packages.add('9', package_9)

# truck1.load_packages([package_9], 'regular')
# truck1.deliver_packages()
# print('Finished last route for truck1', truck1.distance_traveled, truck1.time)

# truck2 = Truck(2, __simplify([11]), distances, __simplify([25, 31, 37, 40]))
# truck2.deliver_packages()
# print('Finished first route for truck2', truck2.distance_traveled, truck2.time)

# truck2.load_packages(__simplify([3, 18, 28, 32, 36, 38, 12, 17, 21]), 'regular')
# truck2.load_packages(__simplify([6, 25]), 'priority')
# truck2.deliver_packages()
# print('Finished last route for truck2', truck2.distance_traveled, truck2.time)
# print('Finished all routes for all trucks')


print()
