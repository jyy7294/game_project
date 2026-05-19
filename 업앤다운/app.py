from .config import ID, PWD, MAX_LOGIN_ATTEMPTS
from .login_manager import LoginManager
from .ranking_board import RankingBoard
from .updown_game import UpDownGame


class App:
    def __init__(self):
        self.login_manager = LoginManager(ID, PWD ,MAX_LOGIN_ATTEMPTS)
        self.ranking_board = RankingBoard()
        self.id = "admin"

    def print_menu(self):
        print()
        print("1. 게임 시작 2. 랭킹 보기 3. 게임 종료")

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
                game = UpDownGame()
                nickname, count = game.play()
                self.ranking_board.add_record(nickname, count)

            elif num == 2:
                self.ranking_board.show_ranking()

            elif num == 3:
                print("프로그램을 종료합니다.")
                break

            else:
                print("잘못된 메뉴입니다.")