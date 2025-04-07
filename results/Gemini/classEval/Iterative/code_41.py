class GomokuGame:
    """
    This class is an implementation of a Gomoku game, supporting for making moves, checking for a winner, and checking if there are five consecutive symbols on the game board.
    """

    def __init__(self, board_size):
        """
        Initializes the game with a given board size.
        It initializes the board with empty spaces and sets the current player symbol as 'X'.
        """
        if not isinstance(board_size, int) or board_size <= 0:
            raise ValueError("Board size must be a positive integer.")

        self.board_size = board_size
        self.board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        self.current_player = 'X'
        self.other_player = 'O'

    def make_move(self, row, col):
        """
        Makes a move at the given row and column.
        If the move is valid, it places the current player's symbol on the board
        and changes the current player to the other player.
        :param row: int, the row index of this move
        :param col: int, the column index
        :return: True if the move is valid, or False otherwise.
        """
        if not isinstance(row, int) or not isinstance(col, int):
            return False

        if not (0 <= row < self.board_size and 0 <= col < self.board_size):
            return False

        if self.board[row][col] != ' ':
            return False

        self.board[row][col] = self.current_player
        self.current_player, self.other_player = self.other_player, self.current_player  # Swap players
        return True

    def check_winner(self):
        """
        Checks if there is a winner by looking for five in a row in all directions (horizontal, vertical, diagonal).
        :return: the symbol of the winning player (either 'X' or 'O') if there is a winner, or None otherwise.
        """
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] != ' ':
                    player = self.board[row][col]
                    if self._check_five_in_a_row(row, col, (0, 1), player):  # Horizontal
                        return player
                    if self._check_five_in_a_row(row, col, (1, 0), player):  # Vertical
                        return player
                    if self._check_five_in_a_row(row, col, (1, 1), player):  # Diagonal
                        return player
                    if self._check_five_in_a_row(row, col, (1, -1), player):  # Anti-Diagonal
                        return player
        return None

    def _check_five_in_a_row(self, row, col, direction, player):
        """
        Checks if there are five consecutive symbols of the same player in a row starting from a given cell in a given direction.
        :param row: int, row of the given cell
        :param col: int, column of the given cell
        :param direction: tuple, (int, int), representing the direction to check (dx, dy).
        :param player: The player ('X' or 'O') to check for.
        :return: True if there are five consecutive symbols of the same player, and False otherwise.
        """
        count = 0
        for i in range(5):
            new_row = row + i * direction[0]
            new_col = col + i * direction[1]
            if 0 <= new_row < self.board_size and 0 <= new_col < self.board_size and self.board[new_row][new_col] == player:
                count += 1
            else:
                return False
        return count == 5

    def is_board_full(self):
        """
        Checks if the board is full.
        :return: True if the board is full, False otherwise.
        """
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] == ' ':
                    return False
        return True

    def get_board(self):
        """
        Returns the current state of the board.
        :return: A 2D list representing the board.
        """
        return [row[:] for row in self.board]  # Return a copy to prevent modification

    def print_board(self):
        """Prints the board to the console."""
        for row in self.board:
            print('|' + '|'.join(row) + '|')
            print('-' * (2 * self.board_size + 1))