# CSC500 - Module 7 Critical Thinking Assignment
# Robust Function Development
# Author: Nathan Hayes
# Date: June 2026
#
# This program works as a simple course information system.
# It uses three dictionaries to store room numbers, instructors,
# and meeting times based on a course number.


# This function creates the course data dictionaries.
# Each dictionary uses the course number as the key.
def create_course_data():
    # dictionary 1: course number -> room number
    room_numbers = {
        "CSC101": "3004",
        "CSC102": "4501",
        "CSC103": "6755",
        "NET110": "1244",
        "COM241": "1411"
    }

    # dictionary 2: course number -> instructor
    instructors = {
        "CSC101": "Haynes",
        "CSC102": "Alvarado",
        "CSC103": "Rich",
        "NET110": "Burke",
        "COM241": "Lee"
    }

    # dictionary 3: course number -> meeting time
    meeting_times = {
        "CSC101": "8:00 a.m.",
        "CSC102": "9:00 a.m.",
        "CSC103": "10:00 a.m.",
        "NET110": "11:00 a.m.",
        "COM241": "1:00 p.m."
    }

    return room_numbers, instructors, meeting_times


# This function looks up the course number entered by the user.
# If the course exists, it prints the room, instructor, and meeting time.
# If the course does not exist, it prints an error message instead of crashing.
def display_course_info(course_number, room_numbers, instructors, meeting_times):
    # check if the course exists before trying to print the information
    if course_number in room_numbers:
        print("\nCourse Information")
        print("------------------")
        print(f"Course Number: {course_number}")
        print(f"Room Number: {room_numbers[course_number]}")
        print(f"Instructor: {instructors[course_number]}")
        print(f"Meeting Time: {meeting_times[course_number]}")
    else:
        print("\nError: Course number not found.")
        print("Please enter a valid course number.")


# This is the main function.
# It starts the program, gets the user's course number,
# and sends that course number to the lookup function.
def main():
    room_numbers, instructors, meeting_times = create_course_data()

    print("=== Course Information System ===")
    print("Available courses: CSC101, CSC102, CSC103, NET110, COM241")

    # get the course number from the user
    course_number = input("\nEnter a course number: ").strip().upper()

    # look up and display the course information
    display_course_info(course_number, room_numbers, instructors, meeting_times)


# run the program
if __name__ == "__main__":
    main()