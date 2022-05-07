import csv
import datetime

# Read in csv files
with open('./daata/distance_data.csv') as csvfile_01:
    distance_csv = list(csv.reader(csvfile_01, delimiter=','))
with open('./daata/distance_name_data.csv') as csvfile_02:
    distance_name_csv = list(csv.reader(csvfile_02, delimiter=','))

    # Get package address data -> 0(n)
    def get_address():
        return distance_name_csv

# The total distance from the row/column values -> 0(1) will be calculated
def get_distance(row, col, total):
    distance = distance_csv[row][col]
    if distance == '':
        distance = distance_csv[col][row]

    return total + float(distance)

# The current distance from row/column values -> 0(1) will be calculated
def get_current_distance(row, col):
    distance = distance_csv[row][col]
    if distance == '':
        distance = distance_csv[col][row]

    return float(distance)

# The total distance for a given truck will be calculated
# runtime of function is 0(n)
def get_time(distance, truck_list):
    new_time = distance / 18
    distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(
        *divmod(new_time * 60, 60))
    final_time = distance_in_minutes + ':00'
    truck_list.append(final_time)
    total = datetime.timedelta()
    for i in truck_list:
        (h, m, s) = i.split(':')
        total += datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    return total

    # these lists represent the sorted trucks that are put in order of efficiency in the function below



    # The algorithm below will use a greedy approach to figure out the best location the trucks will visit
    # based on the trucks current location.

    # The algorithm has 3 parameters. Which include:
    # 1st. Non-optimized list of packages on truck
    # 2nd. The truck's number
    # 3rd. Current location of truck, which will update as the location changes.

    # The use of the first for loop is that it allows us to find the smallest distance to the next location.
    # This will break once the input list has a size of 0 or minimum value is found.

    # The for loop starts by setting "lowest value" to 50.0 and then uses the get_current_distance function
    # to loop through every possible point that is available in order to ensure there is not a lower value that 50.0
    # If there is a value lower than 50.0 then the lowest value is updated and the search will continue once again.
    # Once all possible routes have been searched the truck is permitted to go with the available packages.
    # Which then adds the package object and associated index to the new list.
    # A recursive call is made for the next location and shortened list. Recursive calls will continually be made
    # until the base case is called, which will end the function and return the now empty list.

    # The Space-Time Complexity is 0(n^2).

def get_shortest_route(_list, num, curr_location):
    if not len(_list):
        return _list

    lowest_value = 50.0
    location = 0

    for index in _list:
        value = int(index.add_location)
        if get_current_distance(curr_location, value) <= lowest_value:
            lowest_value = get_current_distance(
                curr_location, value)
            location = value

    for index in _list:
        if get_current_distance(curr_location, int(index.add_location)) == lowest_value:
            if num == 1:
                first_truck.append(index)
                first_truck_indices.append(index.add_location)
                _list.pop(_list.index(index))
                curr_location = location
                get_shortest_route(_list, 1, curr_location)
            elif num == 2:
                second_truck.append(index)
                second_truck_indices.append(index.add_location)
                _list.pop(_list.index(index))
                curr_location = location
                get_shortest_route(_list, 2, curr_location)
            elif num == 3:
                third_truck.append(index)
                third_truck_indices.append(index.add_location)
                _list.pop(_list.index(index))
                curr_location = location
                get_shortest_route(_list, 3, curr_location)

    # Insert 0 for the first index of each index list
    first_truck_indices.insert(0, '0')
    second_truck_indices.insert(0, '0')
    third_truck_indices.insert(0, '0')


    # Below are all helper functions to return a desired value space-time complexity of O(1)
def first_truck_index():
    return first_truck_indices


def first_truck_list():
    return first_truck


def second_truck_index():
    return second_truck_indices


def second_truck_list():
    return second_truck


def third_truck_index():
    return third_truck_indices


def third_truck_list():
    return third_truck

