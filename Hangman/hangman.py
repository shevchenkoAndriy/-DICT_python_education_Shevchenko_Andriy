from random import choice
words = ["bank", "belt", "bomb", "bird", "boom"]

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
    word = choice(words)

    while are_we_playing:
        # print(word)
        answer = (input("Guess the word: > ")).lower()
        if answer == word:
            print("You survived!")
            are_we_playing = False
        else:
            print("You lost!")
            continue


def version_with_tips():
    are_we_playing = True
    word = choice(words)
    tips = word[:3] + ("-" * (len(word)-3))
    # print(tips)
    while are_we_playing:
        # print(word)
        answer = (input("Guess the word " + tips + ": > ")).lower()
        if answer == word:
            print("You survived!")
            are_we_playing = False
        else:
            print("You lost!")
            continue


def hangman_version1():
    attempts = 8
    word = choice(words)
    print(word)
    guessed_word = '-' * len(word)
    used_leter = []
    while attempts > 0 and guessed_word != word:
        print("attempts", attempts)
        answer = (input("Guess the word " + guessed_word + ": > ")).lower()
        # while answer in used_leter:
        #     print("You\'ve already guessed this letter.")
        #     break
        # answer = (input("Guess the word " + guessed_word + ": > ")).lower()
        used_leter.append(answer)
        if answer in word:
            guessed_letter = ''
            for letter in range(len(word)):
                if answer == word[letter]:
                    guessed_letter += answer
                else:
                    guessed_letter += guessed_word[letter]
            guessed_word = guessed_letter
            attempts -= 1
        else:
            # print("That letter doesn't appear in the word")
            attempts -= 1
    if attempts <= 0:
        print("You lost!")
    else:
        print("You survived!")




hangman_greeting()

# simplified_version()

# advanced_version()

# version_with_tips()
# answer = (input("Guess the word " + guessed_word + ": > ")).lower()
# answer = (input("Guess the word " + word_answer + ": > ")).lower()
# print("That letter doesn't appear in the word")
# print("attempts", attempts)
# print("You lost!")
hangman_version1()