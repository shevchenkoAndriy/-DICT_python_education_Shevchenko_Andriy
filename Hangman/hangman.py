word = "train"
def hangman_greeting():
    print("HANGMAN.")
    print("The game will be available soon.")


def simplified_version():
    print("HANGMAN.")
    print("Guess the word: >", word)
    answer = (input("> ")).lower()
    if answer == word:
        print("You survived!")
    else:
        print("You lost!")


hangman_greeting()
simplified_version()
