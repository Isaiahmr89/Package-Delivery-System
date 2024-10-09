# Isaiah Ragland
# Student ID: 009570014

import HashTable
import PackagesCSV
import DistanceCSV
import datetime

def main_menu():
    # Displays interactive UI for the user
    print('\n1: Print all packages and total milage')
    print('2: Lookup all package statuses at a certain time')
    print('3: Lookup a single package with ID number')
    print('4: Exit program')

def main_module():
    print('Welcome to the WGUPS Routing Program!')

    my_hash = HashTable.HashTable()
    # Stores distance data
    my_distance_data = []
    # Stores address data
    my_address_data = []

    PackagesCSV.open_file('WGUPSPackageFile.csv', my_hash)
    DistanceCSV.open_distance_file('WGUPSDistanceTable.csv', my_distance_data)
    DistanceCSV.open_address_file('WGUPSDistanceNames.csv', my_address_data)

    # Truck 1
    # Time object starts deliveries at 8:00
    start_time = '08:00:00'
    h,m,s = start_time.split(':')
    time_obj = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    # Package list to determine what time each package has left
    pkg_list = [1, 13, 39, 14, 15, 16, 34, 19, 20, 21, 7, 29, 40, 4, 30]
    t1 = PackagesCSV.Truck(time_obj, pkg_list)
    for pkg in t1.packages:
        pkg = my_hash.search(pkg)
        pkg.time_left = time_obj

    # Truck 2
    # Time object starts deliveries at 9:06
    start_time = '09:06:00'
    h,m,s = start_time.split(':')
    time_obj = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

    pkg_list = [3, 18, 36, 38, 37, 5, 6, 25, 26, 28, 32, 31, 27]
    t2 = PackagesCSV.Truck(time_obj, pkg_list)
    for pkg in t2.packages:
        pkg = my_hash.search(pkg)
        pkg.time_left = time_obj

    # Truck 3
    # Time object starts deliveries at 11:00
    start_time = '11:00:00'
    h,m,s = start_time.split(':')
    time_obj = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

    pkg_list = [2, 8, 9, 10, 11, 12, 17, 22, 23, 24, 33, 35]
    t3 = PackagesCSV.Truck(time_obj, pkg_list)
    for pkg in t3.packages:
        pkg = my_hash.search(pkg)
        pkg.time_left = time_obj

    # Collects total distance fom each trucks deliveries and stores them in variables
    truck1_miles = DistanceCSV.deliver_packages(t1, my_hash, my_distance_data, my_address_data)
    truck2_miles = DistanceCSV.deliver_packages(t2, my_hash, my_distance_data, my_address_data)
    truck3_miles = DistanceCSV.deliver_packages(t3, my_hash, my_distance_data, my_address_data)

    choice = 0
    # -> O(N)
    while int(choice) != 4:
        main_menu()
        total_miles = truck1_miles + truck2_miles + truck3_miles
        choice = input('Enter an option: ')
        if int(choice) == 1:
            PackagesCSV.print_packages(my_hash)
            print('\nTotal distance for package delivery is:', total_miles, 'miles.\n')

        elif int(choice) == 2:
            # Time input to determine status of all packages at any given time during deliveries
            input_time = input('Enter a time (HH:MM:SS): ')
            h, m, s = input_time.split(':')
            time_obj = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            # -> O(N^2)
            for row in range(len(my_hash.table)):
                pkg = my_hash.search(row + 1)
                # Checks to see if packages are still at the hub
                if time_obj < pkg.time_left:
                    print(f'Package: {pkg.id} | {pkg.address} | {pkg.state}, {pkg.city} | {pkg.zip} | {pkg.delivery} | {pkg.mass} | Departs At: {pkg.time_left} | Status: At Hub')
                # Seconf check to see if the packages are in en route to destination
                elif time_obj >= pkg.time_left:
                    # Finally checks to see if packages have been delivererd if both conditions have not been met
                    if time_obj < pkg.delivery_time:
                        print(f'Package: {pkg.id} | {pkg.address} | {pkg.state}, {pkg.city} | {pkg.zip} | {pkg.delivery} | {pkg.mass} | Departs At: {pkg.time_left} | Status: En Route')
                    else:
                        print(f'Package: {pkg.id} | {pkg.address} | {pkg.state}, {pkg.city} | {pkg.zip} | {pkg.delivery} | {pkg.mass} | Departs At: {pkg.time_left} | Status: Delivered {pkg.delivery_time}')


        elif int(choice) == 3:
            # Input to determine a specific package status at any time.
            package_id = input('Enter package ID: ')
            input_time = input('Enter a time (HH:MM:SS): ')
            h, m, s = input_time.split(':')
            time_obj = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

            pkg = my_hash.search(int(package_id))
            # Checks to see if the package is still at the hub
            if time_obj < pkg.time_left:
                    print(f'Package: {pkg.id} | {pkg.address} | {pkg.state}, {pkg.city} | {pkg.zip} | {pkg.delivery} | {pkg.mass} | Time Left: {pkg.time_left} | Status: At Hub')
            # Second check to see if package is en route to destination
            elif time_obj >= pkg.time_left:
                # Finally checks to see if the package have been delivererd if both conditions have not been met
                if time_obj < pkg.delivery_time:
                    print(f'Package: {pkg.id} | {pkg.address} | {pkg.state}, {pkg.city} | {pkg.zip} | {pkg.delivery} | {pkg.mass} | Time Left: {pkg.time_left} | Status: En Route')
                else:
                    print(f'Package: {pkg.id} | {pkg.address} | {pkg.state}, {pkg.city} | {pkg.zip} | {pkg.delivery} | {pkg.mass} | Time Left: {pkg.time_left} | Status: Delivered {pkg.delivery_time}')
        # Exits the program
        else:
            print('Exiting program...')
            exit()

if __name__ == '__main__':
    main_module()