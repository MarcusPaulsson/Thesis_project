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
        mines = set()

        while len(mines) < self.k:
            x, y = random.randint(0, self.n - 1), random.randint(0, self.n - 1)
            if (x, y) not in mines:
                mines.add((x, y))
                board[x][y] = 'X'
                self.update_adjacent_cells(board, x, y)

        return board

    def update_adjacent_cells(self, board, x, y):
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if 0 <= x + dx < self.n and 0 <= y + dy < self.n and board[x + dx][y + dy] != 'X':
                    board[x + dx][y + dy] += 1

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
        for row in self.player_map:
            for cell in row:
                if cell == '-' and not self.is_mine(cell):
                    return False
        return True

    def is_mine(self, cell):
        return cell == 'X'

    def sweep(self, x, y):
        """
        Sweeps the given position.
        :param x: The x coordinate of the position, int.
        :param y: The y coordinate of the position, int.
        :return: True if the player has won the game, False otherwise, or the player map.
        """
        if self.minesweeper_map[x][y] == 'X':
            return "Game Over! You hit a mine."
        
        self.player_map[x][y] = self.minesweeper_map[x][y]
        if self.check_won():
            return True

        return self.player_map