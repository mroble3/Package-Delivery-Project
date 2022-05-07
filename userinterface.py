# Mohamed Roble Student ID #: 000975812

from csv_reader import get_hash_map
#from main import total_distance
import datetime

def userinterface(total):
    # This is the display message that is shown when the user runs the program. The interface is accessible from here
    print('Welcome to the WGUPS package tracking system!')
    print('Current route was completed in %s miles.'%(total))

    user_input = input("""
    Please select an option below to begin or type 'exit' which will allow you to quit:
        1. Get the info for all the packages at a specific time
        2. Get the info for a single package at a specific time
    """)

    while user_input is not 'exit':
        # If the user selects the First Option -> Option #1
        # 1. Get the info for all the packages at a specific time -> 0(n)
        if user_input in ['1', 1]:
            try:
                input_time = raw_input('Enter a time in (HH:MM:SS) format: ')
                (h, m, s) = input_time.split(':')
                convert_user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

                # Space-time complexity is 0(n^2)
                for count in range(1,41):
                    try:
                        first_time = get_hash_map().get_value(str(count)).delvry_strt
                        second_time = get_hash_map().get_value(str(count)).deliverytime

                        (h, m, s) = first_time.split(':')
                        convert_first_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                        (h, m, s) = second_time.split(':')
                        convert_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                    except ValueError:
                        pass

                    # Figure out which packages left the hub
                    if convert_second_time <= convert_user_time:
                        get_hash_map().get_value(str(count)).delvry_stats = 'Delivered at ' + second_time
                        get_hash_map().get_value(str(count)).deliverytime = 'Left at ' + first_time


                    # Check and see which packages have left hub but not yet delivered
                    elif convert_first_time >= convert_user_time:
                            get_hash_map().get_value(str(count)).delvry_stats = 'In transit'
                            get_hash_map().get_value(str(count)).deliverytime = 'Left at ' + first_time


                        # Checks for which packages have already been delivered
                    else:
                        get_hash_map().get_value(str(count)).delvry_stats = 'At Hub'
                        get_hash_map().get_value(str(count)).deliverytime = 'Leaves at ' + first_time

                    # Followed by printing the package currently info
                    print(
                            'Package ID: %s Delivery status: %s %s' % (
                    get_hash_map().get_value(str(count)).pkgid,
                    get_hash_map().get_value(str(count)).deliverytime,
                    get_hash_map().get_value(str(count)).delvry_stats)
                    )

            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print('Invalid entry!')
                exit()

        # Case if user selects Option #2
                # Gets the info for single package at a specific time -> O(n)
        elif user_input in ['2', 2]:
                try:
                    count = raw_input('Enter a valid package ID: ')
                    first_time = get_hash_map().get_value(str(count)).delvry_strt
                    second_time = get_hash_map().get_value(str(count)).deliverytime
                    input_time = raw_input('Enter a time (HH:MM:SS): ')
                    (h, m, s) = input_time.split(':')
                    convert_user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                    (h, m, s) = first_time.split(':')
                    convert_first_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                    (h, m, s) = second_time.split(':')
                    convert_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

                    # First Checks to figure out which packages have left the hub
                    if convert_first_time >= convert_user_time:

                        get_hash_map().get_value(str(count)).delvry_stats = 'At Hub'
                        get_hash_map().get_value(str(count)).deliverytime = 'Leaves at ' + first_time

                        # Followed by printing the package currently info
                        print('Package ID: ',get_hash_map().get_value(str(count)).pkgid)
                        print('Street address: ', get_hash_map().get_value(str(count)).addy)
                        print('Required delivery time: ', get_hash_map().get_value(str(count)).delvr)
                        print('Package weight: ', get_hash_map().get_value(str(count)).sze)
                        print('Truck status: ', get_hash_map().get_value(str(count)).delvry_stats)
                        print('Delivery status: ', get_hash_map().get_value(str(count)).deliverytime)

                    # Then checks which packages have left the hub but have not been delivered
                    elif convert_first_time <= convert_user_time:
                        if convert_user_time < convert_second_time:
                            get_hash_map().get_value(str(count)).delvry_stats = 'In transit'
                            get_hash_map().get_value(str(count)).deliverytime = 'Left at ' +  first_time

                            # Followed by printing the package currently info
                            print('Package ID: ', get_hash_map().get_value(str(count)).pkgid)
                            print('Street address: ', get_hash_map().get_value(str(count)).addy)
                            print('Required delivery time: ', get_hash_map().get_value(str(count)).delvr)
                            print('Package weight: ', get_hash_map().get_value(str(count)).sze)
                            print('Truck status: ', get_hash_map().get_value(str(count)).delvry_stats)
                            print('Delivery status: ', get_hash_map().get_value(str(count)).deliverytime)

                        # Checks for which packages have already been delivered
                        else:
                            get_hash_map().get_value(str(count)).delvry_stats = 'Delivered at ' + second_time
                            get_hash_map().get_value(str(count)).deliverytime = 'Left at ' + first_time

                            # Followed by printing the package currently info
                            print('Package ID: ', get_hash_map().get_value(str(count)).pkgid)
                            print('Street address: ', get_hash_map().get_value(str(count)).addy)
                            print('Required delivery time: ', get_hash_map().get_value(str(count)).delvr)
                            print('Package weight: ', get_hash_map().get_value(str(count)).sze)
                            print('Truck status: ', get_hash_map().get_value(str(count)).delvry_stats)
                            print('Delivery status: ', get_hash_map().get_value(str(count)).deliverytime)

                except ValueError:
                    print('Invalid entry')
                    exit()

        # 'exit'
        # Is used to exit the program
        elif user_input == 'exit':
                                exit()

        # If there is an Error
        # Print Invalid Entry and the program ends.
        else:
            print('Invalid entry!', [user_input])
            exit()



