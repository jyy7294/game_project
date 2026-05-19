# mukjjippa_game.py

import random

from game.config import CHOICES
from game.ranking_board import add_win, add_loss


def get_computer_choice():
    return random.choice(CHOICES)


def check_rps(user, computer):
    if user == computer:
        return "draw"

    if (
        (user == "가위" and computer == "보")
        or (user == "바위" and computer == "가위")
        or (user == "보" and computer == "바위")
    ):
        return "user"

    return "computer"


def start_game():

    print("[가위바위보 시작]")

    # 공격권 정하기
    while True:

        user = input("가위/바위/보 입력: ")

        if user not in CHOICES:
            print("잘못 입력했습니다.")
            continue

        computer = get_computer_choice()

        print(f"컴퓨터: {computer}")

        result = check_rps(user, computer)

        if result == "draw":
            print("비겼습니다. 다시!")
            continue

        attacker = result

        if attacker == "user":
            print("사용자가 공격권을 가져갑니다.")

        else:
            print("컴퓨터가 공격권을 가져갑니다.")

        break

    # 묵찌빠 시작
    print("\n[묵찌빠 시작]")

    while True:

        print(f"현재 공격자: {attacker}")

        user = input("가위/바위/보 입력: ")

        if user not in CHOICES:
            print("잘못 입력했습니다.")
            continue

        computer = get_computer_choice()

        print(f"컴퓨터: {computer}")

        # 같은 것 냈을 때
        if user == computer:

            if attacker == "user":
                print("사용자 승리!")
                add_win()

            else:
                print("컴퓨터 승리!")
                add_loss()

            break

        # 공격권 변경
        result = check_rps(user, computer)

        if result == "draw":
            continue

        attacker = result