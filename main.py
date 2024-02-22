from lib.student import Student
from lib.classroom import Classroom
from lib.report import Report
from lib.file_op import FileOperation
from lib.menu import Menu

if __name__ == "__main__":
    command = ""
    while command.lower() != "q":
        menu = Menu()
        command = menu.show()
        menu.command(command)
