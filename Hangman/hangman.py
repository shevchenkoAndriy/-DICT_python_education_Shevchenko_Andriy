import random
words = ["education", "stranger", "magazine", "adaptation"]


def hangman_greeting():
    print("HANGMAN.")
    print("The game will be available soon.")


def simplified_version():
    word = "train"
    are_we_playing = True
    while are_we_playing:
        answer = (input("Guess the word: > ")).lower()
        if answer == word:
            print("You survived!")
            are_we_playing = False
        else:
            print("You lost!")
            continue


def advanced_version():
    are_we_playing = True
    word = random.choice(words)

    while are_we_playing:
        # print(word)
        answer = (input("Guess the word: > ")).lower()
        if answer == word:
            print("You survived!")
            are_we_playing = False
        else:
            print("You lost!")
            continue


hangman_greeting()

# simplified_version()

advanced_version()

