from helper import read_json_file


class Submission:
    def __init__(self, std, answers):
        self.std = std
        self.answers = answers
        self.grade = 0

    def get_grade(self):
        return self.grade

    def get_std(self):
        return self.std

    def get_answers(self):
        return read_json_file(self.answers)