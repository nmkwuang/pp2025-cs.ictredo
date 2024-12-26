import math

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
