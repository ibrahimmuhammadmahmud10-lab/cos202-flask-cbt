
from datetime import datetime
from collections import deque

class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer == self.answer


class CBT:
    def __init__(self):
        self.questions = deque()
        self.score = 0
        self.timestamp = None

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.questions:
            return self.questions.popleft()
        return None

    def submit_result(self):
        self.timestamp = datetime.now()
        return self.score, self.timestamp
