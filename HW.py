from Assessment import Assessment


class HomeWork(Assessment):

    def __init__(self, id, title, due_date):
        super().__init__(id)
        self.title = title
        self.due_date = due_date

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_due_date(self):
        return self.due_date

    def view_info(self):
        return (f'Id: {self.get_id()} - title {self.get_title()} - due date {self.get_due_date()}')

    def view_hw(self):
        print(self.view_info())
        self.view_assessment()
