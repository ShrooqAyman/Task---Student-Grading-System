from Person import Person


class Student(Person):
    def __init__(self, id: int, name: str, age: int, email: str, gpa: float, level: str, enrolled_courses: list):
        super().__init__(id, name, age, email)
        self.gpa = gpa
        self.level = level
        self.enrolled_courses = enrolled_courses



    def get_level(self):
        return self.level

    def get_gpa(self):
        return self.gpa

    def get_enrolled_courses(self):
        return self.enrolled_courses

    def get_enrolled_cousrses_info(self):
        for course in self.enrolled_courses:
            return (f"course Id : {course.get_id()}\ncourse name : {course.get_name()}")

    def get_std_info(self):
        return (f"ID: {self.get_id()}\nName: {self.get_name()}\nAge : {self.get_age()}\nEmail : {self.get_email()}\nGPA : {self.get_gpa()}\nLevel: {self.get_level()}\n{self.get_enrolled_cousrses_info()}")
