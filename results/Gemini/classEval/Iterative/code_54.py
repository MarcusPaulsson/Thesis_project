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
        board = []
        total_cells = self.BOARD_SIZE[0] * self.BOARD_SIZE[1]
        num_pairs = total_cells // 2
        
        # Ensure enough icons are provided
        if len(self.ICONS) == 0:
            raise ValueError("ICONS list cannot be empty.")
        
        # Repeat icons to create enough pairs
        icons = (self.ICONS * (num_pairs // len(self.ICONS))) + self.ICONS[:num_pairs % len(self.ICONS)]
        icons = icons * 2  # Double for pairs
        random.shuffle(icons)

        # Populate the board
        icon_index = 0
        for i in range(self.BOARD_SIZE[0]):
            row = []
            for j in range(self.BOARD_SIZE[1]):
                row.append(icons[icon_index])
                icon_index += 1
            board.append(row)
        return board

    def is_valid_move(self, pos1, pos2):
        """
        check if the move of two icons is valid (i.e. positions are within the game board range, the two positions are not the same, the two positions have the same icon, and there is a valid path between the two positions)
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return:True or False ,representing whether the move of two icons is valid
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
        """
        if not (0 <= pos1[0] < self.BOARD_SIZE[0] and 0 <= pos1[1] < self.BOARD_SIZE[1] and
                0 <= pos2[0] < self.BOARD_SIZE[0] and 0 <= pos2[1] < self.BOARD_SIZE[1]):
            return False

        def is_valid(x, y):
            return 0 <= x < self.BOARD_SIZE[0] and 0 <= y < self.BOARD_SIZE[1]

        def bfs(start, end):
            queue = [(start, [])]
            visited = {start}

            while queue:
                (x, y), path = queue.pop(0)

                if (x, y) == end:
                    return True

                # Move up
                for i in range(x - 1, -1, -1):
                    if (i, y) == end:
                        return True
                    if self.board[i][y] != ' ' and (i, y) != start:
                        break
                    if (i, y) not in visited:
                        queue.append(((i, y), path + [(i, y)]))
                        visited.add((i, y))

                # Move down
                for i in range(x + 1, self.BOARD_SIZE[0]):
                    if (i, y) == end:
                        return True
                    if self.board[i][y] != ' ' and (i, y) != start:
                        break
                    if (i, y) not in visited:
                        queue.append(((i, y), path + [(i, y)]))
                        visited.add((i, y))

                # Move left
                for j in range(y - 1, -1, -1):
                    if (x, j) == end:
                        return True
                    if self.board[x][j] != ' ' and (x, j) != start:
                        break
                    if (x, j) not in visited:
                        queue.append(((x, j), path + [(x, j)]))
                        visited.add((x, j))

                # Move right
                for j in range(y + 1, self.BOARD_SIZE[1]):
                    if (x, j) == end:
                        return True
                    if self.board[x][j] != ' ' and (x, j) != start:
                        break
                    if (x, j) not in visited:
                        queue.append(((x, j), path + [(x, j)]))
                        visited.add((x, j))

            return False

        return bfs(pos1, pos2)


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