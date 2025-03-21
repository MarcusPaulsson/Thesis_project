class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.current_player = "X"
        self.winner = None
        self.game_over = False

    def print_board(self):
        """Prints the current board state."""
        print("-------------")
        for i in range(3):
            print(f"| {self.board[i*3]} | {self.board[i*3+1]} | {self.board[i*3+2]} |")
            print("-------------")

    def is_valid_move(self, position):
        """Checks if the given position is a valid move."""
        if not isinstance(position, int):
            return False
        if not (0 <= position <= 8):
            return False
        if self.board[position] != " ":
            return False
        return True

    def make_move(self, position):
        """Makes a move on the board."""
        if self.is_valid_move(position):
            self.board[position] = self.current_player
            self.check_winner()
            self.check_draw()
            self.switch_player()
        else:
            print("Invalid move. Try again.")

    def switch_player(self):
        """Switches the current player."""
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        """Checks if there is a winner."""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]               # Diagonals
        ]

        for combo in winning_combinations:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] != " ":
                self.winner = self.board[a]
                self.game_over = True
                return

    def check_draw(self):
        """Checks if the game is a draw."""
        if " " not in self.board and not self.winner:
            self.game_over = True

    def play(self):
        """Main game loop."""
        while not self.game_over:
            self.print_board()
            try:
                position = int(input(f"Player {self.current_player}, enter your move (0-8): "))
                self.make_move(position)
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 8.")

        self.print_board()
        if self.winner:
            print(f"Player {self.winner} wins!")
        else:
            print("It's a draw!")

if __name__ == "__main__":
    game = TicTacToe()
    game.play()