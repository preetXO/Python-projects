class Question:
    def __init__(self, q_text: str, q_answer: str):
        """Takes in a question and it's answer as arguments"""
        self.text = q_text
        self.answer = q_answer


if __name__ == '__main__':
    import data
    que1 = Question(data.question_data[0]["text"],
                    data.question_data[0]["answer"])
    print(que1.text, que1.answer)
