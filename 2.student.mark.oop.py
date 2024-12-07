# OOP-based Student Mark Management System

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}"


class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

    def __str__(self):
        return f"ID: {self.course_id}, Name: {self.name}"


class Mark:
    def __init__(self):
        self.marks = {}

    def add_mark(self, course_id, student_id, mark):
        if course_id not in self.marks:
            self.marks[course_id] = {}
        self.marks[course_id][student_id] = mark

    def get_marks_by_course(self, course_id):
        return self.marks.get(course_id, {})


class StudentMarkManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = Mark()

    def add_student(self, student_id, name, dob):
        self.students.append(Student(student_id, name, dob))

    def add_course(self, course_id, name):
        self.courses.append(Course(course_id, name))

    def add_mark(self, course_id, student_id, mark):
        self.marks.add_mark(course_id, student_id, mark)

    def list_students(self):
        print("\nList of Students:")
        for student in self.students:
            print(student)

    def list_courses(self):
        print("\nList of Courses:")
        for course in self.courses:
            print(course)

    def show_student_marks(self):
        course_id = input("\nEnter the course ID to view marks: ")
        course_marks = self.marks.get_marks_by_course(course_id)
        if not course_marks:
            print("Invalid course ID or no marks available!")
            return
        
        print(f"\nMarks for Course ID: {course_id}")
        for student_id, mark in course_marks.items():
            student_name = next((student.name for student in self.students if student.student_id == student_id), "Unknown")
            print(f"Student Name: {student_name}, ID: {student_id}, Mark: {mark}")

    def show_menu(self):
        while True:
            print("\nStudent Mark Management System")
            print("1. List all students")
            print("2. List all courses")
            print("3. Show student marks for a course")
            print("0. Exit")
            choice = input("Select an option: ")

            if choice == '1':
                self.list_students()
            elif choice == '2':
                self.list_courses()
            elif choice == '3':
                self.show_student_marks()
            elif choice == '0':
                print("Exiting program.")
                break
            else:
                print("Invalid choice! Please try again.")


# Main program execution
if __name__ == "__main__":
    # Initialize the system and populate it with predefined data
    smms = StudentMarkManagementSystem()

    # Add predefined students
    smms.add_student('22BI13384', 'Quang', '23/11/2004')
    smms.add_student('22BI13174', 'Hoang', '16/12/2004')
    smms.add_student('22BA13305', 'Trung', '21/03/2004')

    # Add predefined courses
    smms.add_course('FR2.1', 'French 2.1')
    smms.add_course('ICT2.4', 'Signals & Systems')

    # Add predefined marks
    smms.add_mark('FR2.1', '22BI13384', 12)
    smms.add_mark('FR2.1', '22BI13174', 15)
    smms.add_mark('FR2.1', '22BA13305', 14)
    smms.add_mark('ICT2.4', '22BI13384', 10)
    smms.add_mark('ICT2.4', '22BI13174', 14)
    smms.add_mark('ICT2.4', '22BA13305', 17)

    # Show the menu
    smms.show_menu()