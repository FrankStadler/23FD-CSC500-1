##############################################
# CSC-500 Module 7 - Assignment
# Programmer - Frank Stadler
##############################################

# Method: Validate_course_number
# Parameters: course_key (string), course_room_number_dict (dictionary),
# course_instructor_dict (dictionary, course_time_dict (dictionary)
# Description: takes in the name of the course, validates it is found in all 3 dictionaries
# returns true if found in all 3
def validate_course_number(course_key, course_room_number_dict, course_instructor_dict, course_time_dict):
    ''' takes in a key and 3 dictionaries. returns true if key found in all 3'''
    valid_course_number = False
    # make sure key is found in all three dictionaries
    if course_key in course_room_number_dict and course_key in course_instructor_dict and course_key in course_time_dict:
        valid_course_number = True
    return valid_course_number

def main():
    # initialize starting dictionaries

    # dictionary which associates a course name key with a room number value
    course_room_number_dict = {'CSC101':'3004', 'CSC102':'4501', 'CSC103':'6755',
                        'NET110':'1244', 'COM241':'1411'}
    # dictionary which associates a course name key with an instructor name value
    course_instructor_dict = {'CSC101':'Haynes', 'CSC102':'Alvarado', 'CSC103':'Rich',
                        'NET110':'Burke', 'COM241':'Lee'}
    # dictionary which associates a course name key with a start time value
    course_time_dict = {'CSC101':'8:00 a.m.', 'CSC102':'9:00 a.m.', 'CSC103':'10:00 a.m.',
                        'NET110':'11:00 a.m.', 'COM241':'1:00 p.m.'}
    # prompt user to select a course number
    input_course_number = input('Please enter a course number to look up: ').upper()

    # validate the course number entered by the user, continue to prompt until a value course is entered
    # lower case versions of course numbers are accepted
    while validate_course_number(input_course_number, course_room_number_dict, course_instructor_dict,
                                 course_time_dict) == False:
        print('Sorry, course you entered is not found, please try again.\n')
        input_course_number = input('Please enter a course number to look up: ').upper()

    # Display course name
    print('\nCourse: {}'.format(input_course_number))
    # Display room value found in the room dictionary
    print('Room: {}'.format(course_room_number_dict[input_course_number]))
    # Display instructor found in the instructor dictionary
    print('Instructor: {}'.format(course_instructor_dict[input_course_number]))
    # Display course time found in the course time dictionary
    print('Course Time: {}'.format(course_time_dict[input_course_number]))
    print()

main()