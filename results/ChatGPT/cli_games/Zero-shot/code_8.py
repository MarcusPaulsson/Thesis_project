class ConnectFour:
    def __init__(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 13)
        print('0 1 2 3 4 5 6')

    def drop_piece(self, column):
        for row in reversed(range(6)):
            if self.board[row][column] == ' ':
                self.board[row][column] = self.current_player
                return True
        return False

    def is_winner(self):
        # Check horizontal, vertical, and diagonal
        for row in range(6):
            for col in range(7):
                if self.board[row][col] == self.current_player:
                    if self.check_direction(row, col, 1, 0) or \
                       self.check_direction(row, col, 0, 1) or \
                       self.check_direction(row, col, 1, 1) or \
                       self.check_direction(row, col, 1, -1):
                        return True
        return False

    def check_direction(self, row, col, delta_row, delta_col):
        count = 0
        for _ in range(4):
            if 0 <= row < 6 and 0 <= col < 7 and self.board[row][col] == self.current_player:
                count += 1
                if count == 4:
                    return True
            else:
                break
            row += delta_row
            col += delta_col
        return False

    def is_full(self):
        return all(self.board[0][col] != ' ' for col in range(7))

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        while True:
            self.print_board()
            column = input(f"Player {self.current_player}, choose a column (0-6): ")
            if not column.isdigit() or not 0 <= int(column) <= 6:
                print("Invalid input. Please choose a column between 0 and 6.")
                continue
            column = int(column)
            if not self.drop_piece(column):
                print("Column full! Try a different column.")
                continue
            if self.is_winner():
                self.print_board()
                print(f"Player {self.current_player} wins!")
                break
            if self.is_full():
                self.print_board()
                print("It's a tie!")
                break
            self.switch_player()

if __name__ == "__main__":
    game = ConnectFour()
    game.play()