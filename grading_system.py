from Instructor import Instructor
from Student import Student
from Course import Course
from helper import read_csv, read_json_file
from constants import STUDENTS_SHEET_PATH, INSTRUCTOR_SHEET_PATH, COURSES_SHEET_PATH

class GradingSystem:
    def __init__(self):
        
        self.courses_lst = []
        self.std_lst = []
        self.instructors_lst = []

        course_lst = read_csv(COURSES_SHEET_PATH)
        print(course_lst)
        for course in course_lst:
            course = Course(id=course['id'], name=course['name'], instructor=course['instructor'])
            self.courses_lst.append(course)

        students_lst = read_csv(STUDENTS_SHEET_PATH)
        for student in students_lst:
            std_courses = []
            for c_id in student['enrolled_courses']:
                std_courses.append(self.search_course(c_id))
            std = Student(id=student['id'], name=student['name'], age=student['age'], email=student['email'], gpa=student['gpa'], level=student['level'], enrolled_courses=std_courses)
            self.std_lst.append(std)

        
        instructor_lst = read_csv(INSTRUCTOR_SHEET_PATH)
        for instructor in instructor_lst:
            inst_courses = []
            for c_id in student['enrolled_courses']:
                inst_courses.append(self.search_course(c_id))
            inst = Instructor(id=instructor['id'], name=instructor['name'], age=instructor['age'], email=instructor['email'],teach_courses=inst_courses)
            self.instructors_lst.append(inst)

       

        
    def create_course(self, id, name, instructor):
        try:
            self.courses_lst.append(Course(id=id, name=name, instructor=instructor))
        except Exception as e:
            print(f'Error: {e}')

    def create_student(self, id, name,age,email,gpa,level,enrolled_courses):
        try:
            self.std_lst.append(Student(id=id, name=name,age=age,email=email,gpa=gpa,level=level,enrolled_courses=enrolled_courses))
        except Exception as e:
            print(f'Error: {e}')

    
    def create_instructor(self, id, name,age,email,teach_courses):
        try:
            self.std_lst.append(Instructor(id=id, name=name,age=age,email=email,teach_courses=teach_courses))
        except Exception as e:
            print(f'Error: {e}')

    
    def search_course(self,id):
        for course in self.courses_lst:
            if course.get_id() == id:
                return course

    def search_student(self,id):
        for student in self.std_lst:
            if student.get_id() == id:
                print(student.get_id(), id)
                return student
                    


    def search_instructor(self,id):
        for instructor in self.instructors_lst:
            if instructor.get_id() == id:
                return instructor

    
