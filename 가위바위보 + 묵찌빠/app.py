# app.py

from game.mukjjippa_game import start_game
from game.ranking_board import show_record


def run():

    while True:

        print("\n===== 메뉴 =====")
        print("1. 게임 시작")
        print("2. 전적 보기")
        print("3. 게임 종료")

        try:
            menu = int(input("메뉴 선택: "))

            if menu == 1:
                start_game()

            elif menu == 2:
                show_record()

            elif menu == 3:
                print("게임 종료")
                break

            else:
                print("1~3 사이 입력")

        except:
            print("숫자를 입력하세요.")