class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def calculate_gpa(self):
        total_points = sum(self.grades.values())
        num_subjects = len(self.grades)
        if num_subjects == 0:
            return 0
        return total_points / num_subjects

    def calculate_overall_grade(self):
        gpa = self.calculate_gpa()
        if gpa >= 90:
            return 'A'
        elif gpa >= 80:
            return 'B'
        elif gpa >= 70:
            return 'C'
        elif gpa >= 60:
            return 'D'
        else:
            return 'F'

# Example usage:
student_name = input("Enter student's name: ")
student = Student(student_name)

num_subjects = int(input("Enter the number of subjects: "))

for _ in range(num_subjects):
    subject = input("Enter subject name: ")
    grade = float(input("Enter grade (0-100): "))
    student.add_grade(subject, grade)

print("\n--- Academic Performance ---")
print(f"Student: {student.name}")
print("Grades:")
for subject, grade in student.grades.items():
    print(f"{subject}: {grade}")
print(f"GPA: {student.calculate_gpa():.2f}")
print(f"Overall Grade: {student.calculate_overall_grade()}")
