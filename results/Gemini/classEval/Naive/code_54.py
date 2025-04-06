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
        icons = (self.ICONS * ((rows * cols) // num_icons // 2 + 1) * 2)[:rows * cols]
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
        if not (0 <= pos1[0] < self.BOARD_SIZE[0] and 0 <= pos1[1] < self.BOARD_SIZE[1] and
                0 <= pos2[0] < self.BOARD_SIZE[0] and 0 <= pos2[1] < self.BOARD_SIZE[1]):
            return False

        if pos1 == pos2:
            return False

        if self.board[pos1[0]][pos1[1]] != self.board[pos2[0]][pos2[1]]:
            return False

        if self.board[pos1[0]][pos1[1]] == ' ':
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
        rows, cols = self.BOARD_SIZE
        board = [row[:] for row in self.board]

        def is_valid(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def find_path(p1, p2, turns):
            if turns > 2:
                return False

            if p1 == p2:
                return True

            r, c = p1
            
            # Move horizontally
            for new_c in range(c + 1, cols):
                if (new_c,r) == (pos2[1], pos2[0]):
                  if board[r][new_c] == board[pos2[0]][pos2[1]] or board[r][new_c] == ' ':
                    if board[r][new_c] == board[pos2[0]][pos2[1]]:
                      return True
                    else:
                      return True
                if board[r][new_c] != ' ':
                    break
                if find_path((r, new_c), p2, turns + 1):
                    return True

            for new_c in range(c - 1, -1, -1):
                if (new_c,r) == (pos2[1], pos2[0]):
                  if board[r][new_c] == board[pos2[0]][pos2[1]] or board[r][new_c] == ' ':
                    if board[r][new_c] == board[pos2[0]][pos2[1]]:
                      return True
                    else:
                      return True
                if board[r][new_c] != ' ':
                    break
                if find_path((r, new_c), p2, turns + 1):
                    return True

            # Move vertically
            for new_r in range(r + 1, rows):
                if (c, new_r) == (pos2[1], pos2[0]):
                  if board[new_r][c] == board[pos2[0]][pos2[1]] or board[new_r][c] == ' ':
                    if board[new_r][c] == board[pos2[0]][pos2[1]]:
                      return True
                    else:
                      return True
                if board[new_r][c] != ' ':
                    break
                if find_path((new_r, c), p2, turns + 1):
                    return True

            for new_r in range(r - 1, -1, -1):
                if (c, new_r) == (pos2[1], pos2[0]):
                  if board[new_r][c] == board[pos2[0]][pos2[1]] or board[new_r][c] == ' ':
                    if board[new_r][c] == board[pos2[0]][pos2[1]]:
                      return True
                    else:
                      return True
                if board[new_r][c] != ' ':
                    break
                if find_path((new_r, c), p2, turns + 1):
                    return True

            return False

        return find_path(pos1, pos2, 0)

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