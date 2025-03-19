class ConnectFour:
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * (self.cols * 2 - 1))
        print(' '.join(str(i) for i in range(self.cols)))

    def drop_piece(self, col):
        for row in reversed(range(self.rows)):
            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player
                return True
        return False

    def is_winning_move(self, row, col):
        return (self.check_direction(row, col, 1, 0) or  # horizontal
                self.check_direction(row, col, 0, 1) or  # vertical
                self.check_direction(row, col, 1, 1) or  # diagonal /
                self.check_direction(row, col, 1, -1))   # diagonal \

    def check_direction(self, row, col, delta_row, delta_col):
        count = 0
        for direction in [1, -1]:
            r, c = row, col
            while 0 <= r < self.rows and 0 <= c < self.cols and self.board[r][c] == self.current_player:
                count += 1
                if count == 4:
                    return True
                r += delta_row * direction
                c += delta_col * direction
        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        while True:
            self.print_board()
            col = input(f"Player {self.current_player}, choose a column (0-{self.cols-1}): ")
            if not col.isdigit() or not (0 <= int(col) < self.cols):
                print("Invalid input. Please try again.")
                continue

            col = int(col)
            if not self.drop_piece(col):
                print("Column full. Try another one.")
                continue

            row = next(r for r in reversed(range(self.rows)) if self.board[r][col] == self.current_player)

            if self.is_winning_move(row, col):
                self.print_board()
                print(f"Player {self.current_player} wins!")
                break

            self.switch_player()


if __name__ == "__main__":
    game = ConnectFour()
    game.play()