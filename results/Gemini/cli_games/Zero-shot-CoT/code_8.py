class ConnectFour:
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.current_player = 'X'  # Start with player X
        self.game_over = False

    def print_board(self):
        """Prints the Connect Four board to the console."""
        for row in range(self.rows):
            print('|' + '|'.join(self.board[row]) + '|')
        print('+' + '+'.join(str(i + 1) for i in range(self.cols)) + '+') # Column numbers


    def is_valid_move(self, col):
        """Checks if a move (column) is valid."""
        if not (0 <= col < self.cols):
            return False  # Column out of bounds
        return self.board[0][col] == ' '  # Column not full

    def drop_piece(self, col):
        """Drops a piece into the specified column."""
        if not self.is_valid_move(col):
            return False  # Invalid move

        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player
                return True  # Piece dropped successfully

        return False  # Should not reach here if move is valid

    def check_win(self):
        """Checks for a win in horizontal, vertical, and diagonal directions."""

        # Horizontal
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if (self.board[row][col] == self.current_player and
                        self.board[row][col + 1] == self.current_player and
                        self.board[row][col + 2] == self.current_player and
                        self.board[row][col + 3] == self.current_player):
                    return True

        # Vertical
        for row in range(self.rows - 3):
            for col in range(self.cols):
                if (self.board[row][col] == self.current_player and
                        self.board[row + 1][col] == self.current_player and
                        self.board[row + 2][col] == self.current_player and
                        self.board[row + 3][col] == self.current_player):
                    return True

        # Positive Diagonal
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if (self.board[row][col] == self.current_player and
                        self.board[row + 1][col + 1] == self.current_player and
                        self.board[row + 2][col + 2] == self.current_player and
                        self.board[row + 3][col + 3] == self.current_player):
                    return True

        # Negative Diagonal
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                if (self.board[row][col] == self.current_player and
                        self.board[row - 1][col + 1] == self.current_player and
                        self.board[row - 2][col + 2] == self.current_player and
                        self.board[row - 3][col + 3] == self.current_player):
                    return True

        return False


    def check_draw(self):
        """Checks if the board is full (draw)."""
        for col in range(self.cols):
            if self.board[0][col] == ' ':
                return False  # Not a draw, there's an empty space
        return True  # It's a draw

    def switch_player(self):
        """Switches the current player."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play_turn(self, col):
        """Plays a single turn for the current player."""
        if self.game_over:
            return False

        if self.drop_piece(col):
            if self.check_win():
                self.print_board()
                print(f"Player {self.current_player} wins!")
                self.game_over = True
                return True

            if self.check_draw():
                self.print_board()
                print("It's a draw!")
                self.game_over = True
                return True

            self.switch_player()
            return True
        else:
            print("Invalid move. Try again.")
            return False #Invalid move


    def play_game(self):
        """Main game loop."""
        while not self.game_over:
            self.print_board()
            try:
                col = int(input(f"Player {self.current_player}, enter column (1-{self.cols}): ")) - 1
                if not self.play_turn(col):
                    continue #Invalid move, ask again
            except ValueError:
                print("Invalid input. Enter a number between 1 and", self.cols)
                continue #Invalid input, ask again
            except KeyboardInterrupt:
                print("\nGame interrupted.")
                self.game_over = True #End the game gracefully

if __name__ == "__main__":
    game = ConnectFour()
    game.play_game()