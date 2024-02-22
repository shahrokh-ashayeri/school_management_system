from .file_op import FileOperation
import time
from .report import Report


class Student:
    def __init__(self, id, f_name, l_name, field, grade) -> None:
        self.courses = [
            "Math",
            "IS and web development",
            "Basic Technichal Knowledge",
            "Human and environment ",
            "Arabic Language",
        ]

        self.id = id
        self.first_name = f_name
        self.last_name = l_name
        self.field = field
        self.grade = grade

    def set_scores(self):
        print(f"{self.last_name}, {self.first_name}".center(50, "-"))
        scores = dict()
        for course in self.courses:
            score = float(input(f"{course}: "))
            scores[course] = score
        self.scores = scores
        FileOperation().write(scores)

    def get_transcript(self):
        output = dict()
        output["first_name"] = self.first_name
        output["last_name"] = self.last_name
        output["scores"] = dict()

        for course, score in self.scores.items():
            output["scores"][course] = score

        self.transcript = output

        return self.transcript

    @classmethod
    def set_private_attr(self):
        id = int(time.time())
        first_name = input("Students firstname: ")
        last_name = input("Students lastname: ")
        field = input("Students education field: ")
        grade = input("Studnets grade: ")

        return Student(
            id=id, f_name=first_name, l_name=last_name, field=field, grade=grade
        )

    def get_private_attr(self):
        data = dict()
        data["id"] = self.id
        data["first_name"] = self.first_name
        data["last_name"] = self.last_name
        data["field"] = self.field
        data["grade"] = self.grade
        return data

    @staticmethod
    def get_all():
        f = FileOperation()
        students_list = f.read_all()
        Report.show_students(students_list)

    def __str__(self):
        output = f"{self.first_name}, {self.last_name}"
        return output
