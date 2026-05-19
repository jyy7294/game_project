# ranking_board.py

wins = 0
losses = 0
total = 0


def add_win():
    global wins, total
    wins += 1
    total += 1


def add_loss():
    global losses, total
    losses += 1
    total += 1


def show_record():
    print("---- 전적 ----")
    print(f"총 게임 수: {total}")
    print(f"승리: {wins}")
    print(f"패배: {losses}")