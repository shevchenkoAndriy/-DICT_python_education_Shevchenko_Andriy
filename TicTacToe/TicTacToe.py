class TicTacToe:

    def __init__(self):
        self.board = []
        self.test_string = [["X", 0, 0], ["X", 0, "X"], ["X", "X", 0]]

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append(' ')
            self.board.append(row)
        return self.board

    @staticmethod
    def print_board(board):
        print(f'''
+=+=+=+=+=+=+=+
    |{board[0][0]} {board[0][1]} {board[0][2]}|
    |{board[1][0]} {board[1][1]} {board[1][2]}|
    |{board[2][0]} {board[2][1]} {board[2][2]}|
+=+=+=+=+=+=+=+
        ''')


st1 = TicTacToe()
st1.print_board(st1.test_string)
