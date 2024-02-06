class Student:
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
