from lib.student import Student
from lib.classroom import Classroom
from lib.report import Report

if __name__ == "__main__":
    students = list()
    for counter in range(2):
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        new_student = Student(f_name=first_name, l_name=last_name)
        students.append(new_student)
    r = Report()
    for student in students:
        student.set_scores()
        r.show_scores(student)

    c = Classroom(students=students)
    print(c.best_scores())
