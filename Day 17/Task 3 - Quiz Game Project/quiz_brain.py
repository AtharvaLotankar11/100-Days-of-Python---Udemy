#TODO 1: To Create a Class called QuizBrain.
#TODO 2: Write an __init__() method
    #TODO 2.1: Inside method initialise question_number to 0
    #TODO 2.2: Inside method also initialise question_list to an input
#TODO 3: Retrieve the item at the current question_number from the question_list
#TODO 4: Use the input() function to show the user the Question text and ask for user's answer
#TODO 5: Create method called 'still_has_questions()'
    #TODO 5.1: Return a boolean depending on the value of question_number
    #TODO 5.2: Use the while loop to show the next question until the end
#TODO 6: Create check_answer() to verify user's answer with correct answer
    #TODO 6.1: Print out Score - if correct: increment lest original score

class QuizBrain:
    """QuizBrain class"""

    def __init__(self, question_list):
        """Constructor"""
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1 #Change Q.0->Q.1 and iterating...
        user_answer = input(f"Q.{self.question_number}.: {current_question.text} (True/False): ")
        self.check_answer(current_question.answer, user_answer)

    def check_answer(self, correct_answer, user_answer):
        if correct_answer.lower() == user_answer.lower():
            self.score += 1
            print("Yay! You got it right.")
        else:
            print("Oops! You missed it.")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}.")
        print("\n")

    def still_has_questions(self, limit):
        return self.question_number < limit
