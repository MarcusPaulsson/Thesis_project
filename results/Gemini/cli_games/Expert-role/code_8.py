class ConnectFour:
    """
    A class to represent the Connect Four game.
    """

    def __init__(self, rows=6, cols=7):
        """
        Initializes the Connect Four game board.

        Args:
            rows (int): The number of rows in the board (default: 6).
            cols (int): The number of columns in the board (default: 7).
        """
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.current_player = 'X'  # Player X starts
        self.game_over = False
        self.winner = None

    def print_board(self):
        """
        Prints the current state of the Connect Four board to the console.
        """
        for row in range(self.rows):
            print('|' + '|'.join(self.board[row]) + '|')
        print('+' + '+'.join(['-'] * self.cols) + '+')
        print(' ' + ' '.join(str(i + 1) for i in range(self.cols)))  # Column numbers

    def drop_piece(self, col):
        """
        Drops a piece into the specified column.

        Args:
            col (int): The column to drop the piece into (0-indexed).

        Returns:
            bool: True if the piece was successfully dropped, False otherwise
                  (e.g., column is full).
        """
        if col < 0 or col >= self.cols:
            print("Invalid column. Please choose a column between 1 and", self.cols)
            return False

        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player
                return True  # Piece successfully dropped

        print("Column", col + 1, "is full.  Choose a different column.")
        return False  # Column is full

    def check_win(self):
        """
        Checks if the current player has won the game.

        Returns:
            bool: True if the current player has won, False otherwise.
        """
        # Check horizontal
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if (self.board[row][col] == self.current_player and
                        self.board[row][col + 1] == self.current_player and
                        self.board[row][col + 2] == self.current_player and
                        self.board[row][col + 3] == self.current_player):
                    return True

        # Check vertical
        for row in range(self.rows - 3):
            for col in range(self.cols):
                if (self.board[row][col] == self.current_player and
                        self.board[row + 1][col] == self.current_player and
                        self.board[row + 2][col] == self.current_player and
                        self.board[row + 3][col] == self.current_player):
                    return True

        # Check positive diagonal
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if (self.board[row][col] == self.current_player and
                        self.board[row + 1][col + 1] == self.current_player and
                        self.board[row + 2][col + 2] == self.current_player and
                        self.board[row + 3][col + 3] == self.current_player):
                    return True

        # Check negative diagonal
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                if (self.board[row][col] == self.current_player and
                        self.board[row - 1][col + 1] == self.current_player and
                        self.board[row - 2][col + 2] == self.current_player and
                        self.board[row - 3][col + 3] == self.current_player):
                    return True

        return False

    def check_draw(self):
        """
        Checks if the game is a draw (i.e., the board is full).

        Returns:
            bool: True if the game is a draw, False otherwise.
        """
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == ' ':
                    return False  # There are still empty spaces
        return True  # Board is full

    def switch_player(self):
        """
        Switches the current player to the other player.
        """
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play_turn(self):
        """
        Plays a single turn of the game, prompting the current player for input
        and updating the board.
        """
        self.print_board()
        while True:
            try:
                col = int(input(f"Player {self.current_player}, enter column (1-{self.cols}): ")) - 1
                if self.drop_piece(col):
                    break  # Valid move, exit the loop
            except ValueError:
                print("Invalid input. Please enter a number between 1 and", self.cols)
            except Exception as e:
                print("An error occurred:", e)

        if self.check_win():
            self.game_over = True
            self.winner = self.current_player
            self.print_board()
            print(f"Player {self.current_player} wins!")
        elif self.check_draw():
            self.game_over = True
            self.print_board()
            print("It's a draw!")
        else:
            self.switch_player()

    def play_game(self):
        """
        Starts and runs the Connect Four game until it is over.
        """
        print("Welcome to Connect Four!")
        while not self.game_over:
            self.play_turn()
        print("Game Over.")


if __name__ == '__main__':
    game = ConnectFour()
    game.play_game()