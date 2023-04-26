class Question:

    def __init__(self, id, question, answer, points):
        self.id = id
        self.question = question
        self.answer = answer
        self.points = points

    def get_question(self):
        return self.question

    def get_answer(self):
        return self.answer

    def get_points(self):
        return self.points


class MultipleChoice(Question):
    def __init__(self, id, question, choices, answer, points):
        super().__init__(id, question, answer, points)
        self.choices = choices

    def get_choices(self):
        for choice in self.choices:
            return (self.choices)


class TrueFalse(Question):
    def __init__(self, id, question, answer, points):
        super().__init__(id, question, answer, points)


class Coding(Question):
    def __init__(self, id, question, answer, points):
        super().__init__(id, question, answer, points)
