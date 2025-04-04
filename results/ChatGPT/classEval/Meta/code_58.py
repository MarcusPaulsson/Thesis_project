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
        self.player_map = self.generate_player_map()
        self.score = 0

    def generate_mine_sweeper_map(self):
        """
        Generates a minesweeper map with the given size of the board and the number of mines.
        :return: The minesweeper map, list.
        """
        board = [[0 for _ in range(self.n)] for _ in range(self.n)]
        mines_placed = 0
        
        while mines_placed < self.k:
            x, y = random.randint(0, self.n - 1), random.randint(0, self.n - 1)
            if board[x][y] == 0:
                board[x][y] = 'X'
                mines_placed += 1
                for i in range(max(0, x-1), min(self.n, x+2)):
                    for j in range(max(0, y-1), min(self.n, y+2)):
                        if board[i][j] != 'X':
                            board[i][j] += 1
        return board

    def generate_player_map(self):
        """
        Generates a player map with the given size of the board.
        :return: The player map, list.
        """
        return [['-' for _ in range(self.n)] for _ in range(self.n)]

    def check_won(self, map):
        """
        Checks whether the player has won the game.
        :return: True if the player has won the game, False otherwise.
        """
        for i in range(self.n):
            for j in range(self.n):
                if map[i][j] == '-' and self.minesweeper_map[i][j] != 'X':
                    return False
        return True

    def sweep(self, x, y):
        """
        Sweeps the given position.
        :param x: The x coordinate of the position, int.
        :param y: The y coordinate of the position, int.
        :return: True if the player has won the game, False otherwise, if the game still continues, return the player map, list.
        """
        if self.minesweeper_map[x][y] == 'X':
            return "Game Over! You hit a mine."
        
        self.player_map[x][y] = self.minesweeper_map[x][y]
        
        if self.check_won(self.player_map):
            return True
        
        return self.player_map