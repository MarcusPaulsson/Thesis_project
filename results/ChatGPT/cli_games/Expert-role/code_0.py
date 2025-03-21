class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_player = 'X'

    def print_board(self):
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("---------")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("---------")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        return False

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
            (0, 4, 8), (2, 4, 6)               # diagonal
        ]
        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                return self.board[a]
        return None

    def is_full(self):
        return ' ' not in self.board

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        while True:
            self.print_board()
            try:
                position = int(input(f"Player {self.current_player}, enter your move (0-8): "))
                if position < 0 or position > 8:
                    print("Invalid position. Please try again.")
                    continue
                if not self.make_move(position):
                    print("Position already taken. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 8.")
                continue

            winner = self.check_winner()
            if winner:
                self.print_board()
                print(f"Player {winner} wins!")
                break
            if self.is_full():
                self.print_board()
                print("It's a draw!")
                break

            self.switch_player()


if __name__ == "__main__":
    game = TicTacToe()
    game.play()