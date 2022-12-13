from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
# write a for loop to iterate over the questiom_data
# Create a Question object from each entry question_data
# Append each Question object to the question_bank

question_bank = []

for question in question_data:
    new_text = question["text"]
    new_answer = question["answer"]
    new_question = Question(new_text,new_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("you've complete the quiz ")
print(f"Your final score was : {quiz.score} /{quiz.question_number}")