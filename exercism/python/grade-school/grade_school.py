from collections import defaultdict

class School:
    def __init__(self):
        self.yearbook = defaultdict(list)

    def add_student(self, name, grade):
        self.yearbook[grade] += [name]

    def roster(self):
        pass

    def grade(self, grade_number):
        pass
