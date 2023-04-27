from Person import Person


class Instructor(Person):
    """
    A class representing a Instructor.

    Attributes:
        id (int): the id of the student.
        name (str): the name of the student.
        age (int): the age of the student.
        email (str): the email of the student.
        teach_courses (list): list of courses that teach by the instructor.
    """
    def __init__(self, id: int, name: str, age: int, email: str, teach_courses: list):
        """
        Initialize a Instructor object.

        Args:
            id (int): the id of the student.
            name (str): the name of the student.
            age (int): the age of the student.
            email (str): the email of the student.
            teach_courses (list): list of courses that teach by the instructor.

        """
        super().__init__(id, name, age, email)
        self.teach_courses = teach_courses

    def get_teach_courses(self):
        """
        Get information about the courses that teach by the instructor.

        Returns:
            str: the information about the courses that teach by the instructor.
        """
        if len(self.teach_courses) > 0:
            return_string = f"All courses Enrolled by student with ID: {self.get_id()}\n"
            for index, course in enumerate(self.teach_courses):
                return_string += f"{index+1}. course Id : {course.get_id()} - course name : {course.get_name()}\n"
            return return_string
        else:
            print('instructor not assigned to courses yet')

        

    def get_inst_info(self):
        """
        Get information about the instructor.

        """
        return (f"ID: {self.get_id()}\nName: {self.get_name()}\nAge : {self.get_age()}\nEmail : {self.get_email()}\n{self.get_teach_courses()}")
