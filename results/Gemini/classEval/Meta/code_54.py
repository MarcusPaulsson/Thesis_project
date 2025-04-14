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
        icons = self.ICONS * ((rows * cols) // len(self.ICONS))
        if (rows * cols) % len(self.ICONS) != 0:
            icons += self.ICONS[:(rows * cols) % len(self.ICONS)]
        random.shuffle(icons)
        
        k = 0
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(icons[k])
                k += 1
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
        row1, col1 = pos1
        row2, col2 = pos2
        rows, cols = self.BOARD_SIZE

        if not (0 <= row1 < rows and 0 <= col1 < cols and 0 <= row2 < rows and 0 <= col2 < cols):
            return False
        if pos1 == pos2:
            return False
        if self.board[row1][col1] != self.board[row2][col2]:
            return False
        if self.board[row1][col1] == ' ':
            return False

        return self.has_path(pos1, pos2)


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
        row1, col1 = pos1
        row2, col2 = pos2
        rows, cols = self.BOARD_SIZE

        if not (0 <= row1 < rows and 0 <= col1 < cols and 0 <= row2 < rows and 0 <= col2 < cols):
            return False

        if pos1 == pos2:
            return True

        # Create a copy of the board with ' ' representing empty spaces
        temp_board = [row[:] for row in self.board]

        def is_valid(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def find_path(r1, c1, r2, c2, turns_left):
            if turns_left < 0:
                return False

            if r1 == r2 and c1 == c2:
                return True

            # Move horizontally
            for c in range(c1 + 1, cols):
                if temp_board[r1][c] != ' ':
                    break
                if find_path(r1, c, r2, c2, turns_left - 1):
                    return True

            for c in range(c1 - 1, -1, -1):
                if temp_board[r1][c] != ' ':
                    break
                if find_path(r1, c, r2, c2, turns_left - 1):
                    return True

            # Move vertically
            for r in range(r1 + 1, rows):
                if temp_board[r][c1] != ' ':
                    break
                if find_path(r, c1, r2, c2, turns_left - 1):
                    return True

            for r in range(r1 - 1, -1, -1):
                if temp_board[r][c1] != ' ':
                    break
                if find_path(r, c1, r2, c2, turns_left - 1):
                    return True

            return False

        # Temporarily mark the positions as empty for pathfinding
        original_val1 = temp_board[row1][col1]
        original_val2 = temp_board[row2][col2]
        temp_board[row1][col1] = ' '
        temp_board[row2][col2] = ' '

        has_path = find_path(row1, col1, row2, col2, 2)

        # Restore the original values
        temp_board[row1][col1] = original_val1
        temp_board[row2][col2] = original_val2

        return has_path


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
        row1, col1 = pos1
        row2, col2 = pos2
        self.board[row1][col1] = ' '
        self.board[row2][col2] = ' '


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