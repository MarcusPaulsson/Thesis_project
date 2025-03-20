class ConnectFour:
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.current_player = 'X'
        self.game_over = False

    def print_board(self):
        for row in self.board:
            print('|' + '|'.join(row) + '|')
        print('+' + '+'.join(['-'] * self.cols) + '+')
        print(' ' + ' '.join(map(str, range(1, self.cols + 1))))

    def is_valid_move(self, col):
        return 0 <= col < self.cols and self.board[0][col] == ' '

    def drop_piece(self, col):
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player
                return row

    def check_win(self, row, col):
        # Check horizontal
        count = 0
        for c in range(max(0, col - 3), min(self.cols, col + 4)):
            if self.board[row][c] == self.current_player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

        # Check vertical
        count = 0
        for r in range(max(0, row - 3), min(self.rows, row + 4)):
            if self.board[r][col] == self.current_player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

        # Check positive diagonal
        count = 0
        for i in range(-3, 4):
            r = row + i
            c = col + i
            if 0 <= r < self.rows and 0 <= c < self.cols:
                if self.board[r][c] == self.current_player:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0

        # Check negative diagonal
        count = 0
        for i in range(-3, 4):
            r = row + i
            c = col - i
            if 0 <= r < self.rows and 0 <= c < self.cols:
                if self.board[r][c] == self.current_player:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0

        return False

    def check_draw(self):
        for col in range(self.cols):
            if self.board[0][col] == ' ':
                return False
        return True

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play_game(self):
        while not self.game_over:
            self.print_board()
            print(f"Player {self.current_player}, it's your turn.")

            try:
                col = int(input(f"Enter a column (1-{self.cols}): ")) - 1
                if not self.is_valid_move(col):
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            row = self.drop_piece(col)

            if self.check_win(row, col):
                self.print_board()
                print(f"Player {self.current_player} wins!")
                self.game_over = True
            elif self.check_draw():
                self.print_board()
                print("It's a draw!")
                self.game_over = True
            else:
                self.switch_player()

if __name__ == "__main__":
    game = ConnectFour()
    game.play_game()