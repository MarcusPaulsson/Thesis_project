class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_player = 'X'  # Start with player X
        self.winner = None

    def print_board(self):
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("--+---+--")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("--+---+--")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

    def make_move(self, position):
        if self.board[position] == ' ' and self.winner is None:
            self.board[position] = self.current_player
            self.check_winner()
            self.switch_player()
        else:
            print("Invalid move. Try again.")

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
            (0, 4, 8), (2, 4, 6)               # Diagonal
        ]
        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                self.winner = self.board[a]
                print(f"Player {self.winner} wins!")
                return
        if ' ' not in self.board:
            print("It's a draw!")
            self.winner = 'Draw'

    def play(self):
        while self.winner is None:
            self.print_board()
            try:
                move = int(input(f"Player {self.current_player}, enter your move (0-8): "))
                if move < 0 or move > 8:
                    print("Invalid input. Please enter a number between 0 and 8.")
                    continue
                self.make_move(move)
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    game = TicTacToe()
    game.play()