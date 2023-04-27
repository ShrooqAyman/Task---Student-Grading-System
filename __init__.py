from grading_system import GradingSystem

import argparse


if __name__== "__main__":
    g = GradingSystem()
    parser = argparse.ArgumentParser()
    parser.add_argument('-id', '--id', type=int, help='person id')
    parser.add_argument('-course_id', '--course_id', type=int, help='course id')
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
    parser.add_argument('--enroll_std_to_course', action='store_true', help='add student')
    parser.add_argument('--show_students', action='store_true', help='show_students')
    parser.add_argument('--show_instructors', action='store_true', help='show_instructors')


    args = parser.parse_args()
    all_args =vars(args)
    n_args = sum([ 1 for arg in all_args.values( ) if arg])


    if args.add_student:
        if args.id is None or args.name is None or args.age is None or args.email is None or args.gpa is None or args.level is None:
            parser.error('required')
        else:
            g.create_student(args.id, args.name , args.age , args.email,args.gpa ,args.level,[])
            print('student added successfully')


    if args.add_instructor:
        if args.id is None or args.name is None or args.age is None or args.email is None:
            parser.error('required')
        else:
            g.create_instructor(args.id, args.name , args.age , args.email, teach_courses=args.teach_courses)
            print('instructor added successfully')


    if args.search_std:
        if args.id is None:
            parser.error('required')
        else:
            if g.search_student(args.id) is not None:
                print(g.search_student(args.id).get_std_info())
            else:
                print(f'not found student with ID {args.id}')

    if args.show_course:
        if args.id is None:
            parser.error('required')
        else:
            if g.search_course(args.id) is not None:
                print(g.search_course(args.id).get_course_info())
            else:
                print(f'not found course with ID {args.id}')
        
    if args.enroll_std_to_course:
        if args.id is None or args.course_id is None:
            parser.error('required')
        else:
            if g.enroll_std_in_course(std_id=args.id, course_id=args.course_id):
                print(f'student {args.id} enrolled to course {args.course_id}')
                print(g.search_course(args.course_id).get_course_info())

            else:
                print(f'student not enrolled to course')

    if args.show_courses:
        print(g.show_all_courses())

    if args.show_students:
        print(g.show_students())

    if args.show_instructors:
        print(g.show_instructors())
