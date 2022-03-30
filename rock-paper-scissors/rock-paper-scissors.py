import random


class RockPaperScissors:
    all_options = ['fire', 'scissors', 'human', 'tree', 'wolf',
                   'sponge', 'paper', 'air', 'water', 'dragon',
                   'devil', 'lightning', 'gun', 'rock', 'snake']

    map_options = {
        'rock': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
        'fire': ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper'],
        'scissors': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
        'snake': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
        'human': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
        'tree': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
        'wolf': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'],
        'sponge': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
        'paper': ['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock'],
        'air': ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
        'water': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
        'dragon': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
        'devil': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
        'lightning': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
        'gun': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf'],
    }

    def __init__(self):
        self.rating = None
        self.name = None
        self.bot_options = None
        self.selected_options = ["exit", "rating"]

    def menu(self):
        self.init_game()
        self.start_game()

    def start_game(self):
        user_choice = self.correct_input_action("Your choice > ", self.selected_options)

        if user_choice == "exit":
            self.save_rating()
            print("Bye")
            return

        if user_choice == "rating":
            self.show_raring()
            self.start_game()
            return

        computer_choice = random.choice(self.bot_options)
        bot_beats_it = self.map_options.get(computer_choice)
        user_beats_it = self.map_options.get(user_choice)

        if user_choice in bot_beats_it:
            print(f"Sorry, but the computer chose {computer_choice}")

        elif computer_choice in user_beats_it:
            self.rating += 100
            print(f"Well done. The computer chose {computer_choice} and failed")

        else:
            self.rating += 50
            print("There is draw")

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

        self.select_options()

    def select_options(self):
        selected_options = self.correct_select_option()
        print("Here is your option:")
        print(*selected_options)
        self.selected_options = [*self.selected_options, *selected_options]
        self.bot_options = selected_options

    def correct_select_option(self):
        selected_options = input("Please input options > ")

        if selected_options == "":
            return ["rock", "paper", "scissors"]

        selected_options = selected_options.split(",")
        selected_options = list(filter(lambda x: x in self.all_options, selected_options))

        if len(selected_options) < 3:
            self.correct_select_option()
            return

        return selected_options

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
