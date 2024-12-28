import tkinter as tk
from tkinter import messagebox
from input import add_student, add_course, add_mark
from output import list_students, list_courses, show_student_marks
from domains.student import Student
from domains.course import Course
from domains.mark import Mark


class StudentMarkManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = Mark()

        # Load data from file
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
        import zlib
        import pickle

        # Combine all data into a dictionary
        data = {
            "students": self.students,
            "courses": self.courses,
            "marks": self.marks.marks,
        }

        # Serialize and compress data
        compressed_data = zlib.compress(pickle.dumps(data))

        # Save to a binary file
        with open("students.dat", "wb") as f:
            f.write(compressed_data)

    def load_data(self):
        import os
        import zlib
        import pickle

        if os.path.exists("students.dat"):
            # Load and decompress data
            with open("students.dat", "rb") as f:
                compressed_data = f.read()
            data = pickle.loads(zlib.decompress(compressed_data))

            # Load students, courses, and marks
            self.students = data["students"]
            self.courses = data["courses"]
            self.marks.marks = data["marks"]

    def run(self):
        # Create the main window
        root = tk.Tk()
        root.title("Student Mark Management System")

        # Define GUI elements
        def list_students_gui():
            self.calculate_gpa()
            students_sorted = sorted(self.students, key=lambda s: s.gpa, reverse=True)
            output = "\n".join(
                f"ID: {s.student_id}, Name: {s.name}, DoB: {s.dob}, GPA: {s.gpa:.2f}" for s in students_sorted
            )
            messagebox.showinfo("List of Students", output)

        def list_courses_gui():
            output = "\n".join(f"ID: {c.course_id}, Name: {c.name}, Credits: {c.credits}" for c in self.courses)
            messagebox.showinfo("List of Courses", output)

        def show_marks_gui():
            def submit_course_id():
                course_id = course_id_entry.get()
                course_marks = self.marks.get_marks_by_course(course_id)
                if not course_marks:
                    messagebox.showerror("Error", "Invalid course ID or no marks available!")
                    return
                output = f"Marks for Course ID: {course_id}\n"
                for student_id, mark in course_marks.items():
                    student_name = next(
                        (student.name for student in self.students if student.student_id == student_id), "Unknown"
                    )
                    output += f"Student Name: {student_name}, ID: {student_id}, Mark: {mark}\n"
                messagebox.showinfo(f"Marks for {course_id}", output)
                course_id_window.destroy()

            course_id_window = tk.Toplevel(root)
            course_id_window.title("Enter Course ID")
            tk.Label(course_id_window, text="Course ID:").pack()
            course_id_entry = tk.Entry(course_id_window)
            course_id_entry.pack()
            tk.Button(course_id_window, text="Submit", command=submit_course_id).pack()

        def exit_program():
            self.save_data()
            root.destroy()

        # Add buttons to the main window
        tk.Button(root, text="List Students", command=list_students_gui).pack(fill=tk.X)
        tk.Button(root, text="List Courses", command=list_courses_gui).pack(fill=tk.X)
        tk.Button(root, text="Show Marks for a Course", command=show_marks_gui).pack(fill=tk.X)
        tk.Button(root, text="Exit", command=exit_program).pack(fill=tk.X)

        # Start the GUI event loop
        root.mainloop()


if __name__ == "__main__":
    smms = StudentMarkManagementSystem()

    # Add predefined students (only if not loaded from file)
    if not smms.students:
        add_student(smms.students, "22BI13384", "Quang", "23/11/2004")
        add_student(smms.students, "22BI13174", "Hoang", "16/12/2004")
        add_student(smms.students, "22BA13305", "Trung", "21/03/2004")

    # Add predefined courses (only if not loaded from file)
    if not smms.courses:
        add_course(smms.courses, "FR2.1", "French 2.1", 3)
        add_course(smms.courses, "ICT2.4", "Signals & Systems", 4)

    # Add predefined marks (only if not loaded from file)
    if not smms.marks.marks:
        add_mark(smms.marks, "FR2.1", "22BI13384", 12.7)
        add_mark(smms.marks, "FR2.1", "22BI13174", 15.5)
        add_mark(smms.marks, "FR2.1", "22BA13305", 14.2)
        add_mark(smms.marks, "ICT2.4", "22BI13384", 10.3)
        add_mark(smms.marks, "ICT2.4", "22BI13174", 14.8)
        add_mark(smms.marks, "ICT2.4", "22BA13305", 17.9)

    smms.run()
