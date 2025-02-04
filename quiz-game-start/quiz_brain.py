class QuizBrain:
    def __init__(self,q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0


    def still_has_question(self):
        if self.question_num < len(self.question_list):
            return True
        else:
            False
    def nextquestion(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num} : {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

        def check_answer(self, user_answer, current_answer):
            if user_answer.lower() == current_answer.lower():
                print("You got it right!")
                self.score += 1
            else:
                print("You got it wrong!")
                
            print(f"The correct answer is {current_answer}")
            print(f"Your current score is {self.score}/{self.question_num}")



