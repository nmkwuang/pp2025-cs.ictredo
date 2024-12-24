from domains.student import Student
from domains.course import Course

def add_student(students, student_id, name, dob):
    students.append(Student(student_id, name, dob))

def add_course(courses, course_id, name, credits):
    courses.append(Course(course_id, name, credits))

def add_mark(marks, course_id, student_id, mark):
    marks.add_mark(course_id, student_id, mark)
