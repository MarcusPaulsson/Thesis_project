import random

class MahjongConnect:
    """
    MahjongConnect is a class representing a game board for Mahjong Connect with features like creating the board, checking valid moves, finding paths, removing icons, and checking if the game is over.
    """

    def __init__(self, board_size, icons):
        """
        Initialize the board size and the icon list, create the game board.

        Args:
            board_size (list): A list of two integers representing the number of rows and columns of the game board.
            icons (list): A list of strings representing the icons.
        """
        self.BOARD_SIZE = board_size
        self.ICONS = icons
        self.board = self.create_board()

    def create_board(self):
        """
        Create the game board with the given board size and icons.

        Returns:
            list: A 2-dimensional list representing the game board.
        """
        rows, cols = self.BOARD_SIZE
        num_icons = rows * cols // 2
        if num_icons * 2 > len(self.ICONS) * (rows * cols // len(self.ICONS)):
            raise ValueError("Not enough icons to fill the board.")

        icons = self.ICONS * (rows * cols // len(self.ICONS))
        icons = icons[:num_icons] * 2
        random.shuffle(icons)

        board = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(icons[i * cols + j])
            board.append(row)
        return board

    def is_valid_move(self, pos1, pos2):
        """
        Check if the move of two icons is valid.

        Args:
            pos1 (tuple): A tuple (row, col) representing the position of the first icon.
            pos2 (tuple): A tuple (row, col) representing the position of the second icon.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        row1, col1 = pos1
        row2, col2 = pos2
        rows, cols = self.BOARD_SIZE

        if not (0 <= row1 < rows and 0 <= col1 < cols and 0 <= row2 < rows and 0 <= col2 < cols):
            return False

        if pos1 == pos2:
            return False

        if self.board[row1][col1] == ' ' or self.board[row2][col2] == ' ':
            return False

        if self.board[row1][col1] != self.board[row2][col2]:
            return False

        return self.has_path(pos1, pos2)

    def has_path(self, pos1, pos2):
        """
        Check if there is a path between two icons with at most two turns.

        Args:
            pos1 (tuple): A tuple (row, col) representing the position of the first icon.
            pos2 (tuple): A tuple (row, col) representing the position of the second icon.

        Returns:
            bool: True if a path exists, False otherwise.
        """
        rows, cols = self.BOARD_SIZE

        def is_valid(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def can_reach(start_row, start_col, end_row, end_col, turns_left, visited):
            if (start_row, start_col) == (end_row, end_col) and turns_left >= 0:
                return True
            if turns_left < 0:
                return False
            if (start_row, start_col, turns_left) in visited:
                return False

            visited.add((start_row, start_col, turns_left))

            # Move horizontally
            for col in range(start_col + 1, cols):
                if self.board[start_row][col] != ' ' and (start_row, col) != (end_row, end_col):
                    break
                if can_reach(start_row, col, end_row, end_col, turns_left - 1 if (start_row,col) != pos2 and (start_row, col) != pos1 else turns_left, visited):
                    return True
            for col in range(start_col - 1, -1, -1):
                if self.board[start_row][col] != ' ' and (start_row, col) != (end_row, end_col):
                    break
                if can_reach(start_row, col, end_row, end_col, turns_left - 1 if (start_row,col) != pos2 and (start_row, col) != pos1 else turns_left, visited):
                    return True

            # Move vertically
            for row in range(start_row + 1, rows):
                if self.board[row][start_col] != ' ' and (row, start_col) != (end_row, end_col):
                    break
                if can_reach(row, start_col, end_row, end_col, turns_left - 1 if (row,start_col) != pos2 and (row, start_col) != pos1 else turns_left, visited):
                    return True
            for row in range(start_row - 1, -1, -1):
                if self.board[row][start_col] != ' ' and (row, start_col) != (end_row, end_col):
                    break
                if can_reach(row, start_col, end_row, end_col, turns_left - 1 if (row,start_col) != pos2 and (row, start_col) != pos1 else turns_left, visited):
                    return True

            return False

        visited = set()
        return can_reach(pos1[0], pos1[1], pos2[0], pos2[1], 2, visited)

    def remove_icons(self, pos1, pos2):
        """
        Remove the connected icons on the game board.

        Args:
            pos1 (tuple): A tuple (row, col) representing the position of the first icon to be removed.
            pos2 (tuple): A tuple (row, col) representing the position of the second icon to be removed.
        """
        self.board[pos1[0]][pos1[1]] = ' '
        self.board[pos2[0]][pos2[1]] = ' '

    def is_game_over(self):
        """
        Check if the game is over (i.e., if there are no more icons on the game board).

        Returns:
            bool: True if the game is over, False otherwise.
        """
        for row in self.board:
            for icon in row:
                if icon != ' ':
                    return False
        return True