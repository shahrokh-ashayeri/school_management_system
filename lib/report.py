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
