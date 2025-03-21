class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_player = 'X'

    def print_board(self):
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("--+---+--")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("--+---+--")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
            (0, 4, 8), (2, 4, 6)               # diagonal
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]
        if ' ' not in self.board:
            return 'Draw'
        return None

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            winner = self.check_winner()
            if winner:
                self.print_board()
                if winner == 'Draw':
                    print("It's a draw!")
                else:
                    print(f"Player {winner} wins!")
                return True
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return False
        else:
            print("Invalid move. Try again.")
            return False

    def play_game(self):
        while True:
            self.print_board()
            try:
                move = int(input(f"Player {self.current_player}, enter your move (1-9): ")) - 1
                if move < 0 or move > 8:
                    print("Invalid move. Enter a number between 1 and 9.")
                    continue
                if self.make_move(move):
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()