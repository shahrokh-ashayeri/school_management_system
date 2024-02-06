from lib.student import Student
from lib.classroom import Classroom

if __name__ == "__main__":
    students = list()
    for counter in range(2):
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        new_student = Student(f_name=first_name, l_name=last_name)
        students.append(new_student)

    for student in students:
        student.set_scores()
        student.show()

    print(c.best_scores())
