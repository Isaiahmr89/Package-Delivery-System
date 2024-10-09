import csv
import datetime


def open_distance_file(file_name, distance_data):
    with open(file_name) as distance_file:
        distances = csv.reader(distance_file, delimiter=',')
        next(distances)

        for row in distances:
            distance_data.append(row)


def open_address_file(file_name, address_data):
    with open(file_name) as address_file:
        addresses = csv.reader(address_file, delimiter=',')

        for row in addresses:
            address_data.append(row[0])


# Gets the distance between two addresses. If value is empty, the addresses are then reversed
# -> O(N)
def get_distance(address_1, address_2, my_distance_data, my_address_data):
    distance = my_distance_data[my_address_data.index(address_1)][my_address_data.index(address_2)]
    if distance == '':
        distance = my_distance_data[my_address_data.index(address_2)][my_address_data.index(address_1)]
    return distance


# Finds the minimum distance between the array of addresses, then moves to the next.
# -> O(N)
def minimum_distance(address_loc, packages, my_hash, my_distance_data, my_address_data):
    minimum = 100.0
    next_address = ''
    next_id = 0
    for pack in packages:
        package = my_hash.search(pack)
        address_2 = package.address
        distance = float(get_distance(address_loc, address_2, my_distance_data, my_address_data))
        if distance < minimum:
            minimum = distance
            next_address = address_2
            next_id = pack
    return next_address, next_id, minimum


# Function to deliver packages from each truck, while finding the minimum distance between each address
# -> O(N)
def deliver_packages(truck, my_hash, my_distance_data, my_address_data):
    miles = 0
    while len(truck.packages) > 0:
        next_address, next_id, minimum = minimum_distance(truck.current_loc, truck.packages, my_hash, my_distance_data,
                                                          my_address_data)
        miles = miles + minimum
        delivery_time = minimum / 18 * 60 * 60
        dts = datetime.timedelta(seconds=delivery_time)
        truck.time = truck.time + dts
        package = my_hash.search(next_id)
        package.status = 'Delivered'
        package.delivery_time = truck.time
        truck.current_loc = next_address
        truck.packages.remove(next_id)
    return miles
