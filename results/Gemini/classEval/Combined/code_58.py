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
        :return: The minesweeper map, list of lists.
        """
        minesweeper_map = [[0 for _ in range(self.n)] for _ in range(self.n)]
        mine_positions = random.sample(range(self.n * self.n), self.k)

        for mine_position in mine_positions:
            row = mine_position // self.n
            col = mine_position % self.n
            minesweeper_map[row][col] = 'X'

        for row in range(self.n):
            for col in range(self.n):
                if minesweeper_map[row][col] == 'X':
                    continue
                count = self.count_adjacent_mines(minesweeper_map, row, col)
                minesweeper_map[row][col] = count

        return minesweeper_map

    def count_adjacent_mines(self, grid, row, col):
        """Counts the number of mines adjacent to a given cell."""
        count = 0
        for i in range(max(0, row - 1), min(self.n, row + 2)):
            for j in range(max(0, col - 1), min(self.n, col + 2)):
                if (i, j) != (row, col) and grid[i][j] == 'X':
                    count += 1
        return count

    def generate_playerMap(self):
        """
        Generates a player map with the given size of the board.
        '-' represents the unknown position.
        :return: The player map, list of lists.
        """
        return [['-' for _ in range(self.n)] for _ in range(self.n)]

    def check_won(self, player_map):
        """
        Checks whether the player has won the game.
        The player wins if all non-mine cells are revealed.
        :return: True if the player has won the game, False otherwise.
        """
        revealed_count = 0
        for i in range(self.n):
            for j in range(self.n):
                if player_map[i][j] != '-':
                    revealed_count += 1
        return revealed_count == self.n * self.n - self.k

    def sweep(self, x, y):
        """
        Sweeps the given position.
        :param x: The x coordinate of the position, int.
        :param y: The y coordinate of the position, int.
        :return:
            - False if the player hits a mine.
            - True if the player wins the game.
            - The updated player map if the game continues.
        """
        if self.minesweeper_map[x][y] == 'X':
            return False
        else:
            self.player_map[x][y] = self.minesweeper_map[x][y]
            self.score += 1
            if self.check_won(self.player_map):
                return True
            else:
                return self.player_map