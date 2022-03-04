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
            self.status = "Computer"
            self.player_pieces.remove(move)

        elif status == "Computer":
            self.status = "Player"
            self.computer_pieces.remove(move)

        self.domino_snake.append(move)

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
Domino snake: {self.domino_snake}
Status: {self.status}""")

    def domino_interface(self):
        print(f"""{"=" * 70}
Stock size: {len(self.stock_pieces)}
Computer pieces: {len(self.computer_pieces)}
""")
        print(*self.domino_snake, sep="")
        print("\nYour pieces:")
        pieces_range = range(len(self.player_pieces))
        for item, i in zip(self.player_pieces, pieces_range):
            print(f"{i+1}: {item}")
        if self.status == "Player":
            print("\nStatus: It's your turn to make a move. Enter your command.")
        elif self.status == "Computer":
            print("\nStatus: Computer is about to make a move. Press Enter to continue...")

    def step_1(self):
        self.init_game()
        self.show_filed()

    def step_2(self):
        self.init_game()
        self.domino_interface()

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


dominoes = Dominoes()
# dominoes.step_1()
dominoes.step_2()
