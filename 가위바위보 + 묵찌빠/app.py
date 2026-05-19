from .config import ID,PWD
from.login_manager import LoginManager
from.ranking_board import RankingBoard
from.가위바위보+묵찌빠_game import Game

class App:
    def __init__(self):
        self.login_manager = LoginManager(ID,PW)
        self.ranking_board = RankingBoard()
        self.correct_id = "admin"

    def print_menu(self):
        print()
        print("1. 게임 시작\n2. 전적 보기\n3. 게임 종료\n메뉴를 선택하세요: ")

    def input_menu(self):
        while True:
            try:
                num = int(input("메뉴를 선택하세요: "))
                return num
            except ValueError:
                print("숫자만 입력해주세요.")

    def run(self):
        if not self.login_manager.login():
            return
        while True:
            self.print_menu()
            num = self.input_menu()

            if num == 1:
                가위바위보+묵찌빠_game = Game()
    
