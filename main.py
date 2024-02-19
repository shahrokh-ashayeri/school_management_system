from lib.student import Student
from lib.classroom import Classroom
from lib.report import Report
from lib.file_op import FileOperation

if __name__ == "__main__":
    students = list()
    for counter in range(2):
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        field = input("Field: ")
        grade = input("Grade: ")
        new_student = Student(
            f_name=first_name, l_name=last_name, field=field, grade=grade
        )
        students.append(new_student)
    r = Report()
    for student in students:
        student.set_scores()
        r.show_scores(student)

    field_of_study = input("Field of study for classroom: ")
    grade = input("Grade of classroom: ")
    c = Classroom(students=students, field_of_study=field_of_study, grade=grade)
    print(c.best_scores())
