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
        total_cells = self.BOARD_SIZE[0] * self.BOARD_SIZE[1]
        num_icons = len(self.ICONS)
        num_pairs = total_cells // 2
        icons_needed = [self.ICONS[i % num_icons] for i in range(num_pairs)] * 2
        random.shuffle(icons_needed)

        board = []
        for i in range(self.BOARD_SIZE[0]):
            row = []
            for j in range(self.BOARD_SIZE[1]):
                row.append(icons_needed[i * self.BOARD_SIZE[1] + j])
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
        if not (0 <= pos1[0] < self.BOARD_SIZE[0] and 0 <= pos1[1] < self.BOARD_SIZE[1] and
                0 <= pos2[0] < self.BOARD_SIZE[0] and 0 <= pos2[1] < self.BOARD_SIZE[1]):
            return False

        def is_valid(x, y):
            return 0 <= x < self.BOARD_SIZE[0] and 0 <= y < self.BOARD_SIZE[1]

        def bfs(start, end):
            queue = [(start, [])]  # (position, path)
            visited = {start}

            while queue:
                (x, y), path = queue.pop(0)

                if (x, y) == end:
                    return True

                # Move horizontally
                for ny in range(self.BOARD_SIZE[1]):
                    if (ny < y and all(self.board[x][i] == ' ' for i in range(ny + 1, y))) or \
                       (ny > y and all(self.board[x][i] == ' ' for i in range(y + 1, ny))):
                        new_pos = (x, ny)
                        if new_pos not in visited and (self.board[x][ny] == ' ' or new_pos == end):
                            queue.append((new_pos, path + [new_pos]))
                            visited.add(new_pos)

                # Move vertically
                for nx in range(self.BOARD_SIZE[0]):
                    if (nx < x and all(self.board[i][y] == ' ' for i in range(nx + 1, x))) or \
                       (nx > x and all(self.board[i][y] == ' ' for i in range(x + 1, nx))):
                        new_pos = (nx, y)
                        if new_pos not in visited and (self.board[nx][y] == ' ' or new_pos == end):
                            queue.append((new_pos, path + [new_pos]))
                            visited.add(new_pos)

            return False

        return bfs(pos1, pos2)


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
            if any(icon != ' ' for icon in row):
                return False
        return True