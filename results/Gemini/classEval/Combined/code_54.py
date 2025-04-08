import random

class MahjongConnect:
    """
    MahjongConnect is a class representing a game board for Mahjong Connect.
    """

    def __init__(self, board_size, icons):
        """
        Initializes the game board with the given size and icons.

        :param board_size: List of two integers, representing rows and columns.
        :param icons: List of strings, representing the available icons.
        """
        self.BOARD_SIZE = board_size
        self.ICONS = icons
        self.board = self.create_board()

    def create_board(self):
        """
        Creates a 2D list representing the game board, populated with icons.

        :return: A 2D list (rows x cols) representing the game board.
        """
        rows, cols = self.BOARD_SIZE
        num_icons = len(self.ICONS)
        board = []
        for _ in range(rows):
            row = []
            for _ in range(cols):
                row.append(random.choice(self.ICONS))
            board.append(row)
        return board

    def is_valid_move(self, pos1, pos2):
        """
        Checks if a move between two positions is valid.

        A move is valid if:
        1. Both positions are within the board boundaries.
        2. The positions are not the same.
        3. The icons at both positions are the same.
        4. There is a valid path between the two positions.

        :param pos1: Tuple (row, col) of the first position.
        :param pos2: Tuple (row, col) of the second position.
        :return: True if the move is valid, False otherwise.
        """
        if not self._is_within_bounds(pos1) or not self._is_within_bounds(pos2):
            return False

        if pos1 == pos2:
            return False

        if self.board[pos1[0]][pos1[1]] != self.board[pos2[0]][pos2[1]]:
            return False

        return self.has_path(pos1, pos2)

    def _is_within_bounds(self, pos):
        """
        Checks if a given position is within the board boundaries.

        :param pos: Tuple (row, col) representing the position.
        :return: True if the position is within bounds, False otherwise.
        """
        row, col = pos
        rows, cols = self.BOARD_SIZE
        return 0 <= row < rows and 0 <= col < cols

    def has_path(self, pos1, pos2):
        """
        Checks if there is a clear path between two positions. This implementation only checks for direct horizontal or vertical paths.

        :param pos1: Tuple (row, col) of the first position.
        :param pos2: Tuple (row, col) of the second position.
        :return: True if a path exists, False otherwise.
        """
        rows, cols = self.BOARD_SIZE

        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols

        def can_connect(p1, p2, board_state):
            if p1 == p2:
                return True

            r1, c1 = p1
            r2, c2 = p2

            if r1 == r2:
                # Horizontal check
                start = min(c1, c2) + 1
                end = max(c1, c2)
                path_clear = all(board_state[r1][y] == ' ' for y in range(start, end))
                return path_clear

            elif c1 == c2:
                # Vertical check
                start = min(r1, r2) + 1
                end = max(r1, r2)
                path_clear = all(board_state[x][c1] == ' ' for x in range(start, end))
                return path_clear
            else:
                return False

        # Create a copy of the board to avoid modifying the original
        temp_board = [row[:] for row in self.board]

        return can_connect(pos1, pos2, temp_board)

    def remove_icons(self, pos1, pos2):
        """
        Removes the icons at the given positions by setting them to ' '.

        :param pos1: Tuple (row, col) of the first icon to remove.
        :param pos2: Tuple (row, col) of the second icon to remove.
        """
        self.board[pos1[0]][pos1[1]] = ' '
        self.board[pos2[0]][pos2[1]] = ' '

    def is_game_over(self):
        """
        Checks if the game is over, meaning no more icons are left on the board.

        :return: True if the game is over, False otherwise.
        """
        for row in self.board:
            for icon in row:
                if icon != ' ':
                    return False
        return True