import random


def simple_version():
    user_choice = correct_input_action("Your choice > ", ("rock", "paper", "scissors"))
    win_move = search_win_move(user_choice)
    print(f"Sorry, but the computer chose {win_move}")


def search_win_move(move):
    win_move = None
    if move == "rock":
        win_move = "paper"
    elif move == "paper":
        win_move = "scissors"
    elif move == "scissors":
        win_move = "rock"
    return win_move


def correct_input_action(string, valid_commands):
    user_input = input(string)
    while user_input not in valid_commands:
        print("Command is not valid")
        user_input = input(string)
    return user_input


def simple_menu():
    user_choice = correct_input_action("Your choice > ", ("rock", "paper", "scissors", "exit"))

    if user_choice == "exit":
        print("Bye")
        return

    computer_choice = random.choice(("rock", "paper", "scissors"))
    computer_win_if = search_win_move(user_choice)
    user_win_if = search_win_move(computer_choice)

    if computer_win_if == computer_choice:
        print(f"Sorry, but the computer chose {computer_choice}")

    elif user_win_if == user_choice:
        print(f"Well done. The computer chose {computer_choice} and failed")

    simple_menu()


"""step-1"""
# simple_version()
"""step-2"""
simple_menu()
