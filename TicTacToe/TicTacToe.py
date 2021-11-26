import itertools


class TicTacToe:
    init_list = []
    command_move = "1 1", "1 2", "1 3",\
                   "2 1", "2 2", "2 3",\
                   "3 1", "3 2", "3 3"

    def __init__(self):
        self.board = []
        self.test_string = [["X", 0, 0], ["X", 0, "X"], ["X", "X", 0]]
        self.available_symbols = ("X", "0", "_")

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('_')
            self.board.append(row)
        return self.board

    def input_cells(self):
        user_input = list(input("Enter cells: > ").upper())
        if len(user_input) != 9:
            print("Can't build a board, you need 9 characters")
            return
        has_valid_input = self.correctly_input_cells(user_input)
        if has_valid_input:
            field = [user_input[:3],
                     user_input[3:6],
                     user_input[6:9]]
            self.print_board(field)
            self.board = field
            return field
        # self.input_cells()

    def board_analysis(self):
        game_board = self.input_cells()
        if not game_board:
            while not game_board:
                self.board_analysis()
        exception = self.check_impossible(game_board)
        if not game_board:
            self.board_analysis()
        win = self.check_winner(game_board)
        if win == "Impossible" or exception:
            print("Impossible")
        elif win == "XXX":
            print("X wins")
        elif win == "000":
            print("0 wins")
        elif not exception and "_" in itertools.chain.from_iterable(game_board):
            print('Game not finished')
        else:
            print("Draw")

    def move_player(self, player):
        moves = self.correct_input_move("Enter the coordinates: ", self.command_move)
        coordinates = (list(map(self.replace_num, moves.split(" "))))
        self.board[coordinates[0]][coordinates[1]] = player

        if self.board[coordinates[0]][coordinates[1]] != "_":
            print("This cell is occupied! Choose another one!")
        self.print_board(self.board)
        self.move_player("X")

    @staticmethod
    def replace_num(move):
        if move == "1":
            move = 0
        elif move == "2":
            move = 1
        elif move == "3":
            move = 2
        return move

    @staticmethod
    def correct_input_move(help_string, valid_move):
        move = input(help_string)
        while move not in valid_move:
            if not move.replace(" ", "").isnumeric():
                print("You should enter numbers!")
                move = input(help_string)
                continue
            elif move not in valid_move:
                print("Coordinates should be from 1 to 3!")
                move = input(help_string)
                continue
        return move

    @staticmethod
    def check_impossible(board):
        board_list = list(itertools.chain.from_iterable(board))
        count_x = board_list.count("X")
        count_0 = board_list.count("0")
        min_count = min(count_0, count_x)
        max_count = max(count_0, count_x)
        if (max_count - 1) <= min_count:
            return False
        elif (max_count - 1) > min_count:
            return True

    @staticmethod
    def correctly_input_cells(user_input):
        error_input = list(filter(lambda x: x not in ("X", "0", "_"), user_input))
        if error_input:
            print("invalid symbol(s):", *{*error_input})
        else:
            return True

    @staticmethod
    def print_board(board):
        print(f'''
+=+=+=+=+=+=+=+
    |{board[0][0]} {board[0][1]} {board[0][2]}|
    |{board[1][0]} {board[1][1]} {board[1][2]}|
    |{board[2][0]} {board[2][1]} {board[2][2]}|
+=+=+=+=+=+=+=+
        ''')

    @staticmethod
    def correctly_input(symbol, valid_symbols):
        symbol = symbol.upper()
        while symbol not in valid_symbols:
            print(f'Invalid symbol({symbol}).'
                  f'Please enter only: 0 _ X')
            symbol = input("> ")
        return symbol

    @staticmethod
    def check_winner(board):
        win_combo = [f"{board[0][0]}{board[0][1]}{board[0][2]}",
                     f"{board[1][0]}{board[1][1]}{board[1][2]}",
                     f"{board[2][0]}{board[2][1]}{board[2][2]}",
                     f"{board[0][0]}{board[1][0]}{board[2][0]}",
                     f"{board[0][1]}{board[1][1]}{board[2][1]}",
                     f"{board[0][2]}{board[1][2]}{board[2][2]}",
                     f"{board[2][0]}{board[1][1]}{board[0][2]}",
                     f"{board[0][0]}{board[1][1]}{board[2][2]}",
                     ]
        used_combo = []
        for combo in win_combo:
            if combo == "XXX":
                used_combo.append(combo)
            elif combo == "000":
                used_combo.append(combo)
        if len(used_combo) >= 1:
            winner, *arg = used_combo
        else:
            winner = None
        if len(used_combo) == 1 and winner == "XXX":
            return winner
        elif len(used_combo) == 1 and winner == "000":
            return winner
        elif len(used_combo) > 1:
            return "Impossible"


# st1 = TicTacToe()
# st1.print_board(st1.test_string)


# st2 = TicTacToe()
# st2.input_cells()


# st3 = TicTacToe()
# st3.board_analysis()
"""
   000xx0x0x - 0 wins; xx00xxx00 - draw;
   00x0x0x__ - X wins; xxx000xxx - impossible;
   x0x_x_x00 - X wins; 0x0_xx00x - not finished
   
"""
"""
   00_xx0x0x ; xx0__xx00 
   __x0x0x__ ; _xx0__xxx 
   _0x_x_x00 ; 0x0_x_0_x 

"""

st4 = TicTacToe()
st4.board_analysis()
st4.move_player("X")
