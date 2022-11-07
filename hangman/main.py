import random
from words import words


def convert_string(string):
    list1 = []
    list1[:0] = string
    return list1


def hangman():
    word = random.choice(words)
    chance = 10
    guessed = ''
    valid_entry = convert_string('abcdefghijklmnopqrstuvwxyz')

    while len(word) > 0:
        main_word = ""

        for letter in word:
            if letter in guessed:
                main_word = main_word + letter
            else:
                main_word = main_word +"_ "
        if main_word == word:
            print(f"{main_word} you won!!!!")
            break

        print(f"guess the word {main_word}")
        guess = input()

        if guess in valid_entry:
            valid_entry.remove(guess)
            guessed = guessed + guess
        else:
            print("enter valid character(repeated input)")
            continue
        if guess not in word:
            chance -= 1
            if chance == 9:
                print("9 chances are left!!!!")
                print("______________________")

            if chance == 8:
                print("8 chances are left!!!!")
                print("______________________")
                print("         O            ")
            if chance == 7:
                print("7 chances are left!!!!")
                print("______________________")
                print("         O            ")
                print("         |            ")
            if chance == 6:
                print("6 chances are left!!!!")
                print("______________________")
                print("         O            ")
                print("         |            ")
                print("        /             ")
            if chance == 5:
                print("5 chances are left!!!!")
                print("______________________")
                print("         O            ")
                print("         |            ")
                print("        / \           ")
            if chance == 4:
                print("4 chances are left!!!!")
                print("______________________")
                print("        \O            ")
                print("         |            ")
                print("        / \           ")
            if chance == 3:
                print("3 chances are left!!!!")
                print("______________________")
                print("        \O/           ")
                print("         |            ")
                print("        / \           ")
            if chance == 2:
                print("2 chances are left!!!!")
                print("______________________")
                print("        \O/_          ")
                print("         |            ")
                print("        / \           ")
            if chance == 1:
                print("Last chance left, a poor man gonna die")
                print("______________________")
                print("        \o/_|          ")
                print("         |            ")
                print("        / \           ")
            if chance == 0:
                print(f"you loose!! word was {word}")
                print("u let a black poor person die")
                print("______________________")
                print("         o_|          ")
                print("        /|\           ")
                print("        / \           ")
                break


name = input("Enter your name => ").upper()
print(f"WELCOME! {name} TO")
print("---HANGMAN---")
print("RULE : you have to guess the word and you have only 10 attempts")
hangman()