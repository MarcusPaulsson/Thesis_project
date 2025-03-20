class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # Represents the board as a list
        self.current_player = "X"
        self.winner = None
        self.game_over = False

    def print_board(self):
        """Prints the current state of the board."""
        print("-------------")
        for i in range(3):
            print(f"| {self.board[i * 3]} | {self.board[i * 3 + 1]} | {self.board[i * 3 + 2]} |")
            print("-------------")

    def is_valid_move(self, move):
        """Checks if a move is valid (within range and the cell is empty)."""
        if not move.isdigit():
            return False
        move = int(move)
        if 0 <= move <= 8 and self.board[move] == " ":
            return True
        return False

    def make_move(self, move):
        """Makes a move on the board."""
        move = int(move)
        self.board[move] = self.current_player
        self.check_winner()
        self.check_draw()
        self.switch_player()

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
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]
                    and self.board[combo[0]] != " "):
                self.winner = self.current_player
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
            move = input(f"Player {self.current_player}, enter your move (0-8): ")

            if self.is_valid_move(move):
                self.make_move(move)
            else:
                print("Invalid move. Try again.")

        self.print_board()  # Print the final board

        if self.winner:
            print(f"Player {self.winner} wins!")
        else:
            print("It's a draw!")


if __name__ == "__main__":
    game = TicTacToe()
    game.play()