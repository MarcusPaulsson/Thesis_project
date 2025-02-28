class ConnectFour:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.board = [[' ' for _ in range(self.columns)] for _ in range(self.rows)]
        self.current_player = 'X'

    def display_board(self):
        print("\n".join(["|".join(row) for row in self.board]))
        print("-" * (self.columns * 2 - 1))
        print(" ".join(str(i) for i in range(self.columns)))

    def drop_piece(self, column):
        for row in reversed(self.board):
            if row[column] == ' ':
                row[column] = self.current_player
                return True
        return False

    def is_winner(self):
        # Check horizontal, vertical, and diagonal
        for r in range(self.rows):
            for c in range(self.columns - 3):
                if self.board[r][c] == self.current_player and \
                   self.board[r][c + 1] == self.current_player and \
                   self.board[r][c + 2] == self.current_player and \
                   self.board[r][c + 3] == self.current_player:
                    return True

        for r in range(self.rows - 3):
            for c in range(self.columns):
                if self.board[r][c] == self.current_player and \
                   self.board[r + 1][c] == self.current_player and \
                   self.board[r + 2][c] == self.current_player and \
                   self.board[r + 3][c] == self.current_player:
                    return True

        for r in range(self.rows - 3):
            for c in range(self.columns - 3):
                if self.board[r][c] == self.current_player and \
                   self.board[r + 1][c + 1] == self.current_player and \
                   self.board[r + 2][c + 2] == self.current_player and \
                   self.board[r + 3][c + 3] == self.current_player:
                    return True

        for r in range(3, self.rows):
            for c in range(self.columns - 3):
                if self.board[r][c] == self.current_player and \
                   self.board[r - 1][c + 1] == self.current_player and \
                   self.board[r - 2][c + 2] == self.current_player and \
                   self.board[r - 3][c + 3] == self.current_player:
                    return True

        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        while True:
            self.display_board()
            column = int(input(f"Player {self.current_player}, choose a column (0-{self.columns - 1}): "))
            if 0 <= column < self.columns and self.drop_piece(column):
                if self.is_winner():
                    self.display_board()
                    print(f"Player {self.current_player} wins!")
                    break
                self.switch_player()
            else:
                print("Invalid move. Try again.")


if __name__ == "__main__":
    game = ConnectFour()
    game.play()