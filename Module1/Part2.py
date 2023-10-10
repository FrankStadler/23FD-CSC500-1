##############################################
# CSC-500 Module 1 - Part 2 Assignment
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
    num1 = input("Please enter a first number: ")
    num2 = input("Please enter a second number: ")

    if not is_number(num1):
        print("Hey, no funny business, first number doesn't look like a valid number.")
    elif not is_number(num2):
        print("Hey, no funny business, second number doesn't look like a valid number.")
    elif float(num2) == 0:
        print("Second number can't be zero, divide by zero is not permitted.")
    else:
        multiplication_result = float(num1) * float(num2)
        print(num1, "*", num2, "=", multiplication_result)
        division_result = float(num1) / float(num2)
        print(num1, "/", num2, "=", division_result)


main()
