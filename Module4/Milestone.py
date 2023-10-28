##############################################
# CSC-500 Module 4 - Milestone Assignment
# Programmer - Frank Stadler
##############################################

import Utilities

# Define class ItemToPurchase
class ItemToPurchase:
    # Class Attributes
    item_name = ''
    item_price = 0.0
    item_quantity = 0

    # Class Constructor
    def __init__(self):
        # Sets initial values for newly instantiated object per our specs
        self.item_name = 'none'
        self.item_price = 0.0
        self.item_quantity = 0

    # Method which prints out the current object's values formatted appropriately
    def print_item_cost(self):
        print('{0} {1} @ ${2:.2f} = ${3:.2f}'.format(self.item_name, self.item_quantity, self.item_price,
                                                     self.item_quantity * self.item_price ))


def main():
    # instantiate first_item and second_item objects to hold the data
    first_item = ItemToPurchase()
    second_item = ItemToPurchase()

    print('   Item 1')
    # prompt user for first item name
    first_item.item_name = input('Enter the item name: ')
    # prompt user for first item price
    first_item.item_price = Utilities.get_and_validate_float('Enter the item price: ')
    # prompt user for first item quantity
    first_item.item_quantity = Utilities.get_and_validate_int('Enter the item quantity: ')
    print()

    print('   Item 2')
    # prompt user for second item name
    second_item.item_name = input('Enter the item name: ')
    # prompt user for second item price
    second_item.item_price = Utilities.get_and_validate_float('Enter the item price: ')
    # prompt user for second item quantity
    second_item.item_quantity = Utilities.get_and_validate_int('Enter the item quantity: ')

    # display the total cost of the two items together
    print('\n TOTAL COST\n')
    # display first item summary line
    first_item.print_item_cost()
    # display second item summary line
    second_item.print_item_cost()
    print()
    # format and display the grand total line
    print('Total: $ {:.2f}'.format(first_item.item_price * first_item.item_quantity +
                                   second_item.item_price * second_item.item_quantity))


main()