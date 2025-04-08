class GomokuGame:
    """
    This class is an implementation of a Gomoku game, supporting for making moves, checking for a winner,
    and checking if there are five consecutive symbols on the game board.
    """

    def __init__(self, board_size):
        """
        Initializes the game with a given board size.
        It initializes the board with empty spaces and sets the current player symbol as 'X'.
        """
        self.board_size = board_size
        self.board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        self.current_player = 'X'

    def make_move(self, row, col):
        """
        Makes a move at the given row and column.
        If the move is valid, it places the current player's symbol on the board
        and changes the current player to the other player.
        :param row: int, the row index of this move
        :param col: int, the column index
        :return: True if the move is valid, or False otherwise.
        """
        if not self._is_valid_move(row, col):
            return False
        
        self.board[row][col] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return True

    def check_winner(self):
        """
        Checks if there is a winner by looking for five in a row in all directions (horizontal, vertical, diagonal).
        :return: the symbol of the winning player (either 'X' or 'O') if there is a winner, or None otherwise.
        """
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] != ' ':
                    if any(self._check_five_in_a_row(row, col, direction) for direction in [(1, 0), (0, 1), (1, 1), (1, -1)]):
                        return self.board[row][col]
        return None

    def _check_five_in_a_row(self, row, col, direction):
        """
        Checks if there are five consecutive symbols of the same player in a row starting from a given cell
        in a given direction (horizontal, vertical, diagonal).
        :param row: int, row of the given cell
        :param col: int, column of the given cell
        :param direction: tuple, (int, int), named as (dx, dy).
        :return: True if there are five consecutive symbols of the same player, and False otherwise.
        """
        dx, dy = direction
        symbol = self.board[row][col]
        count = 0

        for step in range(5):
            new_row = row + step * dx
            new_col = col + step * dy
            
            if 0 <= new_row < self.board_size and 0 <= new_col < self.board_size and self.board[new_row][new_col] == symbol:
                count += 1
            else:
                break
        
        return count == 5

    def _is_valid_move(self, row, col):
        """
        Validates whether a move can be made at the given position.
        :param row: int, the row index
        :param col: int, the column index
        :return: True if the move is valid, False otherwise.
        """
        return 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == ' '