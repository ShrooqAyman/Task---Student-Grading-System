from Person import Person


class Instructor(Person):
    def __init__(self, id: int, name: str, age: int, email: str, teach_courses: list):
        super().__init__(id, name, age, email)
        self.teach_courses = teach_courses

    def get_teach_courses(self):
        for course in self.teach_courses:
            return (f"course Id : {course.get_id()}\ncourse name : {course.get_name()}")

    def get_inst_info(self):
        return (f"ID: {self.get_id()}\nName: {self.get_name()}\nAge : {self.get_age()}\nEmail : {self.get_email()}\n{self.get_teach_courses()}")
