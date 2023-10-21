##############################################
# CSC-500 Module 3 - Part 2 Assignment
# Programmer - Frank Stadler
##############################################

def main():
    # ask user for input - current hour
    current_hour = input('Please enter the current hour, whole number (0-23): ')
    # validate current hour is integer
    if not current_hour.isnumeric():
        # not valid, so display error message and exit
        print('Sorry, input current hour not in a valid format.')
        return
    # validate the current hour is in the valid range
    elif int(current_hour) < 0 or int(current_hour) > 23:
        # not valid, so display error message and exit
        print('Sorry, input hour is not in the 0-23 hour range.')
        return
    else:
        # convert to integer value for use with later calculations
        current_hour = int(current_hour)

    # ask user for input - number of hours
    number_of_hours = input('Please enter the number of hours you would like to add, whole number 0 or greater: ')
    if not number_of_hours.isnumeric():
        # not valid, so display error message and exit
        print('Sorry, number of hours not in a valid format')
        return
    else:
        # convert to integer value for use with later calculations
        number_of_hours = int(number_of_hours)

    # calculate the hour of the day for the alarm
    alarm_hour_of_day = (current_hour + number_of_hours) % 24

    # display results for user
    print('With a start time of {0} and an offset of {1}, the hour of the alarm will be {2}.'
          .format(current_hour, number_of_hours, alarm_hour_of_day))


main()