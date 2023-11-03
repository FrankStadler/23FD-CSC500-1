##############################################
# CSC-500 Module 5 - Part 2 Assignment
# Programmer - Frank Stadler
##############################################

import Utilities

def main():
    # ask the user for the number of books purchased that month
    # the validation screens out negative numbers so I don't need to handle that case within the if statement below
    number_of_books = Utilities.get_and_validate_int('Please enter the number of books purchased this month: ')

    # assign points based on the number of books
    # 0 or 1 book is 0 points
    if number_of_books == 0 or number_of_books == 1:
        points_awarded = 0
    # 2 or 3 books is 5 points
    elif number_of_books == 2 or number_of_books == 3:
        points_awarded = 5
    # 4 or 5 books is 15 points
    elif number_of_books == 4 or number_of_books == 5:
        points_awarded = 15
    # 6 or 7 books is 30 points
    elif number_of_books == 6 or number_of_books == 7:
        points_awarded = 30
    # 8 or more books is 60 points
    elif number_of_books >= 8:
        points_awarded = 60

    # Display a summary line with the number of books purchased and the points awarded
    print('You purchased {0} books and were awarded {1} points. Congratulations'.format(number_of_books,points_awarded))


main()