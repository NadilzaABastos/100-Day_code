# Asking the questions
# Checking if the answer was correct
# Checking if we're the end of the quiz


class QuizBrain:
    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True

        else:
            False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        guess = input(f"Q.{self.question_number} : {current_question.text} (True / False ) : ")
        self.check_answer(guess ,current_question.answer,)

    def check_answer(self,guess , right_answer):
        if guess == right_answer.lower():
            self.score += 1
            print("You got it right !")
        else:
            print("Sorry, that`s wrong")
        print(f"The correct answer was {right_answer}")
        print(f"Your current score is {self.score}/ {self.question_number} :")
        print("\n")




