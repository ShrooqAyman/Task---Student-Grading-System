import os

file_path = os.path.realpath(__file__)
directory = r'C:\Users\hp\Desktop\Pythonprogramming\week4\oop2\task\data'

ALL_QUESTIONS_PATH = os.path.join(directory, 'all_questions.json') 
ANSWERS_PATH = os.path.join(directory, 'submission.json') 
STUDENTS_SHEET_PATH = os.path.join(directory, 'all_students.csv') 
INSTRUCTOR_SHEET_PATH = os.path.join(directory, 'all_instructor.csv') 
COURSES_SHEET_PATH = os.path.join(directory, 'courses.csv') 
