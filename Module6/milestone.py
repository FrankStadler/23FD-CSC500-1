##############################################
# CSC-500 Module 6 - Milestone Assignment
# Programmer - Frank Stadler
##############################################

import utilities
import datetime

# Define class ItemToPurchase
class ItemToPurchase:

    # Class Constructor
    def __init__(self):
        # Sets initial values for newly instantiated object per our specs
        self.item_name = 'none'
        self.item_price = 0.0
        self.item_quantity = 0
        self.item_description = ''

    # Method which prints out the current object's values formatted appropriately
    def print_item_cost(self):
        print('{0} {1} @ ${2:.2f} = ${3:.2f}'.format(self.item_name, self.item_quantity, self.item_price,
                                                     self.item_quantity * self.item_price ))


# Defines class ShoppingCart
class ShoppingCart:
    # parameterized class constructor
    def __init__(self, customer_name = 'none', current_date = 'January 1, 2020'):
        # Sets initial values for newly instantiated object per our specs
        # set customer name attribute of object to the name passed in to the constructor as a parameter
        self.customer_name = customer_name
        # set current date attribute of object to be the date passed in to the constructor as a parameter
        self.current_date = current_date
        # cart items as a list
        self.cart_items = []

    # methods for ShoppingCart class

    # Method Name: add_item
    # Parameters: ItemToPurchase of ItemToPurchase class
    # Description: takes in the ItemToPurchase as a parameter and  adds it to the cart_items list
    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
        return

    # Method Name: remove_item
    # Parameters: item_name_to_remove  (string)
    # Description: takes in the name of the item to remove, searches shopping cart and removes the first matching item
    # based on item_name
    def remove_item(self, item_name_to_remove):
        item_found = False
        # loop through the cart item list
        for i in range(len(self.cart_items)):
            # if we find a matching item based on name, remove it
            if self.cart_items[i].item_name == item_name_to_remove:
                self.cart_items.pop(i)
                # set variable to indicate we found a matching record
                item_found = True
                # exit for loop
                break
                # since we're stopping at the first item found we don't have the consideration
                # of iterating over a list where we deleted items.
        if not item_found:
            # output a descriptive message if the item passed in is not found
            print('Item not found in cart.Nothing removed.')
        return

    # Method Name: modify_item
    # Parameters: ItemToPurchase (class)
    # Description: takes in the ItemToPurchase object with the updated values
    # matches based on item_name.
    # will update item's description, price and quantity
    def modify_item(self, ItemToPurchase):
        item_found = False
        # loop through the cart item list
        for i in range(len(self.cart_items)):
            # if we find a matching item based on name we may be able to modify it
            if self.cart_items[i].item_name == item_name_to_remove:
                item_found = True
                # check to see if the passed in object has default values.
                if not (ItemToPurchase.item_description == '' and ItemToPurchase.item_price == 0.0 and ItemToPurchase.item_quantity == 0):
                    self.cart_items[i].item_description = ItemToPurchase.item_description
                    self.cart_items[i].item_price = ItemToPurchase.item_price
                    self.cart_items[i].item_quantity = ItemToPurchase.item_quantity
                # exit for loop
                break
        if not item_found:
            # output a descriptive message if the item passed in is not found
            print('Nothing modified.')
        return

    # Method Name: get_num_items_in_cart
    # Parameters: None
    # Description: loops through each item in the cart_items list
    # and provides the sum of each item's item_quantity field
    def get_num_items_in_cart(self):
        # initialize quantity to 0
        total_item_quantity = 0
        # loop through each item in the cart
        for item in self.cart_items:
            # add each item's quantity field to the total quantity
            total_item_quantity += item.item_quantity

        return total_item_quantity

    # Method Name: get_cost_of_cart
    # Parameters: None
    # Description: Provides aggregate total of the cost of each item in the cart_items list
    # cost is item price times item quantity.
    def get_cost_of_cart(self):
        # initialize quantity to 0
        total_item_cost = 0.0
        # loop through each item in the cart
        for item in self.cart_items:
            # add each item's quantity field to the total quantity
            total_item_cost += (item.item_quantity * item.item_price)

        return total_item_cost

    # Method Name: print_descriptions
    # Method Parameters: None
    # Description: Provides formatted output for each item in the cart_items list of item name and description
    def print_description(self):
        print('{0}\'s Shopping Cart - {1}'.format(self.customer_name, self.current_date))
        print('Item Descriptions')
        for item in self.cart_items:
            # Display a formatted line for each item in the cart.
            print('{0}: {1}'.format(item.item_name, item.item_description))
        return

    # Method Name: print_total
    # Parameters: None
    # Description: Provides formatted output detailing every item in cart_items
    def print_total(self):
        print('{0}\'s Shopping Cart - {1}'.format(self.customer_name, self.current_date))
        num_items = self.get_num_items_in_cart()
        # if there are no items in the shopping cart, output a message for the user
        # if somehow we have only items with quantity 0, I am counting that as an empty cart as well
        # most shopping systems would have validation to prevent you from keeping a 0 quantity item in your cart
        if num_items == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('Number of Items: {0}'.format(num_items))
            for item in self.cart_items:
                # Display a formatted line for each item in the cart.
                print('{0} {1} @ ${2:.2f} = ${3:.2f}'.format(item.item_name, item.item_quantity, item.item_price, item.item_quantity * item.item_price))
            # display the overall total for the cart
            print('Total: ${0:.2f}'.format(self.get_cost_of_cart()))
        return


# Method: print_menu
# Parameters: ShoppingCart object
# Description: Displays a menu for the user to select one option at a time.
# validates user input and calls the ShoppingCart code for each respective menu item
def print_menu(ShoppingCart):

    # initialize input value for initial execution
    input_value = ''
    # continue until the user selects the quit option
    # We're taking the input value and converting to lower case
    # so that we can accept upper case equivalents as well
    while input_value.lower() != 'q':
        # print descriptions for each item in the shopping cart
        if input_value.lower() == 'i':
            print('\nOUTPUT ITEMS\' DESCRIPTIONS')
            ShoppingCart.print_description()
            print()
        # user selected the shopping cart list total
        elif input_value.lower() == 'o':
            print('\nOUTPUT SHOPPING CART')
            ShoppingCart.print_total()
            print()
        elif input_value != '':
            print('\nSorry, input not recognized. Please try again. \n')
        # output the menu
        # the user will select from one of these items.
        print('MENU')
        print('a - Add item to cart (not implemented for this milestone)')
        print('r - Remove item from cart (not implemented for this milestone)')
        print('c - Change item quantity (not implemented for this milestone)')
        print('i - Output items\' descriptions')
        print('o - Output shopping cart')
        print('q - Quit')
        print('Choose an option:')
        input_value = input()
    return

def main():
    # instantiate first_item and second_item objects to hold the data
    first_item = ItemToPurchase()
    second_item = ItemToPurchase()

    print('   Item 1')
    # prompt user for first item name
    first_item.item_name = input('Enter the item name: ')
    # prompt user for first item description
    first_item.item_description = input('Enter the item description: ')
    # prompt user for first item price
    first_item.item_price = utilities.get_and_validate_float('Enter the item price: ')
    # prompt user for first item quantity
    first_item.item_quantity = utilities.get_and_validate_int('Enter the item quantity: ')
    print()

    print('   Item 2')
    # prompt user for second item name
    second_item.item_name = input('Enter the item name: ')
    # prompt user for second item description
    second_item.item_description = input('Enter the item description: ')
    # prompt user for second item price
    second_item.item_price = utilities.get_and_validate_float('Enter the item price: ')
    # prompt user for second item quantity
    second_item.item_quantity = utilities.get_and_validate_int('Enter the item quantity: ')

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

    # Week 6 milestone
    # declare shopping cart
    # add the two items previously entered to start us out
    shopping_cart = ShoppingCart('Valued Customer', datetime.date.today().strftime("%B %d, %Y"))
    shopping_cart.add_item(first_item)
    shopping_cart.add_item(second_item)
    print_menu(shopping_cart)


main()