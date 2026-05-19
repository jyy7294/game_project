import random

class Game:

    def __init__(self, correct_id, correct_pw, max_attempts):
        self.correct_id = correct_id
        self.correct_pw = correct_pw
        self.max_attempts = max_attempts
        self.guessed = []
        self.record = []
        self.success = []
        self.failure = []
        self.character = []
        words= ["python","apple","banana","school","computer"]
        self.answer= random.choice(words)

    def input_word(self):
        while True:
                
                guess = input("글자를 입력하세요 :").lower()

                if len(guess) != 1:
                    print("한 번에 한 글자만 입력할 수 있습니다.")
                    continue
                if not('a' <= guess <= 'z'):
                    print("알파벳만 입력하세요.")
                    continue
            
                return guess
        
            
    def guess_in_answer(self,guess):
        self.guessed.append(guess)
        character = []
        for word in self.answer: 
            if word in self.guessed:  
               character.append(word) 
            else:
                character.append("_")
        self.character = character                            
                
        print("정답에 포함된 글자입니다.")
        print()

        print("단어: ",end="")
        for p in character:
            print(p,end="")

        print()
        print(f"남은 기회: {self.max_attempts}")
        print(f"입력한 글자: {guess}")

        if "_" not in character :
            print("승리하였습니다.")
            self.success.append(self.correct_id)
            return True
        
        return False

    def not_in_answer(self,guess):
            self.record.append(guess)
            print("틀렸습니다.")
            print()
            print("단어: ",end="")
            for p in self.character:
                print(p,end="")
            print()
            self.max_attempts -= 1
            print(f"남은 기회: {self.max_attempts}")
            print("입력한 글자: ",end="")
            for p in self.record:
                print(p,end=" ")
            print()
            if self.max_attempts == 0:
                 print("패배하였습니다.")
                 self.failure.append(self.correct_id)
                 return True
            
            return False

    def play(self):
        print("글자를 맞혀 보세요")

        self.character = ["_"] * len(self.answer)

        while True:
            guess = self.input_word()

            if (guess in self.guessed) or (guess in self.record):
                 print("이미 입력한 글자는 다시 입력할 수 없습니다.")
                 continue
            if not ('a' <= guess <= 'z') :
                 print("알파벳만 입력하세요.")
                 continue
            if ('A' <= guess <= 'Z'):
                 guess = guess.lower()
                 continue
            if (len(guess) > 1):
                 print("한 번에 한 글자만 입력할 수 있습니다.")
                 continue
            
            if guess in self.answer:
                self.guess_in_answer(guess)

            else:
                self.not_in_answer(guess)

행맨_game = Game()
행맨_game.play()
    