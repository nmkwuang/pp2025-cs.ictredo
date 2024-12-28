import zlib
import pickle

# Load the compressed file
with open("students.dat", "rb") as f:
    compressed_data = f.read()

# Decompress the data
decompressed_data = zlib.decompress(compressed_data)

# Deserialize the data using pickle
data = pickle.loads(decompressed_data)

# Access and print the data
students = data["students"]
courses = data["courses"]
marks = data["marks"]

print("Students:")
for student in students:
    print(f"ID: {student.student_id}, Name: {student.name}, DoB: {student.dob}, GPA: {student.gpa:.2f}")

print("\nCourses:")
for course in courses:
    print(f"ID: {course.course_id}, Name: {course.name}, Credits: {course.credits}")

print("\nMarks:")
for course_id, student_marks in marks.items():
    print(f"Course ID: {course_id}")
    for student_id, mark in student_marks.items():
        print(f"  Student ID: {student_id}, Mark: {mark}")
