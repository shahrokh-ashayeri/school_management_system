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
        elements = list()
        with open(self.filename, mode="r") as element:
            line = element.readline()
            while line:
                row = json.loads(line)
                elements.append(row)
                line = element.readline()

        return elements

    def read_record(self, name, family):
        print(self.read_all())
        pass

    def read_classroom(self, field, grade):
        pass
