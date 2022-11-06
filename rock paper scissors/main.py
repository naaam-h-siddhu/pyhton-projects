import random


options = ['s', 'p', 'r']


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
     or (player == 'p' and opponent == 'r'):
        return True


def play():
    user = input("choose 'r' as Rock 's' as scissor and 'p' as Paper").lower()
    computer = random.choice(options)
    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return "you won"
    return f"you lost computer choose {computer}"


print(play())
