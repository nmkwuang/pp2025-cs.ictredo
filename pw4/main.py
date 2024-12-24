import curses
from input import add_student, add_course, add_mark
from output import list_students, list_courses, show_student_marks
from domains.mark import Mark

class StudentMarkManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = Mark()

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
                # Pass self.calculate_gpa correctly to list_students
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
                break
            else:
                stdscr.addstr("\nInvalid choice! Please try again.\n")
                stdscr.addstr("Press any key to return to the menu...")
                stdscr.refresh()
                stdscr.getkey()

def main(stdscr):
    smms = StudentMarkManagementSystem()

    # Add predefined students
    add_student(smms.students, '22BI13384', 'Quang', '23/11/2004')
    add_student(smms.students, '22BI13174', 'Hoang', '16/12/2004')
    add_student(smms.students, '22BA13305', 'Trung', '21/03/2004')

    # Add predefined courses
    add_course(smms.courses, 'FR2.1', 'French 2.1', 3)
    add_course(smms.courses, 'ICT2.4', 'Signals & Systems', 4)

    # Add predefined marks
    add_mark(smms.marks, 'FR2.1', '22BI13384', 12.7)
    add_mark(smms.marks, 'FR2.1', '22BI13174', 15.5)
    add_mark(smms.marks, 'FR2.1', '22BA13305', 14.2)
    add_mark(smms.marks, 'ICT2.4', '22BI13384', 10.3)
    add_mark(smms.marks, 'ICT2.4', '22BI13174', 14.8)
    add_mark(smms.marks, 'ICT2.4', '22BA13305', 17.9)

    smms.show_menu(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)
