class TicTacToe:
    """
    Represents a Tic-Tac-Toe game.
    """

    def __init__(self):
        """
        Initializes the game board and sets the current player to 'X'.
        """
        self.board = [" " for _ in range(9)]  # Represents the 3x3 board
        self.current_player = "X"
        self.game_over = False

    def print_board(self):
        """
        Prints the current state of the game board to the console.
        """
        print("-------------")
        for i in range(3):
            print(f"| {self.board[i*3]} | {self.board[i*3 + 1]} | {self.board[i*3 + 2]} |")
            print("-------------")

    def is_valid_move(self, position):
        """
        Checks if the given position is a valid move.

        Args:
            position (int): The position to check (1-9).

        Returns:
            bool: True if the position is valid, False otherwise.
        """
        return 1 <= position <= 9 and self.board[position - 1] == " "

    def make_move(self, position):
        """
        Makes a move on the board for the current player.

        Args:
            position (int): The position to make the move (1-9).
        """
        self.board[position - 1] = self.current_player

    def check_win(self):
        """
        Checks if the current player has won the game.

        Returns:
            bool: True if the current player has won, False otherwise.
        """
        # Check rows
        for i in range(3):
            if self.board[i*3] == self.board[i*3 + 1] == self.board[i*3 + 2] != " ":
                return True

        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != " ":
                return True

        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return True
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return True

        return False

    def check_draw(self):
        """
        Checks if the game is a draw.

        Returns:
            bool: True if the game is a draw, False otherwise.
        """
        return " " not in self.board

    def switch_player(self):
        """
        Switches the current player to the other player.
        """
        self.current_player = "O" if self.current_player == "X" else "X"

    def play(self):
        """
        Plays the Tic-Tac-Toe game.
        """
        while not self.game_over:
            self.print_board()
            print(f"Player {self.current_player}, it's your turn.")

            try:
                position = int(input("Enter a position (1-9): "))
                if self.is_valid_move(position):
                    self.make_move(position)
                    if self.check_win():
                        self.print_board()
                        print(f"Player {self.current_player} wins!")
                        self.game_over = True
                    elif self.check_draw():
                        self.print_board()
                        print("It's a draw!")
                        self.game_over = True
                    else:
                        self.switch_player()
                else:
                    print("Invalid move. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    game = TicTacToe()
    game.play()