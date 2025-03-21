class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Represents the 3x3 board as a list
        self.current_player = 'X'  # Start with player X
        self.winner = None
        self.game_over = False

    def print_board(self):
        """Prints the current state of the board to the console."""
        print("-------------")
        for i in range(3):
            print(f"| {self.board[i*3]} | {self.board[i*3 + 1]} | {self.board[i*3 + 2]} |")
            print("-------------")

    def is_valid_move(self, position):
        """Checks if the given position is a valid move (within range and empty)."""
        return 0 <= position < 9 and self.board[position] == ' '

    def make_move(self, position):
        """Places the current player's mark on the board at the given position."""
        if self.is_valid_move(position):
            self.board[position] = self.current_player
            self.check_winner()
            self.switch_player()
            return True
        else:
            return False

    def check_winner(self):
        """Checks if there is a winner after the last move."""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]               # Diagonals
        ]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                self.winner = self.current_player
                self.game_over = True
                return

        if ' ' not in self.board:  # Check for a tie
            self.game_over = True
            self.winner = None  # No winner, it's a tie

    def switch_player(self):
        """Switches the current player to the other player."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play_game(self):
        """Main game loop."""
        print("Welcome to Tic-Tac-Toe!")
        self.print_board()

        while not self.game_over:
            try:
                position = int(input(f"Player {self.current_player}, enter your move (0-8): "))
                if self.make_move(position):
                    self.print_board()
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 8.")

        if self.winner:
            print(f"Player {self.winner} wins!")
        else:
            print("It's a tie!")


if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()