class TicTacToe:
    init_list = []

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
            print("Error:\nCan't build a board, you need 9 characters")
        valid_input = self.correctly_input_cells(user_input)
        if valid_input and user_input != 9:
            field = [user_input[:3],
                     user_input[3:6],
                     user_input[6:9]]
            self.print_board(field)
            return
        self.input_cells()

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

    # @staticmethod
    # def correct(items):
    #     if items not in ("X", "0", "_"):
    #         return True
    #     else:
    #         return False


# st1 = TicTacToe()
# st1.print_board(st1.test_string)


st2 = TicTacToe()
st2.input_cells()
