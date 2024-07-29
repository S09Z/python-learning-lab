class QuizBrain:
    def __init__(self, args_list):
        self.question_number = 0
        self.score = 0
        self.question_list = args_list

    def still_has_question_left(self):
        return self.question_number <= len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number + 1}: {current_question['Question']} (True/False): ")
        self.check_answer(answer.upper(), current_question['Answer'].upper())

    def check_answer(self, user_answer, correct_answer):
        if (user_answer[0] == correct_answer[0]
        or user_answer == correct_answer):
            self.score += 1
            print("Your answer are correct.")
        else:
            print("That's wrong.")
        print(f"The correct answer are {correct_answer}.")
        print(f"Your point are {self.score}/{self.question_number}\n")
