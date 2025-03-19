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
        self.current_player = 'X'  # Player X starts
        self.game_over = False

    def print_board(self):
        """
        Prints the current state of the game board to the console.
        """
        for row in range(self.rows):
            print('|', end='')
            for col in range(self.cols):
                print(self.board[row][col], end='|')
            print()
        print('-' * (2 * self.cols + 1))  # Separator line
        print(' ', end='')
        for col in range(self.cols):
            print(col + 1, end=' ') # Column numbers
        print()

    def is_valid_move(self, col):
        """
        Checks if a move (dropping a piece into a column) is valid.

        Args:
            col (int): The column to check (1-indexed).

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        if col < 1 or col > self.cols:
            return False
        return self.board[0][col - 1] == ' '  # Check if top row is empty

    def drop_piece(self, col):
        """
        Drops a piece of the current player into the specified column.

        Args:
            col (int): The column to drop the piece into (1-indexed).
        """
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col - 1] == ' ':
                self.board[row][col - 1] = self.current_player
                return row  # Return the row where the piece landed

    def check_win(self, row, col):
        """
        Checks if the current move resulted in a win for the current player.

        Args:
            row (int): The row where the piece was dropped.
            col (int): The column where the piece was dropped (1-indexed).

        Returns:
            bool: True if the current player has won, False otherwise.
        """
        player = self.current_player

        # Check horizontal
        count = 0
        for c in range(self.cols):
            if self.board[row][c] == player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

        # Check vertical
        count = 0
        for r in range(self.rows):
            if self.board[r][col - 1] == player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

        # Check positive diagonal
        count = 0
        for i in range(-3, 4):
            r = row + i
            c = col - 1 + i
            if 0 <= r < self.rows and 0 <= c < self.cols:
                if self.board[r][c] == player:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0

        # Check negative diagonal
        count = 0
        for i in range(-3, 4):
            r = row - i
            c = col - 1 + i
            if 0 <= r < self.rows and 0 <= c < self.cols:
                if self.board[r][c] == player:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0

        return False

    def check_draw(self):
        """
        Checks if the game is a draw (board is full).

        Returns:
            bool: True if the game is a draw, False otherwise.
        """
        for col in range(self.cols):
            if self.board[0][col] == ' ':
                return False  # At least one empty space
        return True

    def switch_player(self):
        """
        Switches the current player to the other player.
        """
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play_game(self):
        """
        Starts and runs the Connect Four game loop.
        """
        while not self.game_over:
            self.print_board()
            print(f"Player {self.current_player}, it's your turn.")
            try:
                col = int(input(f"Enter the column to drop your piece (1-{self.cols}): "))
                if self.is_valid_move(col):
                    row = self.drop_piece(col)
                    if self.check_win(row, col):
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
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    game = ConnectFour()
    game.play_game()