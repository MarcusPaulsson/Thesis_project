import random

class MahjongConnect:
    """
    MahjongConnect is a class representing a game board for Mahjong Connect with features like creating the board,
    checking valid moves, finding paths, removing icons, and checking if the game is over.
    """

    def __init__(self, board_size, icons):
        """
        Initialize the board size and the icon list, create the game board.
        :param board_size: list of two integer numbers, representing the number of rows and columns of the game board
        :param icons: list of string, representing the icons
        """
        self.board_size = board_size
        self.icons = icons
        self.board = self.create_board()

    def create_board(self):
        """
        Create the game board with the given board size and icons.
        :return: 2-dimensional list, the game board
        """
        flat_icons = self.icons * (self.board_size[0] * self.board_size[1] // len(self.icons))
        random.shuffle(flat_icons)
        return [flat_icons[i:i + self.board_size[1]] for i in range(0, len(flat_icons), self.board_size[1])]

    def is_valid_move(self, pos1, pos2):
        """
        Check if the move of two icons is valid.
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return: True or False, representing whether the move of two icons is valid
        """
        if pos1 == pos2:
            return False
        if not self.is_within_bounds(pos1) or not self.is_within_bounds(pos2):
            return False
        if self.board[pos1[0]][pos1[1]] != self.board[pos2[0]][pos2[1]]:
            return False
        return self.has_path(pos1, pos2)

    def has_path(self, pos1, pos2):
        """
        Check if there is a path between two icons.
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return: True or False, representing whether there is a path between two icons
        """
        # Implement pathfinding logic (not shown)
        pass

    def remove_icons(self, pos1, pos2):
        """
        Remove the connected icons on the game board.
        :param pos1: position tuple(x, y) of the first icon to be removed
        :param pos2: position tuple(x, y) of the second icon to be removed
        """
        self.board[pos1[0]][pos1[1]] = ' '
        self.board[pos2[0]][pos2[1]] = ' '

    def is_game_over(self):
        """
        Check if the game is over (i.e., if there are no more icons on the game board).
        :return: True or False, representing whether the game is over
        """
        return all(icon == ' ' for row in self.board for icon in row)

    def is_within_bounds(self, pos):
        """
        Check if the position is within the bounds of the board.
        :param pos: position tuple(x, y)
        :return: True if within bounds, False otherwise
        """
        return 0 <= pos[0] < self.board_size[0] and 0 <= pos[1] < self.board_size[1]