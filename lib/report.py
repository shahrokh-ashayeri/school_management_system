from rich.table import Table
from rich.console import Console


class Report:
    def show_scores(self, student):
        table = Table(title=f"{student.first_name}, {student.last_name}")
        table.add_column("Course")
        table.add_column("Score")

        for course, score in student.scores.items():
            table.add_row(str(course), str(score))

        console = Console()
        console.print(table)

    @staticmethod
    def show_students(students):
        table = Table(title="Students List")
        table.add_column("ID")
        table.add_column("First Name")
        table.add_column("Last Name")
        table.add_column("Field")
        table.add_column("Grade")

        for student in students:
            table.add_row(
                str(student["id"]),
                str(student["first_name"]),
                str(student["last_name"]),
                str(student["field"]),
                str(student["grade"]),
            )

        console = Console()
        console.print(table)
