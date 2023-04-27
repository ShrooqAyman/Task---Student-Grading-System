from Question import MultipleChoice, TrueFalse
from submission import Submission
from helper import read_json_file


class Assessment:
    def __init__(self, id):
        self.id = id
        self.m_lst = []
        self.true_false_lst = []
        self.coding_lst = []

        self.answers_lst = []
        self.submissions = []
        self.total_points = 0


    def get_total_points(self):
        return self.total_points


    def get_submissions(self):
        return self.submissions


    def add_questions(self, file_input):
        all_question = read_json_file(file_input)
        for question in all_question:
            self.answers_lst.append(
                {question['id']: {"answers": question['answer'], 'points': question["points"]}})

            if question['type'] == 'multipleChoice':
                question_obj = MultipleChoice(id=question["id"], question=question["question"],
                                              choices=question['choices'], answer=question["answer"], points=question["points"])
                self.m_lst.append(question_obj)
                self.total_points += question['points']

            elif question['type'] == 'trueFalse':
                question_obj = TrueFalse(
                    id=question["id"], question=question["question"], answer=question["answer"], points=question["points"])
                self.true_false_lst.append(question_obj)
                self.total_points += question['points']



    def view_assessment(self):
        if len(self.m_lst) == 0 and len(self.true_false_lst) == 0:
            print('Questions not added yet')
            return
        else:
            print(f'total points {self.total_points}\n')
            if len(self.m_lst) > 0:
                print('\nchoose correct answer:\n ')
                for q in self.m_lst:
                    print(
                        f'{q.get_question()}   ({q.get_points()} points)\n{q.get_choices()}')

            if len(self.true_false_lst) > 0:
                print('\nTrue or False:\n ')
                for q in self.true_false_lst:
                    print(
                        f'{q.get_question()}   ({q.get_points()} points)\nTrue\nFalse')


    def add_submission(self, std, answers):
        try:
            sb = Submission(std=std, answers=answers)
            sb.grade = self.cal_grade(sb)
            self.submissions.append(sb)
        except Exception as e:
            print(f'Error {e}')


    def cal_grade(self, sb):
        std_answers = sb.get_answers()
        total_points = 0
        for result in self.answers_lst:
            qid = list(result.keys())[0]
            expected_answer = result[qid]['answers']
            expected_points = result[qid]['points']

            for answer in std_answers:
                if answer['id'] == qid:
                    given_answer = answer['answer']
                    if given_answer == expected_answer:
                        total_points += expected_points
        return total_points
