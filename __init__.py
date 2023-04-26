from grading_system import GradingSystem
from Grader import Grader
from constants import ANSWERS_PATH, ALL_QUESTIONS_PATH
import argparse


def operations():
    g = GradingSystem()
            
    # create courses
    g.create_course(id=1, name='OS', instructor=1)
    g.create_course(id=2, name='web', instructor=2)

    # create students
    g.create_student(1, 'Shurouq', 23, "shurouqewaili@gmail.com",gpa=0, level=1, enrolled_courses=[])

    # create instructor
    g.create_instructor(id=1, name="Ibrahim", age=60,email='a@gmail.com', teach_courses=[])
    g.create_instructor(id=2, name="Hatem", age=60,email='h@gmail.com', teach_courses=[])
   

    c1 = g.search_course(1)
    std = g.search_student(1)
    print(std)
    print(std.get_name())
    # add students to course
    c1.add_student(std)
    #print(c1.get_name())

    # add new hw
    hw = c1.create_hw(id=1, title="hw1", due_date="20-01-2020")
    hw.add_questions(ALL_QUESTIONS_PATH)
    #print(c1.get_all_hw())

    hw.add_submission(std=std, answers=ANSWERS_PATH)
    #print(Grader(std=std).cal_gpa())

    return g



if __name__== "__main__":
    g = GradingSystem()

    
    parser = argparse.ArgumentParser()
    parser.add_argument('-id', '--id', type=int, help='id')
    parser.add_argument('-age', '--age', type=int, help='age')
    parser.add_argument('-name', '--name', type=str, help='name')
    parser.add_argument('-email', '--email', type=str, help='email')
    parser.add_argument('-gpa', '--gpa', type=int, help='gpa')
    parser.add_argument('-level', '--level', type=int, help='level')
    parser.add_argument('-e', '--enrolled_courses', type=str, help='enrolled_courses')
    parser.add_argument('-t', '--teach_courses', type=str, help='teach_courses')

    parser.add_argument('--add_student', action='store_true', help='add student')
    parser.add_argument('--add_instructor', action='store_true', help='add_instructor')
    parser.add_argument('--search_std', action='store_true', help='search_std')
    parser.add_argument('--show_courses', action='store_true', help='show_courses')
    parser.add_argument('--show_course', action='store_true', help='show_course')


    args = parser.parse_args()
    # count number of passed args 
    all_args =vars(args)
    n_args = sum([ 1 for arg in all_args.values( ) if arg])


    if args.add_student:
        if args.id is None or args.name is None or args.age is None or args.email is None or args.gpa is None or args.level is None:
            parser.error('required')
        else:
            g.create_student(args.id, args.name , args.age , args.email,args.gpa ,args.level,[])

    if args.add_instructor:
        if args.id is None or args.name is None or args.age is None or args.email is None:
            parser.error('required')
        else:
            g.create_instructor(args.id, args.name , args.age , args.email)
    if args.search_std:
        if args.id is None:
            parser.error('required')
        else:
            print(g.search_student(args.id))
