# Object Oriented Programming
# Object = Instance
# class User:
#     # attributes
#     # methods
#     def __init__(self, user_id, username): #self means this instance.
#         self.id = user_id
#         self.username = username
#
# user_1 = User("787", "jhiu") # memory is allocated when user is created
# user_2 = User("787",  "jh")


# Quiz Bank Game

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quizz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")

