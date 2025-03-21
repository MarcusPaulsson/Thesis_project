class ConnectFour:
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
        self.current_player = 'X'  # 'X' or 'O'
        self.game_over = False

    def print_board(self):
        """Prints the current state of the board to the console."""
        for row in self.board:
            print('|' + '|'.join(row) + '|')
        print('+' + '+'.join(['-'] * self.cols) + '+')
        print(' ' + ' '.join(map(str, range(1, self.cols + 1))))

    def is_valid_move(self, col):
        """
        Checks if a move (column) is valid.

        Args:
            col (int): The column number (1-indexed).

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        if not (1 <= col <= self.cols):
            return False
        return self.board[0][col - 1] == ' '  # Check if the top row is empty

    def drop_piece(self, col):
        """
        Drops a piece into the specified column.

        Args:
            col (int): The column number (1-indexed).

        Returns:
            bool: True if the piece was successfully dropped, False otherwise (invalid move).
        """
        if not self.is_valid_move(col):
            return False

        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col - 1] == ' ':
                self.board[row][col - 1] = self.current_player
                return True
        return False  # Should not reach here if is_valid_move is used correctly.

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
        Checks if the board is full (draw).

        Returns:
            bool: True if the board is full, False otherwise.
        """
        for col in range(self.cols):
            if self.board[0][col] == ' ':
                return False
        return True

    def switch_player(self):
        """Switches the current player to the other player."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play_turn(self):
        """Plays a single turn of the game."""
        self.print_board()
        print(f"Player {self.current_player}, it's your turn.")

        while True:
            try:
                col = int(input(f"Enter a column (1-{self.cols}): "))
                if self.drop_piece(col):
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

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

    def play_game(self):
        """Starts and runs the Connect Four game until it's over."""
        print("Welcome to Connect Four!")
        while not self.game_over:
            self.play_turn()
        print("Game over.")


if __name__ == "__main__":
    game = ConnectFour()
    game.play_game()