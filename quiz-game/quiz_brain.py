class QuizBrain:
    def __init__(self, args_list):
        self.question_number = 0
        self.correct_answer_count = 0
        self.question_list = args_list

    def NextQuestion(self):
        current_question = self.question_list[self.question_number]

        answer = input(f"Q.{self.question_number + 1}: {current_question['Question']} (True/False): ")
        if (answer[0].upper() == current_question['Answer'][0].upper()
        or answer.upper() == current_question['Answer'].upper()):
            self.correct_answer_count += 1
        self.question_number += 1
        print(f"Your point are {self.correct_answer_count} of {self.question_number}\n")

        if self.correct_answer_count <= len(self.question_list):
            self.NextQuestion()