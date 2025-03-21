class TicTacToe:
    """
    A class representing a Tic-Tac-Toe game.
    """

    def __init__(self):
        """
        Initializes the game board and sets the initial player.
        """
        self.board = [" " for _ in range(9)]  # Represents the 3x3 board
        self.current_player = "X"  # X starts the game

    def print_board(self):
        """
        Prints the current state of the Tic-Tac-Toe board to the console.
        """
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6:
                print("---+---+---")

    def is_valid_move(self, position):
        """
        Checks if a move to the given position is valid.

        Args:
            position (int): The position to check (1-9).

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return 1 <= position <= 9 and self.board[position - 1] == " "

    def make_move(self, position):
        """
        Makes a move for the current player at the given position.

        Args:
            position (int): The position to make the move (1-9).
        """
        if self.is_valid_move(position):
            self.board[position - 1] = self.current_player
            return True
        else:
            return False

    def check_winner(self):
        """
        Checks if there is a winner.

        Returns:
            str: The winning player ("X" or "O") or None if no winner.
        """
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]               # Diagonals
        ]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return self.board[combo[0]]

        return None

    def is_board_full(self):
        """
        Checks if the board is full (no more moves possible).

        Returns:
            bool: True if the board is full, False otherwise.
        """
        return " " not in self.board

    def switch_player(self):
        """
        Switches the current player to the other player.
        """
        self.current_player = "O" if self.current_player == "X" else "X"

    def play_game(self):
        """
        The main game loop.
        """
        print("Welcome to Tic-Tac-Toe!")
        self.print_board()

        while True:
            print(f"Player {self.current_player}, it's your turn.")
            try:
                position = int(input("Enter a position (1-9): "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
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
    game.play_game()