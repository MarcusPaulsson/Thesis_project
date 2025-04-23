class GomokuGame:
    """
    This class implements a Gomoku game, supporting moves, winner checks, and five consecutive symbols on the game board.
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
        :return: True if the move is valid, False otherwise.
        """
        if self._is_valid_move(row, col):
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_winner(self):
        """
        Checks if there is a winner by looking for five in a row in all directions (horizontal, vertical, diagonal).
        
        :return: the symbol of the winning player (either 'X' or 'O') if there is a winner, None otherwise.
        """
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] != ' ':
                    if any(self._check_five_in_a_row(row, col, direction) for direction in [(1, 0), (0, 1), (1, 1), (1, -1)]):
                        return self.board[row][col]
        return None

    def _check_five_in_a_row(self, row, col, direction):
        """
        Checks if there are five consecutive symbols of the same player in a row starting from a given cell in a given direction.
        
        :param row: int, row of the given cell
        :param col: int, column of the given cell
        :param direction: tuple, (int, int), named as (dx, dy).
        :return: True if there are five consecutive symbols of the same player, False otherwise.
        """
        dx, dy = direction
        count = 0
        player_symbol = self.board[row][col]

        for step in range(5):
            new_row = row + step * dx
            new_col = col + step * dy
            if 0 <= new_row < self.board_size and 0 <= new_col < self.board_size:
                if self.board[new_row][new_col] == player_symbol:
                    count += 1
                else:
                    break
            else:
                break

        return count == 5

    def _is_valid_move(self, row, col):
        """
        Checks if the move is valid (i.e., within bounds and on an empty cell).
        
        :param row: int, the row index of the move
        :param col: int, the column index of the move
        :return: True if the move is valid, False otherwise.
        """
        return 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == ' '