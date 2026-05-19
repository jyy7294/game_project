import random

class Game:

    def __init__(self,correct_id,correct_pw):
        self.correct_id = correct_id
        self.corred_pw = correct_pw
        option = ["가위","바위","보"]
        self.answer = random.choice(option)

    def