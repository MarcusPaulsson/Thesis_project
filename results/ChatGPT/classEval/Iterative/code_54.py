import random

class MahjongConnect:
    """
    MahjongConnect is a class representing a game board for Mahjong Connect with features like creating the board, checking valid moves, finding paths, removing icons, and checking if the game is over.
    """

    def __init__(self, BOARD_SIZE, ICONS):
        """
        Initialize the board size and the icon list, create the game board.
        :param BOARD_SIZE: list of two integers, representing the number of rows and columns of the game board.
        :param ICONS: list of strings, representing the icons.
        """
        if not isinstance(BOARD_SIZE, (list, tuple)) or len(BOARD_SIZE) != 2:
            raise ValueError("BOARD_SIZE must be a list or tuple of two integers.")
        if not all(isinstance(i, int) and i > 0 for i in BOARD_SIZE):
            raise ValueError("BOARD_SIZE must contain positive integers.")
        self.BOARD_SIZE = BOARD_SIZE
        self.ICONS = ICONS
        self.board = self.create_board()

    def create_board(self):
        """
        Create the game board with the given board size and icons.
        :return: 2-dimensional list representing the game board.
        """
        rows, cols = self.BOARD_SIZE
        num_icons = len(self.ICONS)
        total_icons = (rows * cols) // 2
        if total_icons > num_icons:
            icons_list = (self.ICONS * (total_icons // num_icons + 1))[:total_icons]
        else:
            icons_list = self.ICONS[:total_icons]
        icons_list = icons_list * 2  # Each icon appears twice
        random.shuffle(icons_list)
        return [icons_list[i * cols:(i + 1) * cols] for i in range(rows)]

    def is_valid_move(self, pos1, pos2):
        """
        Check if the move of two icons is valid.
        :param pos1: position tuple (x, y) of the first icon.
        :param pos2: position tuple (x, y) of the second icon.
        :return: True or False, representing whether the move is valid.
        """
        if pos1 == pos2:
            return False
        if not self._is_position_valid(pos1) or not self._is_position_valid(pos2):
            return False
        if self.board[pos1[0]][pos1[1]] != self.board[pos2[0]][pos2[1]]:
            return False
        return self.has_path(pos1, pos2)

    def _is_position_valid(self, pos):
        x, y = pos
        return 0 <= x < self.BOARD_SIZE[0] and 0 <= y < self.BOARD_SIZE[1]

    def has_path(self, pos1, pos2):
        """
        Check if there is a path between two icons.
        :param pos1: position tuple (x, y) of the first icon.
        :param pos2: position tuple (x, y) of the second icon.
        :return: True or False, representing whether there is a path.
        """
        visited = set()
        return self._has_path_dfs(pos1[0], pos1[1], pos2[0], pos2[1], visited)

    def _has_path_dfs(self, x1, y1, x2, y2, visited):
        if (x1, y1) in visited:
            return False
        visited.add((x1, y1))
        if (x1, y1) == (x2, y2):
            return True
        
        # Directions for moving in the grid
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        for dx, dy in directions:
            nx, ny = x1 + dx, y1 + dy
            while self._is_position_valid((nx, ny)):
                if self.board[nx][ny] == ' ':
                    if self._has_path_dfs(nx, ny, x2, y2, visited):
                        return True
                elif (nx, ny) == (x2, y2):
                    return True
                else:
                    break  # Hit a wall
                nx += dx
                ny += dy

        return False

    def remove_icons(self, pos1, pos2):
        """
        Remove the connected icons on the game board.
        :param pos1: position tuple (x, y) of the first icon to be removed.
        :param pos2: position tuple (x, y) of the second icon to be removed.
        """
        self.board[pos1[0]][pos1[1]] = ' '
        self.board[pos2[0]][pos2[1]] = ' '

    def is_game_over(self):
        """
        Check if the game is over.
        :return: True or False, representing whether the game is over.
        """
        for row in self.board:
            if any(icon != ' ' for icon in row):
                return False
        return True