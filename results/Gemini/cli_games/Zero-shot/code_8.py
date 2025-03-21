class ConnectFour:
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.current_player = 'X'  # Player X starts
        self.game_over = False

    def print_board(self):
        """Prints the current state of the board."""
        for row in range(self.rows):
            print('|', end='')
            for col in range(self.cols):
                print(self.board[row][col], end='|')
            print()
        print('+' + '-+' * self.cols)
        print(' ', end='')
        for col in range(self.cols):
            print(col + 1, end=' ')
        print()

    def drop_piece(self, col):
        """Drops a piece into the specified column."""
        col -= 1  # Adjust to 0-based indexing

        if not (0 <= col < self.cols):
            print("Invalid column.  Please choose a column between 1 and", self.cols)
            return False

        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player
                return True  # Piece successfully dropped
        print("Column is full.  Please choose another column.")
        return False  # Column is full

    def check_win(self):
        """Checks if the current player has won."""

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
        """Checks if the board is full (a draw)."""
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == ' ':
                    return False  # Found an empty space, not a draw
        return True  # No empty spaces, it's a draw

    def switch_player(self):
        """Switches the current player."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play_game(self):
        """Main game loop."""
        while not self.game_over:
            self.print_board()
            print(f"Player {self.current_player}, it's your turn.")

            try:
                col = int(input(f"Enter the column number (1-{self.cols}) to drop your piece: "))
                if self.drop_piece(col):
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
                    continue # Try again if drop_piece failed
            except ValueError:
                print("Invalid input. Please enter a number.")
            except KeyboardInterrupt:
                print("\nGame interrupted. Exiting...")
                self.game_over = True



if __name__ == "__main__":
    game = ConnectFour()
    game.play_game()