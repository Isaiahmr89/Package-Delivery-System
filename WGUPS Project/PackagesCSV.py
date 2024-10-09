import csv

# makes package object and assigns given values to each package with updates
class Package:
    def __init__(self, id, address, city, state, zip, delivery, mass):
        self.id = id
        self.address = address
        self.state = state
        self.city = city
        self.zip = zip
        self.delivery = delivery
        self.mass = mass
        self.status = 'at hub'
        self.delivery_time = None
        self.time_left = None

    def __str__(self):
        return '%s | %s | %s, %s | %s | %s | %s | Departs At: %s | Status: %s | Delivery Time: %s' % (self.id, self.address, self.state, self.city, self.zip, self.delivery, self.mass, self.time_left, self.status, self.delivery_time)

def open_file(csv_file, my_hash):

    with open(csv_file) as pkg:
        packages_data = csv.reader(pkg, delimiter=',')
        next(packages_data)

        for item in packages_data:
            id = int(item[0])
            address = item[1]
            city = item[2]
            state = item[3]
            zip = item[4]
            delivery = item[5]
            mass = item[6]

            pkg = Package(id, address, city, state, zip, delivery, mass)

            my_hash.insert(id, pkg)

# Function to print entire hash table
# -> O(N)
def print_packages(my_hash):
    for row in range(len(my_hash.table)):
        print('Package: {}'.format(my_hash.search(row + 1)))

# Truck object to creste trucks to deliver packages. All trucks start at the hub
class Truck:
    def __init__(self, time_left, packages):
        self.time_left = time_left
        self.packages = packages
        self.current_loc = '4001 South 700 East'
        self.time = time_left