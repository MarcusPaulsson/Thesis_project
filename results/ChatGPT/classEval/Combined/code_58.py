import random

class MinesweeperGame:
    """
    This class implements a Minesweeper game, including the mechanics for sweeping, winning judgment, and map generation.
    """

    def __init__(self, size: int, mine_count: int) -> None:
        """
        Initializes the Minesweeper game with a board of given size and number of mines.
        
        :param size: The size of the board (size x size).
        :param mine_count: The number of mines to place on the board.
        """
        self.size = size
        self.mine_count = mine_count
        self.minesweeper_map = self._generate_mine_sweeper_map()
        self.player_map = self._generate_player_map()
        self.score = 0

    def _generate_mine_sweeper_map(self) -> list:
        """
        Generates the minesweeper map with mines and numbers indicating adjacent mines.
        
        :return: The minesweeper map as a list of lists.
        """
        board = [[0 for _ in range(self.size)] for _ in range(self.size)]
        mines = set()

        while len(mines) < self.mine_count:
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            if (x, y) not in mines:
                mines.add((x, y))
                board[x][y] = 'X'  # Place a mine

                # Increment surrounding mine counts
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if 0 <= x + dx < self.size and 0 <= y + dy < self.size and board[x + dx][y + dy] != 'X':
                            board[x + dx][y + dy] += 1

        return board

    def _generate_player_map(self) -> list:
        """
        Generates a player map to track the player's progress.
        
        :return: The player map initialized with '-' for unrevealed cells.
        """
        return [['-' for _ in range(self.size)] for _ in range(self.size)]

    def check_won(self) -> bool:
        """
        Checks if the player has won the game by revealing all non-mine cells.
        
        :return: True if the player has won, otherwise False.
        """
        for row in range(self.size):
            for col in range(self.size):
                if self.player_map[row][col] == '-' and (row, col) not in self.get_mines():
                    return False
        return True

    def get_mines(self) -> set:
        """ Helper method to extract mine positions from the minesweeper map. """
        return {(i, j) for i in range(self.size) for j in range(self.size) if self.minesweeper_map[i][j] == 'X'}

    def sweep(self, x: int, y: int):
        """
        Sweeps the cell at the given position.
        
        :param x: The x coordinate of the cell.
        :param y: The y coordinate of the cell.
        :return: True if the player has won, False if a mine is hit, or the player map if the game continues.
        """
        if self.minesweeper_map[x][y] == 'X':
            return False  # Hit a mine

        self.player_map[x][y] = self.minesweeper_map[x][y]
        self.score += 1

        if self.check_won():
            return True  # Player wins

        return self.player_map  # Game continues