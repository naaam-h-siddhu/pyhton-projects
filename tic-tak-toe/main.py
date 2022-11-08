from player import player_1, player_2


def print_board(crosss, zeroo):
    a = 'X' if crosss[0] else ('O' if zeroo[0] else '0')
    b = 'X' if crosss[1] else ('O' if zeroo[1] else '1')
    c = 'X' if crosss[2] else ('O' if zeroo[2] else '2')
    d = 'X' if crosss[3] else ('O' if zeroo[3] else '3')
    e = 'X' if crosss[4] else ('O' if zeroo[4] else '4')
    f = 'X' if crosss[5] else ('O' if zeroo[5] else '5')
    g = 'X' if crosss[6] else ('O' if zeroo[6] else '6')
    h = 'X' if crosss[7] else ('O' if zeroo[7] else '7')
    i = 'X' if crosss[8] else ('O' if zeroo[8] else '8')
    print(f"{a} | {b} | {c}")
    print(f"--|---|--")
    print(f"{d} | {e} | {f}")
    print(f"--|---|--")
    print(f"{g} | {h} | {i}")


def add(a, b, c):
    return a + b + c


def check_win(cross, zero):
    conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [2, 4, 6], [4, 1, 7], [8, 2, 5], [0, 4, 8]]
    for it in conditions:
        if add(cross[it[0]], cross[it[1]], cross[it[2]]) == 3:
            print(f"{player_1} won the game")
            return 1
        if add(zero[it[0]], zero[it[1]], zero[it[2]]) == 3:
            print(f"{player_2} won the game")
            return 0
    return 2


cross = [0, 0, 0, 0, 0, 0, 0, 0, 0]
zero = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = 1
print("WELCOME TO TIC TAK TOE")

counter = 0
while True:
    print_board(cross, zero)
    counter += 1
    if turn == 1:
        print(f"{player_1}'s turn: ")
        move = int(input("enter the place for (X): "))
        cross[move] = 1

    else:
        print(f"{player_2}'s turn: ")
        move = int(input("enter the place for (O): "))
        zero[move] = 1

    check_winner = check_win(cross, zero)
    if check_winner != 2:
        break
    if counter == 9:
        print("<--------Game Tie!!!!-------->>")
        break
    turn = 1 - turn
