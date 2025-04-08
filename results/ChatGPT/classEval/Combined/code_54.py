import random

class MahjongConnect:
    """
    MahjongConnect is a class representing a game board for Mahjong Connect with features like creating the board, checking valid moves, 
    finding paths, removing icons, and checking if the game is over.
    """

    def __init__(self, board_size, icons):
        """
        Initialize the board size and icon list, and create the game board.
        :param board_size: Tuple[int, int], representing the number of rows and columns of the game board.
        :param icons: List[str], representing the icons.
        """
        self.board_size = board_size
        self.icons = icons
        self.board = self.create_board()

    def create_board(self):
        """
        Create the game board with the given board size and icons.
        :return: List[List[str]], the game board.
        """
        num_icons = len(self.icons)
        total_cells = self.board_size[0] * self.board_size[1]
        icons_to_place = (self.icons * (total_cells // num_icons))[:total_cells]
        random.shuffle(icons_to_place)
        
        return [icons_to_place[i * self.board_size[1]:(i + 1) * self.board_size[1]] for i in range(self.board_size[0])]

    def is_valid_move(self, pos1, pos2):
        """
        Check if the move of two icons is valid.
        :param pos1: Tuple[int, int], position of the first icon.
        :param pos2: Tuple[int, int], position of the second icon.
        :return: bool, representing whether the move of two icons is valid.
        """
        if not self._is_within_bounds(pos1) or not self._is_within_bounds(pos2) or pos1 == pos2:
            return False
        if self.board[pos1[0]][pos1[1]] != self.board[pos2[0]][pos2[1]]:
            return False
        return self.has_path(pos1, pos2)

    def has_path(self, pos1, pos2):
        """
        Check if there is a path between two icons.
        :param pos1: Tuple[int, int], position of the first icon.
        :param pos2: Tuple[int, int], position of the second icon.
        :return: bool, representing whether there is a path between two icons.
        """
        # Implement pathfinding logic (BFS or DFS) to determine if a path exists
        return True  # Placeholder for actual pathfinding logic

    def remove_icons(self, pos1, pos2):
        """
        Remove the connected icons on the game board.
        :param pos1: Tuple[int, int], position of the first icon to be removed.
        :param pos2: Tuple[int, int], position of the second icon to be removed.
        """
        self.board[pos1[0]][pos1[1]] = ' '
        self.board[pos2[0]][pos2[1]] = ' '

    def is_game_over(self):
        """
        Check if the game is over (i.e., if there are no more icons on the game board).
        :return: bool, representing whether the game is over.
        """
        return all(icon == ' ' for row in self.board for icon in row)

    def _is_within_bounds(self, pos):
        """
        Check if the given position is within the bounds of the board.
        :param pos: Tuple[int, int], position.
        :return: bool, True if within bounds, False otherwise.
        """
        return 0 <= pos[0] < self.board_size[0] and 0 <= pos[1] < self.board_size[1]