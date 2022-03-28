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


"""step-1"""
simple_version()
