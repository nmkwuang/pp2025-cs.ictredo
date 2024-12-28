from domains.student import Student
from domains.course import Course

def save_to_file(filename, data):
    with open(filename, "w") as f:
        f.write(data)

def add_student(students, student_id, name, dob):
    student = Student(student_id, name, dob)
    students.append(student)
    # Save to file in CSV format: "student_id,name,dob,gpa"
    save_to_file("students.txt", "\n".join(f"{s.student_id},{s.name},{s.dob},{s.gpa}" for s in students))

def add_course(courses, course_id, name, credits):
    course = Course(course_id, name, credits)
    courses.append(course)
    # Save to file
    save_to_file("courses.txt", "\n".join(str(c) for c in courses))

def add_mark(marks, course_id, student_id, mark):
    marks.add_mark(course_id, student_id, mark)
    # Save to file
    with open("marks.txt", "w") as f:
        for course, student_marks in marks.marks.items():
            for student, mark in student_marks.items():
                f.write(f"{course},{student},{mark}\n")
