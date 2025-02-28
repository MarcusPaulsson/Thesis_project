import numpy as np

ROWS = 6
COLUMNS = 7
EMPTY = 0
PLAYER1 = 1
PLAYER2 = 2

class ConnectFour:
    def __init__(self):
        self.board = np.zeros((ROWS, COLUMNS), dtype=int)
        self.current_player = PLAYER1

    def print_board(self):
        print(np.flip(self.board, 0))

    def drop_piece(self, column):
        for row in range(ROWS):
            if self.board[row][column] == EMPTY:
                self.board[row][column] = self.current_player
                return row
        return -1

    def is_valid_location(self, column):
        return self.board[ROWS - 1][column] == EMPTY

    def winning_move(self, row, column):
        # Check horizontal
        for c in range(COLUMNS - 3):
            if (self.board[row][c] == self.current_player and
                self.board[row][c + 1] == self.current_player and
                self.board[row][c + 2] == self.current_player and
                self.board[row][c + 3] == self.current_player):
                return True

        # Check vertical
        for r in range(ROWS - 3):
            if (self.board[r][column] == self.current_player and
                self.board[r + 1][column] == self.current_player and
                self.board[r + 2][column] == self.current_player and
                self.board[r + 3][column] == self.current_player):
                return True

        # Check positively sloped diagonals
        for r in range(ROWS - 3):
            for c in range(COLUMNS - 3):
                if (self.board[r][c] == self.current_player and
                    self.board[r + 1][c + 1] == self.current_player and
                    self.board[r + 2][c + 2] == self.current_player and
                    self.board[r + 3][c + 3] == self.current_player):
                    return True

        # Check negatively sloped diagonals
        for r in range(3, ROWS):
            for c in range(COLUMNS - 3):
                if (self.board[r][c] == self.current_player and
                    self.board[r - 1][c + 1] == self.current_player and
                    self.board[r - 2][c + 2] == self.current_player and
                    self.board[r - 3][c + 3] == self.current_player):
                    return True

        return False

    def switch_player(self):
        self.current_player = PLAYER1 if self.current_player == PLAYER2 else PLAYER2

    def play(self):
        game_over = False
        while not game_over:
            self.print_board()
            column = int(input(f"Player {self.current_player}, select a column (0-{COLUMNS - 1}): "))
            
            if column < 0 or column >= COLUMNS or not self.is_valid_location(column):
                print("Invalid column. Try again.")
                continue

            row = self.drop_piece(column)

            if self.winning_move(row, column):
                self.print_board()
                print(f"Player {self.current_player} wins!")
                game_over = True
            else:
                self.switch_player()

if __name__ == "__main__":
    game = ConnectFour()
    game.play()