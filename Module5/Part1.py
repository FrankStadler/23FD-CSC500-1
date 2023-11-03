##############################################
# CSC-500 Module 5 - Part 1 Assignment
# Programmer - Frank Stadler
##############################################

import Utilities

def main():
    # prompt the user for the number of years of rainfall they would like to work with
    input_num_years = Utilities.get_and_validate_int('Please enter the number of years of rainfall you would like: ')
    # initialize total rainfall for use with data collection
    rainfall_total = 0

    # loop through once for each year entered above.
    for year_number in range(1, input_num_years + 1):
        # loop through once for each month to collect the monthly rainfall amount
        for month in range(1,13):
            # accept the rainfall amount from the user
            input_rainfall = Utilities.get_and_validate_float('Please enter rainfall amount for year {0} {1}: '
                                                              .format(year_number,Utilities.get_month_name_from_number(month)))
            # add rainfall amount to the total
            rainfall_total += input_rainfall

    # Write out summary info about rainfall.
    print('\nSummary Report')
    # Calculate and Display total number of months
    print('Number of Months: {0}'.format(input_num_years * 12))
    # Display the Total Rainfall displayed to two decimal places
    print('Total Inches of Rainfall: {0:.2f}'.format(rainfall_total))
    # Calculate and display the average rain per month displayed to two decimal places
    print('Average Rainfall Per Month: {0:.2f}'.format(rainfall_total / (input_num_years * 12)))


main()