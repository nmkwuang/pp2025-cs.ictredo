def list_students(stdscr, students, calculate_gpa):
    calculate_gpa()  # Correct context is now passed
    students.sort(key=lambda s: s.gpa, reverse=True)
    stdscr.clear()
    stdscr.addstr("List of Students:\n")
    for student in students:
        stdscr.addstr(f"{student}\n")
    stdscr.addstr("\nPress any key to return to the menu...")
    stdscr.refresh()
    stdscr.getkey()

def list_courses(stdscr, courses):
    stdscr.clear()
    stdscr.addstr("List of Courses:\n")
    for course in courses:
        stdscr.addstr(f"{course}\n")
    stdscr.addstr("\nPress any key to return to the menu...")
    stdscr.refresh()
    stdscr.getkey()

def show_student_marks(stdscr, students, marks, course_id):
    stdscr.clear()
    course_marks = marks.get_marks_by_course(course_id)
    if not course_marks:
        stdscr.addstr("Invalid course ID or no marks available!\n")
    else:
        stdscr.addstr(f"Marks for Course ID: {course_id}\n")
        for student_id, mark in course_marks.items():
            student_name = next((student.name for student in students if student.student_id == student_id), "Unknown")
            stdscr.addstr(f"Student Name: {student_name}, ID: {student_id}, Mark: {mark}\n")
    stdscr.addstr("\nPress any key to return to the menu...")
    stdscr.refresh()
    stdscr.getkey()
