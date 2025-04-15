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
        Generates a minesweeper map with the given size of the board and the number of mines,the given parameter n is the size of the board,the size of the board is n*n,the parameter k is the number of mines,'X' represents the mine,other numbers represent the number of mines around the position.
        :return: The minesweeper map, list.
        """
        mine_positions = random.sample(range(self.n * self.n), self.k)
        minesweeper_map = [['0' for _ in range(self.n)] for _ in range(self.n)]

        for pos in mine_positions:
            row = pos // self.n
            col = pos % self.n
            minesweeper_map[row][col] = 'X'

        for i in range(self.n):
            for j in range(self.n):
                if minesweeper_map[i][j] == 'X':
                    continue
                count = 0
                for x in range(max(0, i - 1), min(self.n, i + 2)):
                    for y in range(max(0, j - 1), min(self.n, j + 2)):
                        if minesweeper_map[x][y] == 'X':
                            count += 1
                minesweeper_map[i][j] = str(count)

        return minesweeper_map

    def generate_playerMap(self):
        """
        Generates a player map with the given size of the board, the given parameter n is the size of the board,the size of the board is n*n,the parameter k is the number of mines,'-' represents the unknown position.
        :return: The player map, list.
        """
        return [['-' for _ in range(self.n)] for _ in range(self.n)]

    def check_won(self,map):
        """
        Checks whether the player has won the game,if there are just mines in the player map,return True,otherwise return False.
        :return: True if the player has won the game, False otherwise.
        """
        for i in range(self.n):
            for j in range(self.n):
                if self.minesweeper_map[i][j] != 'X' and map[i][j] == '-':
                    return False
        return True

    def sweep(self, x, y):
        """
        Sweeps the given position.
        :param x: The x coordinate of the position, int.
        :param y: The y coordinate of the position, int.
        :return: True if the player has won the game, False otherwise,if the game still continues, return the player map, list.
        """
        if self.minesweeper_map[x][y] == 'X':
            return False

        self.player_map[x][y] = self.minesweeper_map[x][y]
        self.score += 1

        if self.check_won(self.player_map):
            return True

        return self.player_map