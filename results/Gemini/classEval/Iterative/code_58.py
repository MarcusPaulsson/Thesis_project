import random

class MinesweeperGame:
    """
    Implements a Minesweeper game with mine placement, sweeping, and win condition checking.
    """

    def __init__(self, n, k):
        """
        Initializes the game board and mine positions.

        Args:
            n (int): The size of the board (n x n).
            k (int): The number of mines to place.
        Raises:
            ValueError: If k is greater than or equal to n*n
        """
        if k >= n * n:
            raise ValueError("Number of mines cannot exceed the number of cells.")

        self.n = n
        self.k = k
        self.minesweeper_map = self._generate_mine_sweeper_map()
        self.player_map = self._generate_player_map()
        self.score = 0
        self.game_over = False

    def _generate_mine_sweeper_map(self):
        """
        Generates the hidden minesweeper map with mines and adjacent mine counts.
        """
        mine_map = [[0 for _ in range(self.n)] for _ in range(self.n)]
        mines_placed = 0
        while mines_placed < self.k:
            x = random.randint(0, self.n - 1)
            y = random.randint(0, self.n - 1)
            if mine_map[x][y] == 0:
                mine_map[x][y] = 'X'
                mines_placed += 1

        for i in range(self.n):
            for j in range(self.n):
                if mine_map[i][j] == 'X':
                    continue
                count = 0
                for row in range(max(0, i - 1), min(self.n, i + 2)):
                    for col in range(max(0, j - 1), min(self.n, j + 2)):
                        if mine_map[row][col] == 'X':
                            count += 1
                mine_map[i][j] = count
        return mine_map

    def _generate_player_map(self):
        """
        Generates the player's view of the board, initially filled with hidden cells.
        """
        return [['-' for _ in range(self.n)] for _ in range(self.n)]

    def check_won(self):
        """
        Checks if the player has won the game.
        """
        revealed_count = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.player_map[i][j] != '-':
                    revealed_count += 1
        return revealed_count == self.n * self.n - self.k

    def sweep(self, x, y):
        """
        Sweeps a cell on the board.

        Args:
            x (int): The row index of the cell to sweep.
            y (int): The column index of the cell to sweep.

        Returns:
            bool: True if the game is won, False if game is lost (hit a mine), None if the game continues.
        Raises:
            IndexError: If x or y are out of bounds.
            ValueError: If the cell has already been revealed.
        """
        if not (0 <= x < self.n and 0 <= y < self.n):
            raise IndexError("Coordinates are out of bounds.")

        if self.player_map[x][y] != '-':
            raise ValueError("Cell already revealed.")

        if self.minesweeper_map[x][y] == 'X':
            self.player_map[x][y] = 'X'  # Reveal the mine
            self.game_over = True
            return False  # Game over, player hit a mine
        else:
            self._reveal_cell(x, y)
            if self.check_won():
                return True  # Game won
            else:
                return None # Game continues

    def _reveal_cell(self, x, y):
        """
        Reveals a cell and recursively reveals adjacent empty cells.
        """
        if not (0 <= x < self.n and 0 <= y < self.n) or self.player_map[x][y] != '-':
            return  # Base case: out of bounds or already revealed

        self.player_map[x][y] = self.minesweeper_map[x][y]

        if self.minesweeper_map[x][y] == 0:
            # Recursively reveal adjacent cells
            for row in range(max(0, x - 1), min(self.n, x + 2)):
                for col in range(max(0, y - 1), min(self.n, y + 2)):
                    if row != x or col != y:
                        self._reveal_cell(row, col)

    def print_board(self, show_mines=False):
        """Prints the current state of the game board."""
        board = self.minesweeper_map if show_mines else self.player_map
        for row in board:
            print(' '.join(map(str, row)))