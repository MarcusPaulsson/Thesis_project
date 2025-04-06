class GomokuGame:
    """
    This class implements a Gomoku game, supporting moves, winner checking,
    and verifying five consecutive symbols on the game board.
    """

    def __init__(self, board_size):
        """
        Initializes the game with a given board size.
        The board is initialized with empty spaces, and the current player symbol is set to 'X'.
        """
        self.board_size = board_size
        self.board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        self.current_player = 'X'
        self.move_count = 0

    def make_move(self, row, col):
        """
        Makes a move at the given row and column.
        If the move is valid, it places the current player's symbol on the board
        and switches the current player.
        :param row: int, the row index of this move
        :param col: int, the column index
        :return: True if the move is valid, or False otherwise.
        """
        if self._is_valid_move(row, col):
            self.board[row][col] = self.current_player
            self.move_count += 1
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def _is_valid_move(self, row, col):
        """
        Validates the move by checking if the cell is within bounds and empty.
        :param row: int, the row index
        :param col: int, the column index
        :return: True if the move is valid, otherwise False.
        """
        return 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == ' '

    def check_winner(self):
        """
        Checks if there is a winner by searching for five in a row in all directions.
        :return: the symbol of the winning player ('X' or 'O') if there is a winner, or None otherwise.
        """
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] != ' ':
                    if (self._check_five_in_a_row(row, col, (0, 1)) or  # Horizontal
                        self._check_five_in_a_row(row, col, (1, 0)) or  # Vertical
                        self._check_five_in_a_row(row, col, (1, 1)) or  # Diagonal /
                        self._check_five_in_a_row(row, col, (1, -1))):  # Diagonal \
                        return self.board[row][col]
        return None

    def _check_five_in_a_row(self, row, col, direction):
        """
        Checks for five consecutive symbols from a given cell in a specified direction.
        :param row: int, row of the given cell
        :param col: int, column of the given cell
        :param direction: tuple, (dx, dy). Direction to check for consecutive symbols.
        :return: True if five consecutive symbols are found, otherwise False.
        """
        dx, dy = direction
        count = 0
        player_symbol = self.board[row][col]

        for i in range(5):
            new_row = row + i * dx
            new_col = col + i * dy
            if 0 <= new_row < self.board_size and 0 <= new_col < self.board_size:
                if self.board[new_row][new_col] == player_symbol:
                    count += 1
                else:
                    break
            else:
                break

        return count == 5