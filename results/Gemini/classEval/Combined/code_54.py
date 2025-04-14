import random

class MahjongConnect:
    """
    MahjongConnect is a class representing a game board for Mahjong Connect with features like creating the board, checking valid moves, finding paths, removing icons, and checking if the game is over.
    """

    def __init__(self, BOARD_SIZE, ICONS):
        """
        initialize the board size and the icon list, create the game board
        :param BOARD_SIZE: list of two integer numbers, representing the number of rows and columns of the game board
        :param ICONS: list of string, representing the icons
        """
        self.BOARD_SIZE = BOARD_SIZE
        self.ICONS = ICONS
        self.board = self.create_board()

    def create_board(self):
        """
        create the game board with the given board size and icons
        :return: 2-dimensional list, the game board
        """
        rows, cols = self.BOARD_SIZE
        board = []
        icons = self.ICONS * ((rows * cols) // len(self.ICONS))
        if (rows * cols) % len(self.ICONS) != 0:
            icons += self.ICONS[:(rows * cols) % len(self.ICONS)]
        random.shuffle(icons)
        
        board_icons = icons[:rows * cols]
        board = [board_icons[i * cols:(i + 1) * cols] for i in range(rows)]
        
        return board

    def is_valid_move(self, pos1, pos2):
        """
        check if the move of two icons is valid (i.e. positions are within the game board range, the two positions are not the same, the two positions have the same icon, and there is a valid path between the two positions)
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return:True or False ,representing whether the move of two icons is valid
        """
        if not self.is_valid_position(pos1) or not self.is_valid_position(pos2):
            return False

        if pos1 == pos2:
            return False

        if self.board[pos1[0]][pos1[1]] != self.board[pos2[0]][pos2[1]]:
            return False

        if self.board[pos1[0]][pos1[1]] == ' ':
            return False

        return self.has_path(pos1, pos2)

    def is_valid_position(self, pos):
        """
        check if the position is within the game board range
        :param pos: position tuple(x, y) of the icon
        :return: True or False, representing whether the position is valid
        """
        rows, cols = self.BOARD_SIZE
        r, c = pos
        return 0 <= r < rows and 0 <= c < cols

    def has_path(self, pos1, pos2):
        """
        check if there is a path between two icons
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return: True or False ,representing whether there is a path between two icons
        """
        rows, cols = self.BOARD_SIZE

        def find_path(p1, p2, turns):
            if turns > 2:
                return False

            if p1 == p2:
                return True

            r, c = p1
            
            # Move horizontally
            for nc in range(cols):
                if nc == c:
                    continue
                
                valid_horizontal = True
                for k in range(min(c, nc) + 1, max(c, nc)):
                    if self.board[r][k] != ' ':
                        valid_horizontal = False
                        break
                
                if valid_horizontal:
                    if find_path((r, nc), p2, turns + (1 if nc != c else 0)):
                        return True

            # Move vertically
            for nr in range(rows):
                if nr == r:
                    continue
                
                valid_vertical = True
                for k in range(min(r, nr) + 1, max(r, nr)):
                    if self.board[k][c] != ' ':
                        valid_vertical = False
                        break
                
                if valid_vertical:
                    if find_path((nr, c), p2, turns + (1 if nr != r else 0)):
                        return True

            return False

        return find_path(pos1, pos2, 0)

    def remove_icons(self, pos1, pos2):
        """
        remove the connected icons on the game board
        :param pos1: position tuple(x, y) of the first icon to be removed
        :param pos2: position tuple(x, y) of the second icon to be removed
        :return: None
        """
        self.board[pos1[0]][pos1[1]] = ' '
        self.board[pos2[0]][pos2[1]] = ' '

    def is_game_over(self):
        """
        Check if the game is over (i.e., if there are no more icons on the game board)
        :return: True or False ,representing whether the game is over
        """
        for row in self.board:
            for icon in row:
                if icon != ' ':
                    return False
        return True