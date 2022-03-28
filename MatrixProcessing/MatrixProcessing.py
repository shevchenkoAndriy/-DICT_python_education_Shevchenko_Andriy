class MatrixProcessing:

    def __init__(self):
        ...

    def menu(self):
        user_choice = self.correctly_input_command("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
0. Exit
Your choice: > """, ("1", "2", "3", "0", "4"))
        if user_choice == "1":
            self.add_matrices()
        elif user_choice == "2":
            self.multiplication_by_constant()
        elif user_choice == "3":
            self.multiply_matrices()
        elif user_choice == "4":
            self.matrix_transposition()
        elif user_choice == "0":
            return

        user_choice = self.correctly_input_command("Continue? [yes] / [no] > ", ("yes", "no"))
        if user_choice == "yes":
            self.menu()
        else:
            return

    def multiply_matrices(self):
        matrix1, rows1, columns1 = self.create_matrix(" first ")
        matrix2, rows2, columns2 = self.create_matrix(" second ")
        while rows1 != columns2:
            print("The number of columns"
                  " of the first matrix must"
                  " be equal to the number of rows of"
                  " the second matrix")
            matrix2, rows2, columns2 = self.create_matrix(" second ")
        result = []
        for i in range(rows1):
            row = []
            for j in range(columns2):
                num = 0
                for k in range(columns1):
                    num += matrix1[i][k] * matrix2[k][j]
                row.append(num)
            result.append(row)
        self.show_result(result)

    def multiplication_by_constant(self):
        constant = self.correct_float_input("Enter constant: > ")
        matrix, *_ = self.create_matrix()
        result = []
        for rows in matrix:
            columns = []
            for column in rows:
                columns.append(column * constant)
            result.append(columns)
        self.show_result(result)

    def add_matrices(self):
        matrix1, *shape1 = self.create_matrix(" first ")
        matrix2, *shape2 = self.create_matrix(" second ")
        while shape1 != shape2:
            print(f"Perform addition possible only for a matrix,"
                  f" unique numbers of rows and columns.")
            matrix2, *shape2 = self.create_matrix(" second ")

        result = []
        for m1, m2 in zip(matrix1, matrix2):
            column = []
            for a, b in zip(m1, m2):
                value = a + b
                column.append(value)
            result.append(column)
        self.show_result(result)

    def create_matrix(self, turn=" "):
        rows, columns = self.correct_input_size(f"Enter size of{turn}matrix: > ")
        matrix = self.correct_input_matrix(rows, columns)
        return matrix, rows, columns

    def correct_input_matrix(self, rows, columns):
        matrix = []
        for i in range(1, rows + 1):
            row = self.correct_input_columns(f"Row number {i}: > ", columns)
            matrix.append(row)
        return matrix

    def matrix_transposition(self):
        matrix, *_ = self.create_matrix()
        result = []
        for i in range(len(matrix[0])):
            rows = []
            for row in matrix:
                rows.append(row[i])
            result.append(rows)

        self.show_result(result)

    @staticmethod
    def show_result(matrix):
        print("The result is:")
        for rows in matrix:
            results = []
            for column in rows:
                value = round(column, 2)
                if int(column) == column:
                    value = int(column)
                results.append(value)
            print(*results, sep="  ")

    @staticmethod
    def correct_input_columns(string, number_rows):
        user_input = input(string)
        while True:
            user_input = user_input.split(" ")
            if len(user_input) != number_rows:
                print("Incorrect row filling")
                user_input = input(string)
            try:
                list(map(lambda x: float(x), user_input))
            except ValueError:
                print("Incorrect row filling")
                user_input = input(string)
                continue
            else:
                user_input = list(map(lambda x: float(x), user_input))
                break
        return user_input

    @staticmethod
    def valid_shape(matrix):
        shape = set()
        rows = len(matrix)
        for column in matrix:
            shape.add(len(column))
        if len(shape) == 1:
            return rows, *shape
        else:
            print("ERROR")

    @staticmethod
    def correctly_input_command(string, command):
        user_input = input(string)
        while user_input not in command:
            print("please input correctly command")
            user_input = input(string)
        return user_input

    @staticmethod
    def correct_input_size(string):
        user_input = input(string)

        while True:
            user_input = user_input.split(" ")
            if len(user_input) != 2:
                print("Please input correctly size")
                user_input = input(string)
            try:
                list(map(lambda x: int(x), user_input))
            except ValueError:
                print("Please input correctly size")
                user_input = input(string)
                continue
            else:
                user_input = list(map(lambda x: int(x), user_input))
                break

        return user_input

    @staticmethod
    def correct_float_input(string):
        user_input = input(string)
        while True:
            try:
                float(user_input)
            except ValueError:
                print("Incorrect format")
                user_input = input(string)
                continue
            else:
                break
        return float(user_input)


mxp = MatrixProcessing()
mxp.menu()
