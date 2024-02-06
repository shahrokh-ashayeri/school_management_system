class Classroom:
    def __init__(self, students, field_of_study, grade) -> None:
        self.students = students
        self.field = field_of_study
        self.grade = grade

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
