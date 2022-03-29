import random


class RockPaperScissors:

    def __init__(self):
        self.rating = None
        self.name = None

    def menu(self):
        self.init_game()
        self.start_game()

    def start_game(self):
        user_choice = self.correct_input_action("Your choice > ", ("rock", "paper", "scissors", "exit", "rating"))

        if user_choice == "exit":
            self.save_rating()
            print("Bye")
            return

        if user_choice == "rating":
            self.show_raring()
            self.start_game()
            return

        computer_choice = random.choice(("rock", "paper", "scissors"))
        computer_win_if = self.search_win_move(user_choice)
        user_win_if = self.search_win_move(computer_choice)
        if computer_choice == user_choice:
            self.rating += 50
            print("There is draw")
        elif computer_win_if == computer_choice:
            print(f"Sorry, but the computer chose {computer_choice}")

        elif user_win_if == user_choice:
            self.rating += 100
            print(f"Well done. The computer chose {computer_choice} and failed")

        self.start_game()

    def save_rating(self):
        with open("rating.txt", "w") as f:
            f.write(f"{self.name} {self.rating}")

    def init_game(self):
        self.name = input("Please input your name > ").capitalize()
        print(f"Hello {self.name}")
        prev_rating = self.read_rating_file()
        if not prev_rating:
            self.rating = 0
            return

        prev_name, prev_value = prev_rating

        if prev_name == self.name:
            self.rating = int(prev_value)
        else:
            self.rating = 0

    def show_raring(self):
        print(f"Your rating: {self.rating}")

    @staticmethod
    def search_win_move(move):
        win_move = None
        if move == "rock":
            win_move = "paper"
        elif move == "paper":
            win_move = "scissors"
        elif move == "scissors":
            win_move = "rock"
        return win_move

    @staticmethod
    def correct_input_action(string, valid_commands):
        user_input = input(string)
        while user_input not in valid_commands:
            print("Command is not valid")
            user_input = input(string)
        return user_input

    @staticmethod
    def read_rating_file():
        with open("rating.txt", "r") as f:
            rating = f.read()
            if not rating:
                return

            return rating.split(" ")


rps = RockPaperScissors()
rps.menu()
