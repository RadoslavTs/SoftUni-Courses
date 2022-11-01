class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []
        self.total_students = 0

    def add_student(self, name:str, grade:float):
        if self.total_students < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        total_grade_sum = 0
        for sequence in self.grades:
            total_grade_sum += float(sequence)
        average_grade = total_grade_sum / len(self.grades)
        return average_grade

    def __repr__(self):
        student_string = ", ".join(self.students)
        return f"The students in {self.name}: {student_string}. Average grade: {Class.get_average_grade(self):.2f}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)



