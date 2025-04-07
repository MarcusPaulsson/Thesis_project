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
        if n <= 0 or k < 0 or k > n * n:
            raise ValueError("Invalid board size or number of mines.")
        
        self.n = n
        self.k = k
        self.minesweeper_map = self.generate_mine_sweeper_map()
        self.player_map = self.generate_player_map()
        self.score = 0

    def generate_mine_sweeper_map(self):
        """
        Generates a minesweeper map with the given size of the board and the number of mines.
        :return: The minesweeper map, list.
        """
        board = [[0 for _ in range(self.n)] for _ in range(self.n)]
        mines = set()

        while len(mines) < self.k:
            x = random.randint(0, self.n - 1)
            y = random.randint(0, self.n - 1)
            if (x, y) not in mines:
                mines.add((x, y))
                board[x][y] = 'X'
        
        for x, y in mines:
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if 0 <= x + dx < self.n and 0 <= y + dy < self.n and board[x + dx][y + dy] != 'X':
                        board[x + dx][y + dy] += 1

        return board

    def generate_player_map(self):
        """
        Generates a player map with the given size of the board.
        :return: The player map, list.
        """
        return [['-' for _ in range(self.n)] for _ in range(self.n)]

    def check_won(self):
        """
        Checks whether the player has won the game.
        :return: True if the player has won the game, False otherwise.
        """
        for i in range(self.n):
            for j in range(self.n):
                if self.player_map[i][j] == '-' and self.minesweeper_map[i][j] != 'X':
                    return False
        return True

    def sweep(self, x, y):
        """
        Sweeps the given position.
        :param x: The x coordinate of the position, int.
        :param y: The y coordinate of the position, int.
        :return: True if the player has won the game, False if hit a mine, else returns the updated player map.
        """
        if self.minesweeper_map[x][y] == 'X':
            return False
        
        self.player_map[x][y] = self.minesweeper_map[x][y]
        self.score += 1
        
        if self.check_won():
            return True
        
        return self.player_map