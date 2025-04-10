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
        num_icons = self.board_size[0] * self.board_size[1] // 2
        icon_list = (self.icons * (num_icons // len(self.icons) + 1))[:num_icons]
        random.shuffle(icon_list)
        
        board = [
            icon_list[i * self.board_size[1]:(i + 1) * self.board_size[1]]
            for i in range(self.board_size[0])
        ]
        return board

    def is_valid_move(self, pos1, pos2):
        """
        Check if the move of two icons is valid.
        :param pos1: position tuple (x, y) of the first icon
        :param pos2: position tuple (x, y) of the second icon
        :return: True or False, representing whether the move of two icons is valid
        """
        return (pos1 != pos2 and 
                self.is_within_bounds(pos1) and 
                self.is_within_bounds(pos2) and 
                self.board[pos1[0]][pos1[1]] == self.board[pos2[0]][pos2[1]] and 
                self.has_path(pos1, pos2))

    def is_within_bounds(self, pos):
        """Check if the position is within the board bounds."""
        return 0 <= pos[0] < self.board_size[0] and 0 <= pos[1] < self.board_size[1]

    def has_path(self, pos1, pos2):
        """
        Check if there is a path between two icons.
        :param pos1: position tuple (x, y) of the first icon
        :param pos2: position tuple (x, y) of the second icon
        :return: True or False, representing whether there is a path between two icons
        """
        # Placeholder for actual path finding logic
        return True

    def remove_icons(self, pos1, pos2):
        """
        Remove the connected icons on the game board.
        :param pos1: position tuple (x, y) of the first icon to be removed
        :param pos2: position tuple (x, y) of the second icon to be removed
        """
        self.board[pos1[0]][pos1[1]] = ' '
        self.board[pos2[0]][pos2[1]] = ' '

    def is_game_over(self):
        """
        Check if the game is over (i.e., if there are no more icons on the game board).
        :return: True or False, representing whether the game is over
        """
        return all(icon == ' ' for row in self.board for icon in row)