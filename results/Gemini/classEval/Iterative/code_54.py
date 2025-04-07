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
        num_tiles = self.BOARD_SIZE[0] * self.BOARD_SIZE[1]
        num_icons = len(self.ICONS)
        pairs_needed = num_tiles // 2
        
        if pairs_needed * 2 != num_tiles:
            raise ValueError("Board size must allow for an even number of tiles to form pairs.")

        icons = self.ICONS * (pairs_needed // num_icons)
        remaining = pairs_needed % num_icons
        icons += self.ICONS[:remaining]
        
        icons = icons * 2  # Double the icons to create pairs
        random.shuffle(icons)

        board = []
        for i in range(self.BOARD_SIZE[0]):
            row = []
            for j in range(self.BOARD_SIZE[1]):
                row.append(icons[i * self.BOARD_SIZE[1] + j])
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

        if pos1 == pos2:
            return True 

        def find_path(p1, p2):
            q = [(p1, [])]
            visited = {p1}
            rows, cols = self.BOARD_SIZE

            while q:
                (x, y), path = q.pop(0)

                if (x, y) == p2:
                    return True

                # Move up
                for i in range(x - 1, -1, -1):
                    if (i, y) == p2 or self.board[i][y] == ' ':
                        if (i, y) not in visited:
                            q.append(((i, y), path + [(i, y)]))
                            visited.add((i, y))
                    else:
                        break

                # Move down
                for i in range(x + 1, rows):
                    if (i, y) == p2 or self.board[i][y] == ' ':
                        if (i, y) not in visited:
                            q.append(((i, y), path + [(i, y)]))
                            visited.add((i, y))
                    else:
                        break

                # Move left
                for j in range(y - 1, -1, -1):
                    if (x, j) == p2 or self.board[x][j] == ' ':
                        if (x, j) not in visited:
                            q.append(((x, j), path + [(x, j)]))
                            visited.add((x, j))
                    else:
                        break

                # Move right
                for j in range(y + 1, cols):
                    if (x, j) == p2 or self.board[x][j] == ' ':
                        if (x, j) not in visited:
                            q.append(((x, j), path + [(x, j)]))
                            visited.add((x, j))
                    else:
                        break
            return False

        temp1 = self.board[pos1[0]][pos1[1]]
        temp2 = self.board[pos2[0]][pos2[1]]

        self.board[pos1[0]][pos1[1]] = ' '
        self.board[pos2[0]][pos2[1]] = ' '
        has_path = find_path(pos1,pos2)
        self.board[pos1[0]][pos1[1]] = temp1
        self.board[pos2[0]][pos2[1]] = temp2
        return has_path

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