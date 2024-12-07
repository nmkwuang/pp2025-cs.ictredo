# Student Mark Management System

# Predefined data
students = [
    {'id': '22BI13384', 'name': 'Quang', 'dob': '23/11/2004'},
    {'id': '22BI13174', 'name': 'Hoang', 'dob': '16/12/2004'},
    {'id': '22BA13305', 'name': 'Trung', 'dob': '21/03/2004'}
]

courses = [
    {'id': 'FR2.1', 'name': 'French 2.1'},
    {'id': 'ICT2.4', 'name': 'Signals & Systems'}
]

marks = {
    'FR2.1': {'22BI13384': 12, '22BI13174': 15, '22BA13305': 14},
    'ICT2.4': {'22BI13384': 10, '22BI13174': 14, '22BA13305': 17}
}

# Listing functions
def list_students():
    print("\nList of Students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

def list_courses():
    print("\nList of Courses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

def show_student_marks():
    course_id = input("\nEnter the course ID to view marks: ")
    if course_id not in marks:
        print("Invalid course ID!")
        return
    print(f"\nMarks for Course ID: {course_id}")
    for student_id, mark in marks[course_id].items():
        student_name = next(student['name'] for student in students if student['id'] == student_id)
        print(f"Student Name: {student_name}, ID: {student_id}, Mark: {mark}")

# Menu
def show_menu():
    while True:
        print("\nStudent Mark Management System")
        print("1. List all students")
        print("2. List all courses")
        print("3. Show student marks for a course")
        print("0. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            list_students()
        elif choice == '2':
            list_courses()
        elif choice == '3':
            show_student_marks()
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please try again.")

# Main program execution
if __name__ == "__main__":
    show_menu()