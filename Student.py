from Person import Person
from Grader import Grader


class Student(Person):
    """
    A class representing a student.

    Attributes:
        id (int): the id of the student.
        name (str): the name of the student.
        age (int): the age of the student.
        email (str): the email of the student.
        gpa (float): the GPA of the student.
        level (int): the level of the student.
        enrolled_courses (list): list of courses that enrolled by student.
    """
    def __init__(self, id: int, name: str, age: int, email: str, gpa: float, level: int, enrolled_courses: list):
        """
        Initialize a Student object.

        Args:
            id (int): the id of the student.
            name (str): the name of the student.
            age (int): the age of the student.
            email (str): the email of the student.
            gpa (float): the GPA of the student.
            level (int): the level of the student.
            enrolled_courses (list): The courses enrolled by the student.

        """
        super().__init__(id, name, age, email)
        self.gpa = gpa
        self.level = level
        self.enrolled_courses = enrolled_courses

    def get_level(self):
        """
        Get the level of the student.

        Returns:
            int: The level of the student.
        """
        return self.level

    def get_gpa(self):
        """
        Get the GPA of the student.

        Returns:
            float: GPA of the student.
        """
        return self.gpa

    def get_enrolled_courses(self):
        """
        Get the courses enrolled by the student.

        Returns:
            list: the courses enrolled by the student.
        """
        return self.enrolled_courses

    def get_enrolled_cousrses_info(self):
        """
        Get information about the courses enrolled by the student.

        Returns:
            str: the information about the courses enrolled by the student.
        """
        if len(self.enrolled_courses) > 0:
            return_string = f"***************\nAll courses Enrolled by student with ID: {self.get_id()}\n"
            for index, course in enumerate(self.enrolled_courses):
                return_string += f"{index+1}. course Id : {course.get_id()} - course name : {course.get_name()}\n"
            return return_string
        else:
            print('student not assigned to courses yet')

    def get_std_info(self):
        """
        Get the information about the student.
        Returns:
            str: the information about the student.
        """
        return (f"ID: {self.get_id()}\nName: {self.get_name()}\nAge : {self.get_age()}\nEmail : {self.get_email()}\nGPA : {self.get_gpa()}\nLevel: {self.get_level()}\n{self.get_enrolled_cousrses_info()}")


    def set_gpa(self):
        self.gpa = Grader(self).cal_gpa()