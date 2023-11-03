
import datetime
# A reusable method which prompts the user for an integer input with the supplied prompt
# and repeats until the user enters a conforming value
def get_and_validate_int(prompt):
    input_value = input(prompt)
    while not input_value.isnumeric():
        print('Sorry, invalid value, please try again.')
        input_value = input(prompt)
    return int(input_value)


# A reusable method which prompts the user for a float input with the supplied prompt
# and repeats until the user enters a conforming value
def get_and_validate_float(prompt):
    input_value = input(prompt)
    while not is_float(input_value) or float(input_value) <= 0:
        print('Sorry, invalid value, please try again.')
        input_value = input(prompt)
    return float(input_value)


# A reusable function to validate that the given value is a valid float
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# A reusable function that takes in the month number as an integer and returns the corresponding month name
def get_month_name_from_number(month_number):
    datetime_object = datetime.datetime.strptime(str(month_number), "%m")

    return datetime_object.strftime("%B")