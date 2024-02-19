import json


class FileOperation:
    def __init__(self, filename="data.txt"):
        self.filename = filename

    def write(self, data):
        json_data = json.dumps(data)
        f = open(self.filename, "a")
        f.write("\n")
        f.write(json_data)

    def read_all(self):
        lst_ = [1, 2, 3, 4]
        return lst_

    def read_record(self, name, family):
        print(self.read_all())
        pass

    def read_classroom(self, field, grade):
        pass
