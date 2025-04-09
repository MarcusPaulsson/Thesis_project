import random

class MinesweeperGame:
    """
    This is a class that implements mine sweeping games including minesweeping and winning judgment.
    """

    def __init__(self, n, k) -> None:
        """
        Initializes the MinesweeperGame class with the size of the board and the number of mines.
        :param n: The size of the board, int.
        :param k: The number of mines, int.
        """
        self.n = n
        self.k = k
        self.minesweeper_map = self.generate_mine_sweeper_map()
        self.player_map = self.generate_playerMap()
        self.score = 0

    def generate_mine_sweeper_map(self):
        """
        Generates a minesweeper map with the given size of the board and the number of mines.
        'X' represents the mine, other numbers represent the number of mines around the position.
        :return: The minesweeper map, list.
        """
        board = [['0' for _ in range(self.n)] for _ in range(self.n)]
        mines = random.sample(range(self.n * self.n), self.k)
        for mine in mines:
            row = mine // self.n
            col = mine % self.n
            board[row][col] = 'X'

        for r in range(self.n):
            for c in range(self.n):
                if board[r][c] == 'X':
                    continue
                count = 0
                for i in range(max(0, r - 1), min(self.n, r + 2)):
                    for j in range(max(0, c - 1), min(self.n, c + 2)):
                        if board[i][j] == 'X':
                            count += 1
                board[r][c] = str(count)
        return board

    def generate_playerMap(self):
        """
        Generates a player map with the given size of the board, '-' represents the unknown position.
        :return: The player map, list.
        """
        return [['-' for _ in range(self.n)] for _ in range(self.n)]

    def check_won(self, map):
        """
        Checks whether the player has won the game.
        :return: True if the player has won the game, False otherwise.
        """
        for row in map:
            for cell in row:
                if cell == '-':
                    return False
        return True

    def sweep(self, x, y):
        """
        Sweeps the given position.
        :param x: The x coordinate of the position, int.
        :param y: The y coordinate of the position, int.
        :return: True if the player has won the game, False otherwise,
                 if the game still continues, return the player map, list.
        """
        if self.minesweeper_map[x][y] == 'X':
            return False

        self.player_map[x][y] = self.minesweeper_map[x][y]
        self.score += 1

        if self.check_won(self.player_map):
            return True

        return self.player_map