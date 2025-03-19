class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def print_board(self):
        """Prints the current state of the board."""
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6:
                print("---+---+---")

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
        """Makes a move at the given position."""
        if self.is_valid_move(position):
            self.board[position] = self.current_player
            return True
        else:
            return False

    def check_winner(self):
        """Checks if there is a winner."""
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != " ":
                return self.board[i]

        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != " ":
                return self.board[i]

        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return self.board[2]

        return None

    def is_board_full(self):
        """Checks if the board is full."""
        return " " not in self.board

    def switch_player(self):
        """Switches the current player."""
        self.current_player = "O" if self.current_player == "X" else "X"

    def play(self):
        """Main game loop."""
        print("Welcome to Tic-Tac-Toe!")
        self.print_board()

        while True:
            print(f"Player {self.current_player}, it's your turn.")
            try:
                position = int(input("Enter the position (0-8): "))
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 8.")
                continue

            if self.make_move(position):
                self.print_board()
                winner = self.check_winner()

                if winner:
                    print(f"Player {winner} wins!")
                    break
                elif self.is_board_full():
                    print("It's a draw!")
                    break
                else:
                    self.switch_player()
            else:
                print("Invalid move. Please try again.")


if __name__ == "__main__":
    game = TicTacToe()
    game.play()