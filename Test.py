from Assessment import Assessment 

class Test(Assessment):
    def __init__(self, id, title, time):
        super().__init__(id)
        self.title = title
        self.time = time