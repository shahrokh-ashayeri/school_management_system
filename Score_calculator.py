from rich.console import Console
from rich.table import Table


class Student:
    # Gets firstname and lastname
    def __init__(self, f_name, l_name) -> None:
        self.courses = [
            "Math",
            "IS and web development",
            "Basic Technichal Knowledge",
            "Human and environment ",
            "Arabic Language",
        ]
        self.first_name = f_name
        self.last_name = l_name

    def set_scores(self):
        print(f"{self.last_name}, {self.first_name}".center(50, "-"))
        scores = dict()
        for course in self.courses:
            score = float(input(f"{course}: "))
            scores[course] = score
        self.scores = scores

    def get_transcript(self):
        output = dict()
        output["first_name"] = self.first_name
        output["last_name"] = self.last_name
        output["scores"] = dict()

        for course, score in self.scores.items():
            output["scores"][course] = score

        self.transcript = output
        return self.transcript

    def show(self):
        table = Table(title=f"{self.first_name}, {self.last_name}")
        table.add_column("Course")
        table.add_column("Score")

        for course, score in self.scores.items():
            table.add_row(str(course), str(score))

        console = Console()
        console.print(table)


class Classroom:
    def __init__(self, students) -> None:
        self.students = students

    def best_scores(self):
        max_scores = dict()
        for student in self.students:
            for course, score in student.scores.items():
                if course not in max_scores.keys():
                    max_scores[course] = {
                        f"{student.first_name}, {student.last_name}": score
                    }
                else:
                    current_data = list(max_scores[course].items())[0]

                    if current_data[1] < student.scores[course]:
                        max_scores[course] = {
                            f"{student.first_name}, {student.last_name}": student.scores[
                                course
                            ]
                        }
        return max_scores


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
    c = Classroom(students=students)
    print(c.best_scores())
