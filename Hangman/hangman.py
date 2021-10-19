from random import choice
ascii_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                 "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
words = ["bank", "belt", "bomb", "bird", "boom"]


def hangman_greeting():
    print("HANGMAN.")
    print("The game will be available soon.")


# def simplified_version():
#     word = "train"
#     are_we_playing = True
#     while are_we_playing:
#         answer = (input("Guess the word: > ")).lower()
#         if answer == word:
#             print("You survived!")
#             are_we_playing = False
#         else:
#             print("You lost!")
#             continue
#
#
# def advanced_version():
#     are_we_playing = True
#     word = choice(words)
#
#     while are_we_playing:
#         # print(word)
#         answer = (input("Guess the word: > ")).lower()
#         if answer == word:
#             print("You survived!")
#             are_we_playing = False
#         else:
#             print("You lost!")
#             continue
#
#
# def version_with_tips():
#     are_we_playing = True
#     word = choice(words)
#     tips = word[:3] + ("-" * (len(word)-3))
#     # print(tips)
#     while are_we_playing:
#         # print(word)
#         answer = (input("Guess the word " + tips + ": > ")).lower()
#         if answer == word:
#             print("You survived!")
#             are_we_playing = False
#         else:
#             print("You lost!")
#             continue
#
#
# def hangman_version1():
#     attempts = 8
#     word = choice(words)
#     print(word)
#     guessed_word = '-' * len(word)
#     used = []
#     while attempts > 0 and guessed_word != word:
#         print("attempts", attempts)
#         answer = (input("Guess the word " + guessed_word + ": > ")).lower()
#         used.append(answer)
#         if answer in word:
#             guessed_letter = ''
#             for letter in range(len(word)):
#                 if answer == word[letter]:
#                     guessed_letter += answer
#                 else:
#                     guessed_letter += guessed_word[letter]
#             guessed_word = guessed_letter
#             attempts -= 1
#         else:
#             # print("That letter doesn't appear in the word")
#             attempts -= 1
#     if attempts <= 0:
#         print("You lost!")
#     else:
#         print("You survived!")
#
#
# def hangman_version2():
#     attempts = 8
#     word = choice(words)
#     print(word)
#     guessed_word = '-' * len(word)
#     used = []
#     while attempts > 0 and guessed_word != word:
#         print("attempts", attempts)
#
#         answer = (input("Guess the word " + guessed_word + ": > ")).lower()
#         while answer in used:
#             if answer in word:
#                 attempts -= 1
#                 print("No improvements")
#                 # print("You\'ve already guessed this letter.")
#                 break
#             else:
#                 break
#         used.append(answer)
#         if answer in word:
#             guessed_letter = ''
#             for letter in range(len(word)):
#                 if answer == word[letter]:
#                     guessed_letter += answer
#                 else:
#                     guessed_letter += guessed_word[letter]
#             guessed_word = guessed_letter
#
#         else:
#             print("That letter doesn't appear in the word")
#             if answer in used:
#                 attempts -= 1
#     if attempts <= 0:
#         print("You lost!")
#     else:
#         print(guessed_word + "\nYou guessed the word!")
#
#         print("You survived!")


def hangman_version3():
    attempts = 8
    word = choice(words)
    print(word)
    guessed_part_word = '-' * len(word)
    used = []
    while attempts > 0 and guessed_part_word != word:
        print("attempts", attempts)
        answer = correct_input_user(guessed_part_word, used)
        if answer in used:
            continue
        used.append(answer)

        if answer in word:
            guessed_part_word = \
                add_correct_letter_to_guessed_part_word(answer, word, guessed_part_word)
        else:
            print("That letter doesn't appear in the word")
            if answer in used:
                attempts -= 1
    determines_result_game(attempts, guessed_part_word)


def checking_input_english_letters(letter, possible_letters, word):
    while letter not in possible_letters:
        print("Please enter a lowercase English letter.")
        letter = input("Guess the word " + word + ": > ")


def duplicate_letter_check(letter, used):
    if letter in used:
        print("You've already guessed this letter.")


def correct_input_user(guessed_part_word, used):
    answer = input("Guess the word " + guessed_part_word + ": > ")
    if len(answer) > 1:
        print("You should input a single letter.")
    checking_correct_length_input(answer, guessed_part_word)
    checking_input_english_letters(answer, ascii_letters, guessed_part_word)
    duplicate_letter_check(answer, used)
    return answer


def checking_correct_length_input(input_users, word):
    while len(input_users) > 1:
        print("You should input a single letter.")
        input_users = input("Guess the word " + word + ": > ")


def add_correct_letter_to_guessed_part_word(answer, word, guessed_part_word):
    guessed_letter = ''
    for letter in range(len(word)):
        if answer == word[letter]:
            guessed_letter += answer
        else:
            guessed_letter += guessed_part_word[letter]
    return guessed_letter


def determines_result_game(attempts, guessed_part_word):
    if attempts <= 0:
        print("You lost!")
    else:
        print(guessed_part_word + "\nYou guessed the word!")

        print("You survived!")


hangman_greeting()


# simplified_version()


# advanced_version()


# version_with_tips()


# hangman_version1()


# hangman_version2()


hangman_version3()
