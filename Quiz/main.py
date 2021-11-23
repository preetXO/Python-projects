from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
que_bank = []
for item in question_data:
    que = item["question"]
    answer = item["correct_answer"]
    que_bank.append(Question(que, answer))

if __name__ == '__main__':
    quiz = QuizBrain(que_bank)
    while quiz.still_has_question():
        quiz.next_question()
    print("\nThe quiz has finished")
    print(f"Your total score is {quiz.score} out of {len(que_bank)}")
