from .student import Student
from .file_op import FileOperation


class Menu:
    def __init__(self):
        pass

    def command(self, cmd):
        if cmd == "1":
            studnet = Student.set_private_attr()
            f = FileOperation()
            f.write(studnet.get_private_attr())
        elif cmd == "5":
            Student.get_all()
        elif cmd == "8":
            Student.search(grade="11", last_name="mortezaqoli")
        else:
            print("invalid command")

    def show(self):
        menu_items = """
        1- Add new student
        2- Add new Teacher
        3- Get student transcript
        4- Enter scores
        5- Show all students
        6- Show all teachers
        7- Report
        8- Search (default:mohammad)
        """

        print(menu_items)
        command = input("Press a command number to continue [Q: Exit]: ")

        return command
