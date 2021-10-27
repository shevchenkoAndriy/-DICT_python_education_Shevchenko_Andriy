from random import choice
ascii_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                 "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
words = ["bank", "belt", "bomb", "bird", "boom"]
command = ["exit", "play"]


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
            attempts -= 1
            print("That letter doesn't appear in the word")

    determines_result_game(attempts, guessed_part_word)
    hangman_menu()


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


def hangman_menu():
    user_input = input('Type \"play\" to play the game, \"exit\" to quit: > ').lower()
    print("HANGMAN")
    if user_input == "play":
        hangman_version3()
    elif user_input == "exit":
        print("exit")
    else:
        return debug_error_menu()


def debug_error_menu():
    hangman_menu()


hangman_menu()
