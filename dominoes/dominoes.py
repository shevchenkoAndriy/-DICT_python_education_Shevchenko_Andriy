from random import sample


class Dominoes:
    def __init__(self):
        self.game_dice = [[a, b] for a in range(7) for b in range(a, 7)]
        self.player_pieces = None
        self.computer_pieces = None
        self.stock_pieces = None
        self.status = None
        self.domino_snake = []

    def init_bot_dice(self):
        not_selected = list(filter(lambda x: x not in self.player_pieces, self.game_dice))
        return sample(not_selected, k=7)

    def make_move(self, move):
        status = self.status
        if status == "Player":
            self.player_pieces.remove(move)

        elif status == "Computer":
            self.computer_pieces.remove(move)

        self.make_action(move, status)

        self.change_player()

    def determine_action(self, move, first, last):
        is_universal = (move[0] == first and move[1] == last)\
                       or (move[0] == last and move[1] == first)

        if len(self.domino_snake) < 1:
            return
        if is_universal:
            return "universal"
        elif move[0] == self.domino_snake[len(self.domino_snake) - 1][1]:
            return "append"
        elif move[1] == self.domino_snake[len(self.domino_snake) - 1][1]:
            return "append"
        elif move[0] == self.domino_snake[0][0]:
            return "insert"
        elif move[1] == self.domino_snake[0][0]:
            return "insert"

    def change_player(self):
        if self.status == "Computer":
            self.status = "Player"

        elif self.status == "Player":
            self.status = "Computer"

    def make_action(self, move, user):
        if len(self.domino_snake) != 0:
            first_number_snake = self.domino_snake[0][0]
            last_number_snake = self.domino_snake[len(self.domino_snake) - 1][1]
            action = self.determine_action(move, first_number_snake, last_number_snake)
        else:
            self.domino_snake.append(move)
            return

        if action == "universal" and user != "Computer":
            action = self.correct_input_action('Add ahead press enter or '
                                               'input "back" to add back > ',
                                               ("", "back"))
        elif action == "universal" and user == "computer":
            action = "append"

        if action == "append" and move[1] == last_number_snake:
            move = list(reversed(move))

        if action == "append":
            self.domino_snake.append(move)

        if action == "insert" and move[0] == first_number_snake:
            move = list(reversed(move))

        if action == "insert":
            self.domino_snake.insert(0, move)

    def who_starts_game(self):
        max_double_player, pieces_player = self.get_max_double(self.player_pieces)
        max_double_bot, pieces_bot = self.get_max_double(self.computer_pieces)
        if not max_double_bot:
            ...
        elif not max_double_player:
            ...
        elif max_double_bot > max_double_player:
            return "Computer", pieces_bot
        elif max_double_player > max_double_bot:
            return "Player", pieces_player

    def show_filed(self):
        print(f"""Stock pieces: {self.stock_pieces}
Computer pieces: {self.computer_pieces}

Player pieces: {self.player_pieces}

Domino snake: {self.domino_snake[:14] if len(self.domino_snake) >= 14 else self.domino_snake}
              {self.domino_snake[14:] if len(self.domino_snake) > 14 else ""}              
Status: {self.status}""")

    def domino_interface(self):
        print(f"""{"=" * 70}
Stock size: {len(self.stock_pieces)}
Computer pieces: {len(self.computer_pieces)}
""")
        if len(self.domino_snake) > 6:
            print(*self.domino_snake[:3], "...", *self.domino_snake[-3:], sep="")
        else:
            print(*self.domino_snake, sep="")
        print("\nYour pieces:")
        pieces_range = range(len(self.player_pieces))
        valid_commands = self.search_move_option(self.player_pieces)
        for item, i in zip(self.player_pieces, pieces_range):
            if i + 1 in valid_commands:
                print(f"{i + 1}: {item}")
            else:
                print(f"{i+1}:{item}")
        if self.status == "Player":
            print("\nStatus: It's your turn to make a move. Enter your command.")
        elif self.status == "Computer":
            print("\nStatus: Computer is about to make a move. Press Enter to continue...")

    def start_game(self):
        if self.status == "Player":
            self.user_action()
        elif self.status == "Computer":
            self.computer_action()

    def go_to_shop(self, user_dice):
        user_pieces = user_dice
        valid_commands = None
        while len(self.stock_pieces) != 0:
            print(f"{self.status}: Oops, i'm going to the market")
            self.correct_enter_input("Please press Enter to continue > ")
            new_dice = self.get_dice()
            user_pieces.append(new_dice)
            valid_commands = self.search_move_option(user_pieces)

            if valid_commands:
                break

            print(f"Stock size: {len(self.stock_pieces)}\n", "Fail, try again", sep="")

        return valid_commands

    def get_dice(self):
        new_dice, *_ = sample(self.stock_pieces, k=1)
        self.stock_pieces.remove(new_dice)
        return new_dice

    def is_have_choice(self, user_pieces):
        valid_commands = self.search_move_option(user_pieces)
        if len(valid_commands) == 0:
            valid_commands = self.go_to_shop(user_pieces)
            self.domino_interface()
            return valid_commands
        else:
            return valid_commands

    def user_action(self):
        valid_commands = self.is_have_choice(self.player_pieces)
        if not valid_commands:
            print("Pass")
            self.change_player()
            return
        user_input = self.correctly_input_command("Player > ", valid_commands)
        self.make_move(self.player_pieces[user_input - 1])

    def computer_action(self):
        self.correct_enter_input("> ")
        valid_commands = self.is_have_choice(self.computer_pieces)
        if not valid_commands:
            print("Pass")
            self.change_player()
            return

        self.make_move(self.computer_pieces[valid_commands[0] - 1])

    def search_move_option(self, user_pieces):
        possible_moves = []
        necessary = self.find_necessary_pieces()
        possible_pieces = list(filter(lambda x: self.find(x, necessary), user_pieces))
        for i in range(len(user_pieces)):
            if user_pieces[i] in possible_pieces:
                possible_moves.append(i+1)

        return possible_moves

    def find_necessary_pieces(self):
        domino_snake = self.domino_snake
        necessary = []
        if len(domino_snake) == 1:
            necessary.append(domino_snake[0][0])
        else:
            necessary.append(domino_snake[0][0])
            necessary.append(domino_snake[len(domino_snake) - 1][1])
        return necessary

    def correctly_integer_input(self, string):
        user_input = input(string)
        try:
            int(user_input)
        except ValueError:
            print("Please input integer number")
            self.correctly_integer_input(string)
        else:
            return int(user_input)

    def correctly_input_command(self, string, valid_commands):
        user_input = self.correctly_integer_input(string)
        while user_input not in valid_commands:
            print("Command is not valid")
            user_input = self.correctly_integer_input(string)
        return user_input

    def step_1(self):
        self.init_game()
        self.show_filed()

    def step_2(self):
        self.init_game()
        self.domino_interface()

    def step_3(self):
        self.init_game()
        need_stop = False
        while not need_stop:
            self.domino_interface()
            self.start_game()
            need_stop = self.is_need_break()

        self.status = need_stop
        self.show_filed()

    def is_need_break(self):
        fish = self.it_is_fish()
        if len(self.player_pieces) == 0:
            return "The game is over. You won!"
        elif len(self.computer_pieces) == 0:
            return "The game is over. Computer won!"
        elif fish:
            return "Fish"

    def it_is_fish(self):
        pieces = self.find_necessary_pieces()
        user_option = list(filter(lambda x: self.find(x, pieces), self.player_pieces))
        computer_option = list(filter(lambda x: self.find(x, pieces), self.computer_pieces))
        stock_option = list(filter(lambda x: self.find(x, pieces), self.stock_pieces))
        print(f"u: {user_option} c: {computer_option}, store: {stock_option}")
        if len(user_option) == 0 and len(computer_option) == 0 and len(stock_option) == 0:
            return True

    def init_game(self):
        self.player_pieces = sample(self.game_dice, k=7)
        self.computer_pieces = self.init_bot_dice()
        used_pieces = [*self.player_pieces, *self.computer_pieces]
        self.stock_pieces = list(filter(lambda x: x not in used_pieces, self.game_dice))
        result = self.who_starts_game()
        if result:
            name, dice = result
            self.status = name
            self.make_move(dice)
        else:
            self.init_game()

    @staticmethod
    def get_max_double(player):
        doubles_player = list(filter(lambda x: x[0] == x[1], player))
        list_numbers = list(map(lambda x: x[0], doubles_player))
        max_number = None
        if list_numbers:
            max_number = max(list_numbers)
        return max_number, [max_number, max_number]

    @staticmethod
    def correct_enter_input(string):
        user_input = input(string)
        while user_input != "":
            user_input = input()

    @staticmethod
    def find(user, necessary):
        return user[0] in necessary or user[1] in necessary

    @staticmethod
    def correct_input_action(string, valid_commands):
        user_input = input(string)
        while user_input not in valid_commands:
            print("Command is not valid")
            user_input = input(string)
        if user_input == "":
            return "append"
        if user_input == "back":
            return "insert"
        return user_input


dominoes = Dominoes()
# dominoes.step_1()
# dominoes.step_2()
dominoes.step_3()
