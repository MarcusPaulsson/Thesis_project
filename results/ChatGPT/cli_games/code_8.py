import numpy as np

class ConnectFour:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.board = np.zeros((self.rows, self.columns), dtype=int)
        self.current_player = 1

    def print_board(self):
        print(np.flip(self.board, 0))

    def drop_piece(self, column):
        for row in range(self.rows):
            if self.board[row][column] == 0:
                self.board[row][column] = self.current_player
                return True
        return False

    def is_winning_move(self):
        # Check horizontal locations for win
        for c in range(self.columns - 3):
            for r in range(self.rows):
                if (self.board[r][c] == self.current_player and
                        self.board[r][c + 1] == self.current_player and
                        self.board[r][c + 2] == self.current_player and
                        self.board[r][c + 3] == self.current_player):
                    return True

        # Check vertical locations for win
        for c in range(self.columns):
            for r in range(self.rows - 3):
                if (self.board[r][c] == self.current_player and
                        self.board[r + 1][c] == self.current_player and
                        self.board[r + 2][c] == self.current_player and
                        self.board[r + 3][c] == self.current_player):
                    return True

        # Check positively sloped diagonals
        for c in range(self.columns - 3):
            for r in range(self.rows - 3):
                if (self.board[r][c] == self.current_player and
                        self.board[r + 1][c + 1] == self.current_player and
                        self.board[r + 2][c + 2] == self.current_player and
                        self.board[r + 3][c + 3] == self.current_player):
                    return True

        # Check negatively sloped diagonals
        for c in range(self.columns - 3):
            for r in range(3, self.rows):
                if (self.board[r][c] == self.current_player and
                        self.board[r - 1][c + 1] == self.current_player and
                        self.board[r - 2][c + 2] == self.current_player and
                        self.board[r - 3][c + 3] == self.current_player):
                    return True

        return False

    def play_game(self):
        game_over = False
        while not game_over:
            self.print_board()
            column = int(input(f"Player {self.current_player}, choose a column (0-{self.columns-1}): "))
            if column < 0 or column >= self.columns or not self.drop_piece(column):
                print("Invalid move. Try again.")
                continue
            
            if self.is_winning_move():
                self.print_board()
                print(f"Player {self.current_player} wins!")
                game_over = True
            else:
                self.current_player = 2 if self.current_player == 1 else 1

if __name__ == "__main__":
    game = ConnectFour()
    game.play_game()