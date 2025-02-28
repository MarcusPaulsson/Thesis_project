class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_player = 'X'

    def print_board(self):
        print('---------')
        for i in range(3):
            print(f'| {" | ".join(self.board[i * 3:(i + 1) * 3])} |')
            print('---------')

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

    def is_board_full(self):
        return ' ' not in self.board

    def play(self):
        while True:
            self.print_board()
            move = input(f"Player {self.current_player}, enter your move (1-9): ")
            try:
                move = int(move) - 1
                if move < 0 or move > 8 or self.board[move] != ' ':
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue

            self.board[move] = self.current_player
            winner = self.check_winner()

            if winner:
                self.print_board()
                print(f"Congratulations! Player {winner} wins!")
                break
            elif self.is_board_full():
                self.print_board()
                print("It's a draw!")
                break

            self.current_player = 'O' if self.current_player == 'X' else 'X'


if __name__ == "__main__":
    game = TicTacToe()
    game.play()