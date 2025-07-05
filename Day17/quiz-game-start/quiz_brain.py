class QuizBrain:
    def __init__(self,q_list):
        self.question_no=0
        self.question_list=q_list
        self.score=0

    def still_has_questions(self):
        if self.question_no<len(self.question_list):
            return True
        else:
            return False


    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            print("You got it right")
            self.score+=1
            print(f"Your current score is {self.score}/{self.question_no}")
        else:
            print("You got it wrong")
            print(f"Your current score is {self.score}/{self.question_no}")
        print(f"The correct answer was {correct_answer}")




    def next_question(self):
        current_question=self.question_list[self.question_no]
        self.question_no+=1
        user_answer=input(f"Q.{self.question_no} {current_question.text} (TRUE/FALSE): ")
        self.check_answer(user_answer,current_question.answer)

