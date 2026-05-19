import random

class UpDownGame:
    def __init__(self, start = 1, end = 150):
        self.start = start
        self.end = end
        self.target = random.randint(start,end)
        self.count = 0

    def input_number(self):
        while True:
            try:
                x = int(input("정답을 입력하세요."))
                return x
            except ValueError:
                print()
            except ValueError:
                print("1,2,3 번 중에 입력하세요.")
    
    def give_hint(self, x):
        if x < self.target:
            print("UP")
        elif x > self.target:
            print("DOWN")
    
    def give_extra_hint(self,x):
        difference = abs(self.target - x)

        if difference <= 5:
            print("힌트: 거의 다 왔습니다. ")
        elif difference <= 15:
            print("힌트: 가까워지고 있습니다.")
        else:
            print("힌트: 아직 멉니다.")

    def play(self):
        print(f"{self.start}부터 {self.end} 사이의 숫자를 맞혀보세요.")

        while True:
            x = self.input_number()
            self.count += 1

            if x == self.target:
                print(f"정답입니다! 시도 횟수: {self.count}회")
                nickname = input("닉네임을 입력하세요: ")
                return nickname,self.count
            
            self.give_hint(x)
            self.give_extra_hint(x)