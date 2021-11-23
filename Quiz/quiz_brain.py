class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self) -> None:
        que = self.question_list[self.question_no]
        self.question_no += 1
        self.check_answer(input(f"Q{self.question_no}. {que.text} (True/False): "), que.answer)

    def still_has_question(self) -> bool:
        return self.question_no < len(self.question_list)

    def check_answer(self, user_ans: str, correct_answer: str) -> None:
        if user_ans.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("Incorrect answer")
        print(f"The correct answer was {correct_answer}")
        print(f"Total correct answers are; {self.score} out of {self.question_no}")
        print("\n")


if __name__ == '__main__':
    pass
