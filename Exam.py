from Assessment import Assessment


class Exam(Assessment):
    def __init__(self, id, title, time):
        super().__init__(id)
        self.title = title
        self.time = time
