import curses
import os
import zlib
from input import add_student, add_course, add_mark
from output import list_students, list_courses, show_student_marks
from domains.mark import Mark

class StudentMarkManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = Mark()
        self.load_data()

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

    def save_data(self):
        # Save students, courses, and marks in a structured format
        with open("students.txt", "w") as f:
            for student in self.students:
                f.write(f"{student.student_id},{student.name},{student.dob},{student.gpa}\n")
        
        with open("courses.txt", "w") as f:
            for course in self.courses:
                f.write(f"{course.course_id},{course.name},{course.credits}\n")
        
        with open("marks.txt", "w") as f:
            for course_id, student_marks in self.marks.marks.items():
                for student_id, mark in student_marks.items():
                    f.write(f"{course_id},{student_id},{mark}\n")

        # Compress all files into students.dat
        with open("students.txt", "rb") as f:
            students_data = f.read()
        with open("courses.txt", "rb") as f:
            courses_data = f.read()
        with open("marks.txt", "rb") as f:
            marks_data = f.read()
        
        compressed_data = zlib.compress(
            students_data + b"\n---\n" + courses_data + b"\n---\n" + marks_data
        )
        with open("students.dat", "wb") as f:
            f.write(compressed_data)

    def load_data(self):
        if os.path.exists("students.dat"):
            # Decompress students.dat
            with open("students.dat", "rb") as f:
                compressed_data = f.read()
            data = zlib.decompress(compressed_data)
            students_data, courses_data, marks_data = data.split(b"\n---\n")

            # Load students
            with open("students.txt", "wb") as f:
                f.write(students_data)
            for line in students_data.decode().splitlines():
                student_id, name, dob, gpa = line.split(",")
                student = Student(student_id, name, dob)
                student.gpa = float(gpa)
                self.students.append(student)

            # Load courses
            with open("courses.txt", "wb") as f:
                f.write(courses_data)
            for line in courses_data.decode().splitlines():
                course_id, name, credits = line.split(",")
                course = Course(course_id, name, int(credits))
                self.courses.append(course)

            # Load marks
            with open("marks.txt", "wb") as f:
                f.write(marks_data)
            for line in marks_data.decode().splitlines():
                course_id, student_id, mark = line.split(",")
                self.marks.add_mark(course_id, student_id, float(mark))

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
                list_students(stdscr, self.students, self.calculate_gpa)
            elif choice == '2':
                list_courses(stdscr, self.courses)
            elif choice == '3':
                stdscr.clear()
                stdscr.addstr("Enter the course ID to view marks: ")
                stdscr.refresh()
                course_id = stdscr.getstr().decode()
                show_student_marks(stdscr, self.students, self.marks, course_id)
            elif choice == '0':
                self.save_data()
                break
            else:
                stdscr.addstr("\nInvalid choice! Please try again.\n")
                stdscr.addstr("Press any key to return to the menu...")
                stdscr.refresh()
                stdscr.getkey()

def main(stdscr):
    smms = StudentMarkManagementSystem()

    # Add predefined students (only if not loaded from file)
    if not smms.students:
        add_student(smms.students, '22BI13384', 'Quang', '23/11/2004')
        add_student(smms.students, '22BI13174', 'Hoang', '16/12/2004')
        add_student(smms.students, '22BA13305', 'Trung', '21/03/2004')

    # Add predefined courses (only if not loaded from file)
    if not smms.courses:
        add_course(smms.courses, 'FR2.1', 'French 2.1', 3)
        add_course(smms.courses, 'ICT2.4', 'Signals & Systems', 4)

    # Add predefined marks (only if not loaded from file)
    if not smms.marks.marks:
        add_mark(smms.marks, 'FR2.1', '22BI13384', 12.7)
        add_mark(smms.marks, 'FR2.1', '22BI13174', 15.5)
        add_mark(smms.marks, 'FR2.1', '22BA13305', 14.2)
        add_mark(smms.marks, 'ICT2.4', '22BI13384', 10.3)
        add_mark(smms.marks, 'ICT2.4', '22BI13174', 14.8)
        add_mark(smms.marks, 'ICT2.4', '22BA13305', 17.9)

    smms.show_menu(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)
