##############################################
# CSC-500 Module 3 - Part 1 Assignment
# Programmer - Frank Stadler
##############################################

# built-in isnumeric only validates integers. I want to allow for float values
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def main():
    # ask user to input food charge
    food_charge = input('Please enter total food charge: $ ')
    # let's validate input to make sure it is a number.
    if not is_number(food_charge):
        # display error message to user and exit if we have bad data
        print('Sorry, the value you provided doesn\'t look like a valid number.\n')
        return
    else:
        # we have a valid number, let's convert the string to a float for use with the later calculations
        food_charge = float(food_charge)

    # calculate tip
    tip_amount = food_charge * .18

    # calculate sales tax
    tax_amount = food_charge * .07

    # calculate total
    total_amount = food_charge + tip_amount + tax_amount

    # display each line item to the user
    # display food charge formatted to two decimal places
    print('Food charge is :            ${:.2f}'.format(food_charge))
    # display tip charge formatted to two decimal places
    print('Tip amount at 18% is :      ${:.2f}'.format(tip_amount))
    # display sales tax amount formatted to two decimal places
    print('Sales tax amount at 7% is : ${:.2f}'.format(tax_amount))
    # display total amount formatted to two decimal places
    print('Grand total is :            ${:.2f}'.format(total_amount))


main()
