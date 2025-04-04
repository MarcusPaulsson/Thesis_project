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
        num_of_icons = self.BOARD_SIZE[0] * self.BOARD_SIZE[1] // 2
        icons = random.sample(self.ICONS * 2, num_of_icons)
        board = [icons[i:i + self.BOARD_SIZE[1]] for i in range(0, len(icons), self.BOARD_SIZE[1])]
        return board

    def is_valid_move(self, pos1, pos2):
        """
        check if the move of two icons is valid 
        """
        if pos1 == pos2:
            return False
        if not (0 <= pos1[0] < self.BOARD_SIZE[0] and 0 <= pos1[1] < self.BOARD_SIZE[1]):
            return False
        if not (0 <= pos2[0] < self.BOARD_SIZE[0] and 0 <= pos2[1] < self.BOARD_SIZE[1]):
            return False
        if self.board[pos1[0]][pos1[1]] != self.board[pos2[0]][pos2[1]]:
            return False
        return self.has_path(pos1, pos2)

    def has_path(self, pos1, pos2):
        """
        check if there is a path between two icons
        """
        visited = set()

        def dfs(x, y):
            if (x, y) == pos2:
                return True
            visited.add((x, y))
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.BOARD_SIZE[0] and 0 <= ny < self.BOARD_SIZE[1]:
                    if (nx, ny) not in visited and self.board[nx][ny] == self.board[pos1[0]][pos1[1]]:
                        if dfs(nx, ny):
                            return True
            return False

        return dfs(pos1[0], pos1[1])

    def remove_icons(self, pos1, pos2):
        """
        remove the connected icons on the game board
        """
        if self.is_valid_move(pos1, pos2):
            self.board[pos1[0]][pos1[1]] = ' '
            self.board[pos2[0]][pos2[1]] = ' '

    def is_game_over(self):
        """
        Check if the game is over 
        """
        for row in self.board:
            if any(icon != ' ' for icon in row):
                return False
        return True