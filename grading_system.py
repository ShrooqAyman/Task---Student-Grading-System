from Instructor import Instructor
from Student import Student
from Course import Course
from helper import read_csv, read_json_file
from constants import STUDENTS_SHEET_PATH, INSTRUCTOR_SHEET_PATH, COURSES_SHEET_PATH, HW_SHEET_PATH,ALL_QUESTIONS_PATH, ANSWERS_PATH
from HW import HomeWork

class GradingSystem:
    def __init__(self):
        
        self.courses_lst = []
        self.std_lst = []
        self.instructors_lst = []

        course_lst = read_csv(COURSES_SHEET_PATH)
        for course in course_lst:
            self.create_course(id=course['id'], name=course['name'], instructor=course['instructor'])

        students_lst = read_csv(STUDENTS_SHEET_PATH)
        for student in students_lst:
            std_courses = []
            for c_id in student['enrolled_courses']:
                std_courses.append(self.search_course(c_id))

            self.create_student(id=student['id'], name=student['name'], age=student['age'], email=student['email'], gpa=student['gpa'], level=student['level'], enrolled_courses=std_courses)

        instructor_lst = read_csv(INSTRUCTOR_SHEET_PATH)
        for instructor in instructor_lst:
            inst_courses = []
            for c_id in student['enrolled_courses']:
                inst_courses.append(self.search_course(c_id))
    
            self.create_instructor(id=instructor['id'], name=instructor['name'], age=instructor['age'], email=instructor['email'],teach_courses=inst_courses)


        course_1 = self.search_course(1)
        std_1 = self.search_student(1)

        hw_lst = read_csv(HW_SHEET_PATH)
        for hw in hw_lst:
            h = course_1.create_hw(id=hw['id'], title=hw['title'], due_date=hw['due_date'])
            h.add_questions(ALL_QUESTIONS_PATH)
            h.add_submission(std_1, ANSWERS_PATH)

        self.enroll_std_in_course(course_id=1,std_id=1)

        
    def create_course(self, id, name, instructor):
        try:
            self.courses_lst.append(Course(id=id, name=name, instructor=instructor))
            return True
        except Exception as e:
            print(f'Error: {e}')
            return False

    def create_student(self, id, name,age,email,gpa,level,enrolled_courses):
        try:
            self.std_lst.append(Student(id=id, name=name,age=age,email=email,gpa=gpa,level=level,enrolled_courses=enrolled_courses))
            return True
        except Exception as e:
            print(f'Error: {e}')
            return False

    
    def create_instructor(self, id, name,age,email,teach_courses):
        try:
            self.instructors_lst.append(Instructor(id=id, name=name,age=age,email=email,teach_courses=teach_courses))
            return True
        except Exception as e:
            print(f'Error: {e}')
            return False

    
    def search_course(self,id):
        for course in self.courses_lst:
            if course.get_id() == id:
                return course

    def search_student(self,id):
        for student in self.std_lst:
            if student.get_id() == id:
                return student
                   

    def search_instructor(self,id):
        for instructor in self.instructors_lst:
            if instructor.get_id() == id:
                return instructor


    def enroll_std_in_course(self, std_id, course_id):
        try:
            std = self.search_student(std_id)
            course = self.search_course(course_id)
            course.add_student(std)
            return True
        except Exception as e:
            print(f'Error : {e}')
            return False

    def show_all_courses(self):
        if len(self.courses_lst) > 0:
            for course in self.courses_lst:
                print(course.get_course_info())

    def show_students(self):
        if len(self.std_lst) > 0:
            for std in self.std_lst:
                print(std.get_std_info())


    def show_instructors(self):
        if len(self.instructors_lst) > 0:
            for inst in self.instructors_lst:
                print(inst.get_inst_info())
