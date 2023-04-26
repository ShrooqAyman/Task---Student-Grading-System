from HW import HomeWork
from Exam import Exam
from Test import Test


class Course:
    def __init__(self, id, name, instructor):
        self.id = id
        self.name = name
        self.instructor = instructor
        self.students = []
        self.hw_lst = []
        self.tests_lst = []
        self.exams_lst = []
        self.hw_points = 0
        self.tests_points = 0
        self.exams_points = 0

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_instructor(self):
        return self.instructor

    def get_students(self):
        return self.students

    def add_student(self, student):
        self.students.append(student)

    def create_hw(self, id, title, due_date):
        hw = HomeWork(id=id, title=title, due_date=due_date)
        self.hw_lst.append(hw)
        return hw

    def create_exam(self, id, title, time):
        exam = Exam(id=id, title=title, time=time)
        self.exams_lst.append(exam)
        return exam

    def create_test(self, id, title, time):
        test = Test(id=id, title=title, time=time)
        self.tests_lst.append(test)
        return test

    def get_all_hw(self):
        for hw in self.hw_lst:
            return (f'HW Id : {hw.get_id()}\nTitle : {hw.get_title()}\n')

    def cal_hw_points(self):
        for hw in self.hw_lst:
            self.hw_points += hw.get_total_points()
        return self.hw_points

    def cal_tests_points(self):
        for test in self.tests_lst:
            self.tests_points += test.get_total_points()
        return  self.tests_points

    def cal_exams_points(self):
        for exam in self.exams_lst:
            self.exams_points += exam.get_total_points()

        return   self.exams_points

    def get_hw_lst(self):
        return self.hw_lst

    def get_test_lst(self):
        return self.tests_lst

    def get_exams_lst(self):
        return self.exams_lst


