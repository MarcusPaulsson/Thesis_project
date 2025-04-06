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
        :raises ValueError: If the number of mines exceeds the number of available cells.
        """
        if k > n * n:
            raise ValueError("Number of mines cannot exceed the number of cells in the board.")
        self.n = n
        self.k = k
        self.minesweeper_map = self.generate_mine_sweeper_map()
        self.player_map = self.generate_player_map()
        
    def generate_mine_sweeper_map(self):
        """
        Generates a minesweeper map with the given size of the board and the number of mines.
        :return: The minesweeper map, list.
        """
        board = [[0 for _ in range(self.n)] for _ in range(self.n)]
        mines = random.sample(range(self.n * self.n), self.k)

        for mine in mines:
            x, y = divmod(mine, self.n)
            board[x][y] = 'X'
            for i in range(max(0, x - 1), min(self.n, x + 2)):
                for j in range(max(0, y - 1), min(self.n, y + 2)):
                    if board[i][j] != 'X':
                        board[i][j] += 1
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
        :return: "Game Over" if the player hits a mine, True if the player has won the game, otherwise the player map.
        :raises IndexError: If the coordinates are out of bounds.
        """
        if not (0 <= x < self.n) or not (0 <= y < self.n):
            raise IndexError("Coordinates out of bounds.")
        
        if self.minesweeper_map[x][y] == 'X':
            return "Game Over"
        
        self.player_map[x][y] = self.minesweeper_map[x][y]
        
        if self.check_won():
            return True
        
        return self.player_map