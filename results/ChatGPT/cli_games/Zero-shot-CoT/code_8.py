class ConnectFour:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.board = [[' ' for _ in range(self.columns)] for _ in range(self.rows)]
        self.current_player = 'X'

    def print_board(self):
        print("\n".join(['|'.join(row) for row in self.board]))
        print('-' * (self.columns * 2 - 1))

    def drop_piece(self, column):
        for row in reversed(range(self.rows)):
            if self.board[row][column] == ' ':
                self.board[row][column] = self.current_player
                return True
        return False

    def is_winner(self):
        for row in range(self.rows):
            for col in range(self.columns):
                if self.check_win(row, col):
                    return True
        return False

    def check_win(self, row, col):
        if self.board[row][col] != self.current_player:
            return False
        # Check horizontal
        if col + 3 < self.columns and all(self.board[row][col + i] == self.current_player for i in range(4)):
            return True
        # Check vertical
        if row + 3 < self.rows and all(self.board[row + i][col] == self.current_player for i in range(4)):
            return True
        # Check diagonal /
        if row + 3 < self.rows and col - 3 >= 0 and all(self.board[row + i][col - i] == self.current_player for i in range(4)):
            return True
        # Check diagonal \
        if row + 3 < self.rows and col + 3 < self.columns and all(self.board[row + i][col + i] == self.current_player for i in range(4)):
            return True
        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        while True:
            self.print_board()
            column = int(input(f"Player {self.current_player}, choose a column (0-{self.columns-1}): "))
            if 0 <= column < self.columns and self.drop_piece(column):
                if self.is_winner():
                    self.print_board()
                    print(f"Player {self.current_player} wins!")
                    break
                self.switch_player()
            else:
                print("Column full or invalid. Try again.")

if __name__ == "__main__":
    game = ConnectFour()
    game.play()