class ConnectFour:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.board = [[' ' for _ in range(self.columns)] for _ in range(self.rows)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|' + '|'.join(row) + '|')
        print(' ' + '-'.join(['-' for _ in range(self.columns)]))

    def drop_piece(self, column):
        for row in reversed(range(self.rows)):
            if self.board[row][column] == ' ':
                self.board[row][column] = self.current_player
                return row
        return -1

    def check_winner(self, row, column):
        # Check horizontal
        for c in range(max(0, column - 3), min(self.columns, column + 4)):
            if all(self.board[row][c + i] == self.current_player for i in range(4) if 0 <= c + i < self.columns):
                return True

        # Check vertical
        if row <= self.rows - 4:
            if all(self.board[row + i][column] == self.current_player for i in range(4)):
                return True

        # Check diagonal (bottom-left to top-right)
        for d in range(-3, 1):
            if 0 <= row + d < self.rows and 0 <= column + d < self.columns and \
               all(self.board[row + d + i][column + d + i] == self.current_player for i in range(4) if 0 <= row + d + i < self.rows and 0 <= column + d + i < self.columns):
                return True

        # Check diagonal (top-left to bottom-right)
        for d in range(-3, 1):
            if 0 <= row - d < self.rows and 0 <= column + d < self.columns and \
               all(self.board[row - d + i][column + d + i] == self.current_player for i in range(4) if 0 <= row - d + i < self.rows and 0 <= column + d + i < self.columns):
                return True

        return False

    def play(self):
        while True:
            self.print_board()
            try:
                column = int(input(f"Player {self.current_player}, choose a column (0-{self.columns - 1}): "))
                if column < 0 or column >= self.columns:
                    print("Invalid column. Try again.")
                    continue
                
                row = self.drop_piece(column)
                if row == -1:
                    print("Column is full. Try again.")
                    continue
                
                if self.check_winner(row, column):
                    self.print_board()
                    print(f"Player {self.current_player} wins!")
                    break
                
                self.current_player = 'O' if self.current_player == 'X' else 'X'

            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    game = ConnectFour()
    game.play()