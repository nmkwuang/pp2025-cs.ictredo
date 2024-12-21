import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.gpa = 0.0  # To store the student's GPA

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}, GPA: {self.gpa:.1f}"


class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits

    def __str__(self):
        return f"ID: {self.course_id}, Name: {self.name}, Credits: {self.credits}"


class Mark:
    def __init__(self):
        self.marks = {}

    def add_mark(self, course_id, student_id, mark):
        rounded_mark = math.floor(mark * 10) / 10  # Round down to 1 decimal place
        if course_id not in self.marks:
            self.marks[course_id] = {}
        self.marks[course_id][student_id] = rounded_mark

    def get_marks_by_course(self, course_id):
        return self.marks.get(course_id, {})


class StudentMarkManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = Mark()

    def add_student(self, student_id, name, dob):
        self.students.append(Student(student_id, name, dob))

    def add_course(self, course_id, name, credits):
        self.courses.append(Course(course_id, name, credits))

    def add_mark(self, course_id, student_id, mark):
        self.marks.add_mark(course_id, student_id, mark)

    def calculate_gpa(self):
        for student in self.students:
            total_credits = 0
            total_weighted_marks = 0
            for course in self.courses:
                course_marks = self.marks.get_marks_by_course(course.course_id)
                if student.student_id in course_marks:
                    total_weighted_marks += course_marks[student.student_id] * course.credits
                    total_credits += course.credits
            if total_credits > 0:
                student.gpa = total_weighted_marks / total_credits

    def list_students(self, stdscr):
        self.calculate_gpa()
        self.students.sort(key=lambda s: s.gpa, reverse=True)
        stdscr.clear()
        stdscr.addstr("List of Students:\n")
        for student in self.students:
            stdscr.addstr(f"{student}\n")
        stdscr.addstr("\nPress any key to return to the menu...")
        stdscr.refresh()
        stdscr.getkey()

    def list_courses(self, stdscr):
        stdscr.clear()
        stdscr.addstr("List of Courses:\n")
        for course in self.courses:
            stdscr.addstr(f"{course}\n")
        stdscr.addstr("\nPress any key to return to the menu...")
        stdscr.refresh()
        stdscr.getkey()

    def show_student_marks(self, stdscr):
        stdscr.clear()
        stdscr.addstr("Enter the course ID to view marks: ")
        stdscr.refresh()
        course_id = stdscr.getstr().decode()
        stdscr.clear()
        course_marks = self.marks.get_marks_by_course(course_id)
        if not course_marks:
            stdscr.addstr("Invalid course ID or no marks available!\n")
        else:
            stdscr.addstr(f"Marks for Course ID: {course_id}\n")
            for student_id, mark in course_marks.items():
                student_name = next((student.name for student in self.students if student.student_id == student_id), "Unknown")
                stdscr.addstr(f"Student Name: {student_name}, ID: {student_id}, Mark: {mark}\n")
        stdscr.addstr("\nPress any key to return to the menu...")
        stdscr.refresh()
        stdscr.getkey()

    def show_menu(self, stdscr):
        while True:
            stdscr.clear()
            stdscr.addstr("Student Mark Management System\n")
            stdscr.addstr("1. List all students\n")
            stdscr.addstr("2. List all courses\n")
            stdscr.addstr("3. Show student marks for a course\n")
            stdscr.addstr("0. Exit\n")
            stdscr.addstr("Select an option: ")
            stdscr.refresh()
            choice = stdscr.getkey()

            if choice == '1':
                self.list_students(stdscr)
            elif choice == '2':
                self.list_courses(stdscr)
            elif choice == '3':
                self.show_student_marks(stdscr)
            elif choice == '0':
                break
            else:
                stdscr.addstr("\nInvalid choice! Please try again.\n")
                stdscr.addstr("Press any key to return to the menu...")
                stdscr.refresh()
                stdscr.getkey()


# Main program execution
def main(stdscr):
    # Initialize the system and populate it with predefined data
    smms = StudentMarkManagementSystem()

    # Add predefined students
    smms.add_student('22BI13384', 'Quang', '23/11/2004')
    smms.add_student('22BI13174', 'Hoang', '16/12/2004')
    smms.add_student('22BA13305', 'Trung', '21/03/2004')

    # Add predefined courses
    smms.add_course('FR2.1', 'French 2.1', 3)
    smms.add_course('ICT2.4', 'Signals & Systems', 4)

    # Add predefined marks
    smms.add_mark('FR2.1', '22BI13384', 12.7)
    smms.add_mark('FR2.1', '22BI13174', 15.5)
    smms.add_mark('FR2.1', '22BA13305', 14.2)
    smms.add_mark('ICT2.4', '22BI13384', 10.3)
    smms.add_mark('ICT2.4', '22BI13174', 14.8)
    smms.add_mark('ICT2.4', '22BA13305', 17.9)

    # Show the menu
    smms.show_menu(stdscr)


if __name__ == "__main__":
    curses.wrapper(main)
