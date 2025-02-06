from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_text = item["text"]
    question_ans = item["answer"]
    question = Question(question_text, question_ans)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    if quiz.user_ans == "off":
        break
    else:
        quiz.next_question()

print("The quiz is completed!")
print(f"Your final score is: {quiz.score}/{len(question_data)}")
