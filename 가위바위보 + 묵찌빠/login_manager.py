# login_manager.py

from game.config import CORRECT_ID, CORRECT_PW


def login():
    chance = 3

    while chance > 0:
        user_id = input("ID를 입력하세요: ")
        user_pw = input("PASSWORD를 입력하세요: ")

        if user_id == CORRECT_ID and user_pw == CORRECT_PW:
            print("로그인 성공!")
            return True

        else:
            chance -= 1
            print(f"로그인 실패! 남은 횟수: {chance}")

    print("3회 실패로 프로그램 종료")
    return False