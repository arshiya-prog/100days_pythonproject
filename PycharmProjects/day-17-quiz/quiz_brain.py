class QuizBrain:
    def __init__(self, que):
        self.question_number = 0
        self.question_list = que
        self.score = 0
        self.user_ans = ""

    def still_has_questions(self):
        length = len(self.question_list)
        if self.question_number < length:
            return True
        else:
            return False

    def next_question(self):
        q = self.question_list[self.question_number]
        self.question_number += 1
        self.user_ans = input(f"Q.{self.question_number}: {q.text} (True/False)?: ").lower()
        self.check_answer(self.user_ans, q.ans)

    def check_answer(self, inp, ans):
        if ans.lower() == inp.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {ans}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("")


