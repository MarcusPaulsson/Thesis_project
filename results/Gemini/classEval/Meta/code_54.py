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
        >>>mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.BOARD_SIZE = [4, 4]
        mc.ICONS = ['a', 'b', 'c']
        mc.board = mc.create_board()
        """
        self.BOARD_SIZE = BOARD_SIZE
        self.ICONS = ICONS
        self.board = self.create_board()

    def create_board(self):
        """
        create the game board with the given board size and icons
        :return: 2-dimensional list, the game board
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        >>> mc.create_board()
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        """
        rows, cols = self.BOARD_SIZE
        num_icons = len(self.ICONS)
        board = []
        icons = (self.ICONS * (rows * cols // len(self.ICONS) // 2 + 1) * 2)[:rows * cols]
        random.shuffle(icons)
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(icons[i * cols + j])
            board.append(row)
        return board

    def is_valid_move(self, pos1, pos2):
        """
        check if the move of two icons is valid (i.e. positions are within the game board range, the two positions are not the same, the two positions have the same icon, and there is a valid path between the two positions)
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return:True or False ,representing whether the move of two icons is valid
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        >>> mc.is_valid_move((0, 0), (1, 0))
        True
        """
        x1, y1 = pos1
        x2, y2 = pos2
        rows, cols = self.BOARD_SIZE

        if not (0 <= x1 < rows and 0 <= y1 < cols and 0 <= x2 < rows and 0 <= y2 < cols):
            return False

        if pos1 == pos2:
            return False

        if self.board[x1][y1] != self.board[x2][y2]:
            return False

        if self.has_path(pos1, pos2):
            return True

        return False


    def has_path(self, pos1, pos2):
        """
        check if there is a path between two icons
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return: True or False ,representing whether there is a path between two icons
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        >>> mc.is_valid_move((0, 0), (1, 0))
        True
        """
        x1, y1 = pos1
        x2, y2 = pos2
        rows, cols = self.BOARD_SIZE

        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols

        def check_path(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if x1 == x2:
                for y in range(min(y1, y2) + 1, max(y1, y2)):
                    if self.board[x1][y] != ' ':
                        return False
                return True
            if y1 == y2:
                for x in range(min(x1, x2) + 1, max(x1, x2)):
                    if self.board[x][y1] != ' ':
                        return False
                return True
            return False

        # Direct connection
        if check_path(pos1, pos2):
            return True

        # One turn
        for i in range(rows):
            if check_path(pos1, (i, y1)) and check_path((i, y1), pos2) and self.board[i][y1] == ' ':
                return True
        for j in range(cols):
            if check_path(pos1, (x1, j)) and check_path((x1, j), pos2) and self.board[x1][j] == ' ':
                return True

        # Two turns
        for i in range(rows):
            for j in range(cols):
                if self.board[i][j] == ' ':
                    if check_path(pos1, (i, j)) and check_path((i, j), pos2):
                        # Path 1 to (i,j)
                        path1_valid = True
                        if pos1[0] == (i,j)[0]:
                            for k in range(min(pos1[1], (i,j)[1]) + 1, max(pos1[1], (i,j)[1])):
                                if self.board[pos1[0]][k] != ' ':
                                    path1_valid = False
                                    break
                        else:
                            for k in range(min(pos1[0], (i,j)[0]) + 1, max(pos1[0], (i,j)[0])):
                                if self.board[k][pos1[1]] != ' ':
                                    path1_valid = False
                                    break
                        #Path 2 (i,j) to pos2
                        path2_valid = True
                        if pos2[0] == (i,j)[0]:
                            for k in range(min(pos2[1], (i,j)[1]) + 1, max(pos2[1], (i,j)[1])):
                                if self.board[pos2[0]][k] != ' ':
                                    path2_valid = False
                                    break
                        else:
                            for k in range(min(pos2[0], (i,j)[0]) + 1, max(pos2[0], (i,j)[0])):
                                if self.board[k][pos2[1]] != ' ':
                                    path2_valid = False
                                    break
                        if path1_valid and path2_valid:
                            return True
        return False

    def remove_icons(self, pos1, pos2):
        """
        remove the connected icons on the game board
        :param pos1: position tuple(x, y) of the first icon to be removed
        :param pos2: position tuple(x, y) of the second icon to be removed
        :return: None
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        >>> mc.remove_icons((0, 0), (1, 0))
        mc.board = [[' ', 'b', 'c', 'a'],
                    [' ', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        """
        x1, y1 = pos1
        x2, y2 = pos2
        self.board[x1][y1] = ' '
        self.board[x2][y2] = ' '


    def is_game_over(self):
        """
        Check if the game is over (i.e., if there are no more icons on the game board)
        :return: True or False ,representing whether the game is over
        >>> mc = MahjongConnect([4, 4] ['a', 'b', 'c'])
        >>> mc.board = [[' ', ' ', ' ', ' '],
        >>>         [' ', ' ', ' ', ' '],
        >>>         [' ', ' ', ' ', ' '],
        >>>         [' ', ' ', ' ', ' ']]
        >>> mc.is_game_over()
        True
        """
        for row in self.board:
            for icon in row:
                if icon != ' ':
                    return False
        return True