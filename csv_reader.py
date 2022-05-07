import csv
from Package import Package
from hash_table import HashMap
def read_distances():
    distance_table = []
    with open('./daata/distance_data.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        for row in read_csv:
            distance_table.append(row)
    return distance_table

def read_addresses():
    address_table = []
    with open('./daata/distance_name_data.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        for row in read_csv:
            row[0] = int(row[0])
            address_table.append(row)
    return address_table


def read_packages():
    with open('./daata/input_data.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')

        hash_map = HashMap()  # Calls Hashmap class to create an object of Hashmap
        # Read in values from csv file into key/value pairs inside of the hash table
        # space-time complexity is 0(n)
        for row in read_csv:
                package_id = int(row[0])
                address = row[1]
                city = row[2]
                state = row[3]
                zip = row[4]
                delivery = row[5]
                size = [6]
                note = [7]
                delivery_start = [8]
                address_location = [9]
                delivery_status = [10]

                value = Package(package_id, address_location, address, city, state, zip, delivery, size, note, delivery_start, delivery_status)

                # Conditional statements to determine which packages are on which trucks.

                '''# change the wrong address package to the correct address
                if '84104' in row[4] and '10:30' not in delivery:
                    final_delivery.append(value)
    
                # First truck's first delivery
                if delivery != 'EOD':
                    if 'Must' in row[5] or 'None' in row[5]:
                        first_truck_delivery.append(value)
    
                # Second truck's delivery
                if 'Can only be' in row[7] or 'Delayed' in row[7]:
                    second_truck_delivery.append(value)
    
                # Check remaining packages
                if value not in first_truck_delivery and value not in second_truck_delivery and value not in final_delivery:
                    second_truck_delivery.append(value) if len(second_truck_delivery) < len(
                        final_delivery) else final_delivery.append(value)
    '''
                # Insert value into the hash table
                hash_map.insert(package_id, value)
    return hash_map

