from constants import HW_RATIO, EXAM_RATIO, TEST_RATIO


class Grader:
    def __init__(self, std):
        self.std = std

    def cal_gpa(self):
        gpa = 0
        courses = self.std.enrolled_courses

        for course in courses:
            hw_lst = course.get_hw_lst()
            tests_lst = course.get_test_lst()
            exams_lst = course.get_exams_lst()

            hw_points = course.cal_hw_points()
            test_points = course.cal_tests_points()
            exam_points = course.cal_exams_points()

            std_hw_points = 0
            std_test_points = 0
            std_exam_points = 0

            for hw in hw_lst:
                submissions = hw.get_submissions()

                for sub in submissions:
                    if sub.get_std() == self.std:
                        std_hw_points += sub.get_grade()

            hw_equivalent_points = (std_hw_points / hw_points) * HW_RATIO

            hw_grade = round(hw_equivalent_points, 1)
            gpa += hw_grade

            for test in tests_lst:
                submissions = test.get_submissions()

                for sub in submissions:
                    if sub.get_std() == self.std:
                        std_test_points += sub.get_grade()
            try:

                test_equivalent_points = (
                    std_test_points / test_points) * TEST_RATIO
                test_grade = round(test_equivalent_points, 1)
            except Exception as e:
                test_grade = 0

            gpa += test_grade

            for exam in exams_lst:
                submissions = exam.get_submissions()

                for sub in submissions:
                    if sub.get_std() == self.std:
                        std_exam_points += sub.get_grade()
            try:

                exam_equivalent_points = (
                    std_exam_points / exam_points) * EXAM_RATIO
                exam_grade = round(exam_equivalent_points, 1)
            except Exception as e:
                exam_grade = 0
            gpa += exam_grade

        return gpa
