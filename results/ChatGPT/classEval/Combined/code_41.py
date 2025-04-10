class GomokuGame:
    """
    This class implements a Gomoku game, allowing players to make moves, check for a winner,
    and verify if there are five consecutive symbols on the game board.
    """

    def __init__(self, board_size):
        """
        Initializes the game with a specified board size, creating an empty board
        and setting the current player to 'X'.
        """
        self.board_size = board_size
        self.board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        self.current_player = 'X'

    def make_move(self, row, col):
        """
        Makes a move at the specified row and column.
        If the move is valid, it places the current player's symbol on the board
        and switches to the other player.
        
        :param row: int, row index of the move
        :param col: int, column index of the move
        :return: True if the move is valid, False otherwise.
        """
        if not self._is_valid_move(row, col):
            return False

        self.board[row][col] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return True

    def check_winner(self):
        """
        Checks for a winner by looking for five in a row in all directions (horizontal, vertical, diagonal).
        
        :return: the symbol of the winning player ('X' or 'O') if there is a winner, None otherwise.
        """
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] != ' ':
                    if any(self._check_five_in_a_row(row, col, direction) for direction in [(1, 0), (0, 1), (1, 1), (1, -1)]):
                        return self.board[row][col]
        return None

    def _check_five_in_a_row(self, row, col, direction):
        """
        Checks for five consecutive symbols of the same player starting from a given cell in a specified direction.
        
        :param row: int, row of the starting cell
        :param col: int, column of the starting cell
        :param direction: tuple (dx, dy), direction to check
        :return: True if there are five consecutive symbols, False otherwise.
        """
        dx, dy = direction
        player_symbol = self.board[row][col]

        for i in range(5):
            new_row = row + i * dx
            new_col = col + i * dy
            if not (0 <= new_row < self.board_size and 0 <= new_col < self.board_size and self.board[new_row][new_col] == player_symbol):
                return False
        return True

    def _is_valid_move(self, row, col):
        """
        Validates if a move can be made at the specified position.
        
        :param row: int, row index of the move
        :param col: int, column index of the move
        :return: True if the move is valid, False otherwise.
        """
        return 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == ' '