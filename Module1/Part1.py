##############################################
# CSC-500 Module 1 - Part 1 Assignment
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
    else:
        sum_result = float(num1) + float(num2)
        print(num1, "+", num2, "=", sum_result)
        subtraction_result = float(num1) - float(num2)
        print(num1, "-", num2, "=", subtraction_result)


main()
