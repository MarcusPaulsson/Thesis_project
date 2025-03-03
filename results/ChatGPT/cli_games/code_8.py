import numpy as np

ROWS = 6
COLUMNS = 7
CONNECT = 4

class ConnectFour:
    def __init__(self):
        self.board = np.zeros((ROWS, COLUMNS), int)
        self.game_over = False
        self.turn = 0

    def drop_piece(self, column):
        for row in range(ROWS-1, -1, -1):
            if self.board[row][column] == 0:
                self.board[row][column] = 1 if self.turn == 0 else 2
                break

    def is_valid_location(self, column):
        return self.board[ROWS-1][column] == 0

    def winning_move(self):
        for row in range(ROWS):
            for col in range(COLUMNS - 3):
                if self.check_line(row, col, 0, 1):
                    return True
        for row in range(ROWS - 3):
            for col in range(COLUMNS):
                if self.check_line(row, col, 1, 0):
                    return True
        for row in range(ROWS - 3):
            for col in range(COLUMNS - 3):
                if self.check_line(row, col, 1, 1):
                    return True
        for row in range(3, ROWS):
            for col in range(COLUMNS - 3):
                if self.check_line(row, col, -1, 1):
                    return True
        return False

    def check_line(self, row, col, row_step, col_step):
        piece = self.board[row][col]
        if piece == 0:
            return False
        for i in range(1, CONNECT):
            if self.board[row + i * row_step][col + i * col_step] != piece:
                return False
        return True

    def print_board(self):
        print(np.flip(self.board, 0))

    def play(self):
        while not self.game_over:
            self.print_board()
            column = int(input(f"Player {self.turn + 1}, choose a column (0-6): "))
            if self.is_valid_location(column):
                self.drop_piece(column)
                if self.winning_move():
                    self.print_board()
                    print(f"Player {self.turn + 1} wins!")
                    self.game_over = True
                self.turn ^= 1
            else:
                print("Column full or invalid. Try again.")

if __name__ == '__main__':
    game = ConnectFour()
    game.play()