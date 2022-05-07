#Mohamed Roble Student ID: #000975812
import datetime

import csv_reader
from Package import Package
from Truck import Truck

'''
p = Package(1)
print(p.packageid)
print(p.isDelivered())
'''

# The times represent the times the trucks leave the hub

hashmap = csv_reader.read_packages()
#print(hashmap)
distance_table = csv_reader.read_distances()
#print(distance_table)
address_list = csv_reader.read_addresses()
#print(address_list)

'''Implement Nearest Neighbor Algorithm'''

def get_address_index(address_to_find):
    for address_object in address_list:
        if address_object[2] == address_to_find:
            return address_object[0]
    return -1

def get_address_distance(starting_address, ending_address):
    start_index = get_address_index(starting_address)
    ending_index = get_address_index(ending_address)
    #print(starting_address,ending_address,start_index, ending_index)
    if ending_index > start_index:
        return float(distance_table[ending_index][start_index])
    else:
        return float(distance_table[start_index][ending_index])
    return 0.0

def has_more_packages_to_deliver(truck):
    for package_id in truck.packagelist:
        package_object = hashmap.get_value(package_id)
        if package_object.isNotDelivered():
            return True
    return False
'''

Nearest Neighbor Algorithm

We would go through each package individually to determine the closest address to the Hub, by inputting each address
into the GPS system to show the shortest distance from the Hub.
Once nearest address is found the driver starts his/her route for delivery, 
and once delivered the driver continues to proceed
from the current address onto the next closest address. 

while the truck has more packages to deliver:
    for the remaining packages:
        get package with minimum distance
        mark the packages delivered
'''
def deliver_packages_for_truck(truck,starting_address):
    '''
    We need to define the starting address
    :param truck:
    :return:
    '''
    current_address = starting_address
    current_time = truck.starttime
    while has_more_packages_to_deliver(truck):
        '''
        Need to setup minimum distance variables for minimum distance & minimum package id
        '''
        minimum_distance = 999.9
        minimum_package = None
        for package_id in truck.packagelist:
            package_object = hashmap.get_value(package_id)
            if package_object.isNotDelivered():
                distance = get_address_distance(current_address,package_object.addy)
                if distance < minimum_distance:
                    minimum_distance = distance
                    minimum_package = package_object


        '''This is where we mark the package delivered'''
        current_address = minimum_package.addy
        current_time = current_time + datetime.timedelta(hours=(minimum_distance/18))
        minimum_package.deliverytime = current_time
        minimum_package.mileage = minimum_distance
        minimum_package.delvry_strt = truck.starttime

first_leave_time = datetime.datetime(2022,4,21,8,0,0)
second_leave_time = datetime.datetime(2022,4,21,9,00,0)
third_leave_time = datetime.datetime(2022,4,21,11,0,0)

pkg_list = [1, 13, 14, 15, 16, 19, 20, 2, 4, 5, 7, 8, 10, 11, 12, 17]
truck1 = Truck(1,pkg_list,first_leave_time)
deliver_packages_for_truck(truck1,"4001 South 700 East")
truck1_mileage = sum([hashmap.get_value(i).mileage for i in truck1.packagelist])


for package_id in pkg_list:
    pkg = hashmap.get_value(package_id)


pkg_list = [3, 6, 18, 25, 29, 30, 31, 34, 36, 37, 38, 40, 21, 22]
truck2 = Truck(2,pkg_list,second_leave_time)
deliver_packages_for_truck(truck2,"4001 South 700 East")
truck2_mileage = sum([hashmap.get_value(i).mileage for i in truck2.packagelist])

for package_id in pkg_list:
    pkg = hashmap.get_value(package_id)

pkg_list = [9, 28, 32, 23, 24, 26, 27, 33, 35, 39]
truck3 = Truck(3,pkg_list,third_leave_time)
deliver_packages_for_truck(truck3,"4001 South 700 East")
truck3_mileage = sum([hashmap.get_value(i).mileage for i in truck3.packagelist])


for package_id in pkg_list:
    pkg = hashmap.get_value(package_id)


print('Welcome to the WGUPS package tracking system!')
print('Current route was completed in %s miles.' % (truck3_mileage + truck2_mileage + truck1_mileage))

while 1:


    user_input = input("""
        Please select an option below to begin or type 'exit' which will allow you to quit:
            1. Get the info for all the packages at a specific time
            2. Get the info for a single package at a specific time
        """)
    if user_input in ['1', 1]:

            input_time = raw_input('Enter a time in (HH:MM:SS) format: ')
            (h, m, s) = input_time.split(':')
            convert_user_time = datetime.datetime(2022,4,21,int(h),int(m),int(s))

            # Space-time complexity is 0(n^2)
            for package_id in range(1, 41):
                pkg = hashmap.get_value(package_id)
                if pkg.deliverytime < convert_user_time:
                    pkg.delvry_stats = "delivered"
                elif convert_user_time > pkg.delvry_strt:
                    pkg.delvry_stats = "in route"
                else:
                    pkg.delvry_stats = "at the hub"
                print(str(pkg))
# We set delivery_start to first_leave_time for all of truck one's packages -> 0(n)
'''for index, value in enumerate(csv_reader.get_first_delivery()):
    csv_reader.get_first_delivery()[index].delvry_strt = first_leave_time[0]
    first_delivery.append(csv_reader.get_first_delivery()[index])

# Compare truck one addresses to address list -> O(n^2)
for index, outer in enumerate(first_delivery):
    for inner in distance.get_address():
        if outer[2] == inner[2]:
            first_truck_distance_list.append(outer[0])
            first_delivery[index][1] = inner[0]

# Call algorithm to sort packages for first truck
distance.get_shortest_route(first_delivery, 1, 0)
total_distance_1 = 0

# The for loop calculates the total distance of the first truck and distance of each package
# Space-time complexity is 0(n)
for index in range(len(distance.first_truck_index())):
    try:
        # calculate the total distance of the truck
        total_distance_1 = distance.get_distance(int(distance.first_truck_index()[index]), int(distance.first_truck_index()[index + 1]), total_distance_1)

        # calculate the distance of each package along the route
        deliver_package = distance.get_time(distance.get_current_distance(int(distance.first_truck_index()[index]), int(distance.first_truck_index()[index + 1])), first_leave_time)
        distance.first_truck_list()[index][10] = (str(deliver_package))
        csv_reader.get_hash_map().update(int(distance.first_truck_list()[index][0]), first_delivery)
    except IndexError:
        pass

# Set delivery_start to second_leave_time for all truck two packages
# Space-time complexity is 0(n)
for index, value in enumerate(csv_reader.get_second_delivery()):
    csv_reader.get_second_delivery()[index].delvry_strt = second_leave_time[0]
    second_delivery.append(csv_reader.get_second_delivery()[index])

# Compare truck two addresses to address list -> O(n^2)
for index, outer in enumerate(second_delivery):
    for inner in distance.get_address():
        if outer.addy == inner[2]:
            second_truck_distance_list.append(outer.pkgid)
            outer.add_location = inner[0]

# Call algorithm to sort packages for the second truck
distance.get_shortest_route(second_delivery, 2, 0)
total_distance_2 = 0
# Calculate total distance of the second truck and distance of each package -> O(n)
for index in range(len(distance.second_truck_index())):
    try:
        total_distance_2 = distance.get_distance(int(distance.second_truck_index()[index]),
                                                 int(distance.second_truck_index()[index + 1]), total_distance_2)

        deliver_package = distance.get_time(distance.get_current_distance(int(distance.second_truck_index()[index]), int(distance.second_truck_index() [index + 1])), second_leave_time)
        distance.second_truck_list()[index].deliverytime = (str(deliver_package))
        csv_reader.get_hash_map().update(int(distance.second_truck_list()[index].pkgid), second_delivery)
    except IndexError:
        pass

# Set delivery_start to third_leave_time for all truck three packages
# Space-time complexity is 0(n)
for index, value in enumerate(csv_reader.get_final_delivery()):
    csv_reader.get_final_delivery()[index].delvry_strt = third_leave_time[0]
    third_delivery.append(csv_reader.get_final_delivery()[index])

# Compare the three truck's addresse's to the list of addresses -> O(n^2)
for index, outer in enumerate(third_delivery):
    for inner in distance.get_address():
        if outer.addy == inner[2]:
            third_truck_distance_list.append(outer.pkgid)
            third_delivery[index].add_location = inner[0]

# Call algorithm to sort packages for third truck
distance.get_shortest_route(third_delivery, 3, 0)
total_distance_3 = 0

# Calculate the total distance of the third truck along with the distance of each individual package
# Space-time complexity is 0(n)
for index in range(len(distance.third_truck_index())):
    try:
        total_distance_3 = distance.get_distance(int(distance.third_truck_index()[index]), int(distance.third_truck_index()[index + 1]), total_distance_3)

        deliver_package = distance.get_time(distance.get_current_distance(int(distance.third_truck_index()[index]), int(distance.third_truck_index()[index + 1])), third_leave_time)
        distance.third_truck_list()[index].deliverytime = (str(deliver_package))
        csv_reader.get_hash_map().update(int(distance.third_truck_list()[index].pkgid), third_delivery)
    except IndexError:
        pass

# Returns the total distance of all three trips used to calculate the distance of all packages
# Space-time complexity is O(1)
def total_distance():
    return total_distance_1 + total_distance_2 + total_distance_3

userinterface.userinterface(total_distance_1 + total_distance_2 + total_distance_3)'''



