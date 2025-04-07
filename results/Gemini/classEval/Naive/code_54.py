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
        num_icons = self.BOARD_SIZE[0] * self.BOARD_SIZE[1] // 2
        icons_needed = self.ICONS * (num_icons // len(self.ICONS)) + self.ICONS[:num_icons % len(self.ICONS)]
        icons = icons_needed * 2
        random.shuffle(icons)
        board = []
        for i in range(self.BOARD_SIZE[0]):
            row = []
            for j in range(self.BOARD_SIZE[1]):
                row.append(icons.pop())
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
        if not (0 <= pos1[0] < self.BOARD_SIZE[0] and 0 <= pos1[1] < self.BOARD_SIZE[1] and
                0 <= pos2[0] < self.BOARD_SIZE[0] and 0 <= pos2[1] < self.BOARD_SIZE[1]):
            return False

        if pos1 == pos2:
            return False

        if self.board[pos1[0]][pos1[1]] == ' ' or self.board[pos2[0]][pos2[1]] == ' ':
            return False

        if self.board[pos1[0]][pos1[1]] != self.board[pos2[0]][pos2[1]]:
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
        def is_valid(x, y):
            return 0 <= x < self.BOARD_SIZE[0] and 0 <= y < self.BOARD_SIZE[1]

        def find_path(curr, end, visited, turns):
            if curr == end:
                return True

            if turns > 2:
                return False

            x, y = curr
            if (x, y, turns) in visited:
                return False
            visited.add((x, y, turns))

            # Move horizontally
            for dy in [-1, 1]:
                ny = y + dy
                while is_valid(x, ny):
                    if (x, ny) == end and (self.board[x][ny] == self.board[pos1[0]][pos1[1]] or self.board[x][ny] == ' '):
                        return True
                    if self.board[x][ny] != ' ' and (x, ny) != end:
                        break
                    if find_path((x, ny), end, visited.copy(), turns + 1 if dy != (ny - y) else turns):
                        return True
                    ny += dy

            # Move vertically
            for dx in [-1, 1]:
                nx = x + dx
                while is_valid(nx, y):
                    if (nx, y) == end and (self.board[nx][y] == self.board[pos1[0]][pos1[1]] or self.board[nx][y] == ' '):
                        return True
                    if self.board[nx][y] != ' ' and (nx, y) != end:
                        break
                    if find_path((nx, y), end, visited.copy(), turns + 1 if dx != (nx - x) else turns):
                        return True
                    nx += dx

            return False
        if self.board[pos1[0]][pos1[1]] == ' ' or self.board[pos2[0]][pos2[1]] == ' ':
            return False
        if pos1 == pos2:
            return True

        return find_path(pos1, pos2, set(), 0)

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
        self.board[pos1[0]][pos1[1]] = ' '
        self.board[pos2[0]][pos2[1]] = ' '


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