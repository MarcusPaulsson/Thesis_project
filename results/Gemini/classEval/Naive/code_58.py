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
        mine_map = [[0 for _ in range(self.n)] for _ in range(self.n)]
        mines_positions = random.sample(range(self.n * self.n), self.k)

        for mine_index in mines_positions:
            row = mine_index // self.n
            col = mine_index % self.n
            mine_map[row][col] = 'X'

        for row in range(self.n):
            for col in range(self.n):
                if mine_map[row][col] == 'X':
                    continue
                count = 0
                for i in range(max(0, row - 1), min(self.n, row + 2)):
                    for j in range(max(0, col - 1), min(self.n, col + 2)):
                        if mine_map[i][j] == 'X':
                            count += 1
                mine_map[row][col] = count
        return mine_map

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
        revealed_count = 0
        for i in range(self.n):
            for j in range(self.n):
                if map[i][j] != '-':
                    revealed_count += 1

        return revealed_count == (self.n * self.n - self.k)

    def sweep(self, x, y):
        """
        Sweeps the given position.
        :param x: The x coordinate of the position, int.
        :param y: The y coordinate of the position, int.
        :return: True if the player has won the game, False otherwise,if the game still continues, return the player map, list.
        """
        if self.minesweeper_map[x][y] == 'X':
            return False  # Game over

        self.player_map[x][y] = self.minesweeper_map[x][y]

        if self.check_won(self.player_map):
            return True  # Player wins

        return self.player_map