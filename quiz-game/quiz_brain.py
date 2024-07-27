class QuizBrain:
    def __init__(self, args_list):
        self.question_number = 0
        self.question_list = args_list

    def NextQuestion(self):
        current_question = self.question_list[self.question_number]
        input(f"Q.{self.question_number}: {current_question.Question} (True/False)")

    def QuizChallenge(self):
        pass
