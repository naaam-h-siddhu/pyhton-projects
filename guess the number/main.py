import random


def human_guess(x):
    random_num = random.randint(1, x)
    let = 0
    count = 0
    while let != random_num:
        let = int(input(f"guess the number between 1 and {x}:"))
        if let > random_num:
            print("sorry, guess again too high")
            count += 1
        elif let < random_num:
            print("sorry, guess again too low")
            count += 1
    print(f"yay, you have guessed the number {random_num} and your score is {count}")


def comp_guess(x):
    low = 1
    high = x
    feed = ''
    guess = 0
    while feed != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feed = input(f"Is {guess} too high(H) , too low(L), or correct(C) ").lower()
        if feed == 'h':
            high = guess-1
        elif feed == 'l':
            low = guess+1
    print(f"yay! The computer guessed your number {guess}, correctly")


comp_guess(100)
