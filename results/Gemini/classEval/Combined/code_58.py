import random

class MinesweeperGame:
    """
    A class to represent a Minesweeper game.
    """

    def __init__(self, n: int, k: int) -> None:
        """
        Initializes the MinesweeperGame with the board size and number of mines.

        Args:
            n: The size of the board (n x n).
            k: The number of mines to place on the board.
        """
        if not isinstance(n, int) or n <= 0:
            raise ValueError("Board size 'n' must be a positive integer.")
        if not isinstance(k, int) or k < 0 or k > n * n:
            raise ValueError("Number of mines 'k' must be a non-negative integer less than or equal to n*n.")

        self.n = n
        self.k = k
        self.minesweeper_map = self.generate_mine_sweeper_map()
        self.player_map = self.generate_player_map()
        self.score = 0

    def generate_mine_sweeper_map(self) -> list[list[str | int]]:
        """
        Generates the minesweeper map with mines and numbers indicating adjacent mines.

        Returns:
            A 2D list representing the minesweeper map. 'X' denotes a mine, and numbers indicate the
            number of adjacent mines.
        """
        mine_sweeper_map = [[0 for _ in range(self.n)] for _ in range(self.n)]
        mine_positions = random.sample(range(self.n * self.n), self.k)

        # Place mines
        for pos in mine_positions:
            row = pos // self.n
            col = pos % self.n
            mine_sweeper_map[row][col] = 'X'

        # Calculate adjacent mine counts
        for row in range(self.n):
            for col in range(self.n):
                if mine_sweeper_map[row][col] == 'X':
                    continue
                count = self.count_adjacent_mines(mine_sweeper_map, row, col)
                mine_sweeper_map[row][col] = count

        return mine_sweeper_map

    def count_adjacent_mines(self, board: list[list[str | int]], row: int, col: int) -> int:
        """
        Counts the number of mines adjacent to a given cell.

        Args:
            board: The minesweeper board.
            row: The row index of the cell.
            col: The column index of the cell.

        Returns:
            The number of adjacent mines.
        """
        count = 0
        for i in range(max(0, row - 1), min(self.n, row + 2)):
            for j in range(max(0, col - 1), min(self.n, col + 2)):
                if (i, j) != (row, col) and board[i][j] == 'X':
                    count += 1
        return count

    def generate_player_map(self) -> list[list[str]]:
        """
        Generates the player's map, initially filled with hidden cells.

        Returns:
            A 2D list representing the player's map, where each cell is initialized to '-'.
        """
        return [['-' for _ in range(self.n)] for _ in range(self.n)]

    def check_won(self, current_map: list[list[str | int]]) -> bool:
        """
        Checks if the player has won the game.

        Args:
            current_map: The current state of the player's map.

        Returns:
            True if the player has won, False otherwise.  Winning means all non-mine cells are revealed.
        """
        revealed_count = 0
        for row in range(self.n):
            for col in range(self.n):
                if current_map[row][col] != '-':
                    revealed_count += 1

        return revealed_count == self.n * self.n - self.k

    def sweep(self, x: int, y: int) -> bool | list[list[str | int]]:
        """
        Sweeps a cell on the board.

        Args:
            x: The row index of the cell to sweep.
            y: The column index of the cell to sweep.

        Returns:
            False if a mine is hit, True if the game is won after the sweep, and the updated player map
            if the game continues.
        """
        if not (0 <= x < self.n and 0 <= y < self.n):
            raise ValueError("Invalid row or column index.")

        if self.minesweeper_map[x][y] == 'X':
            return False

        self.player_map[x][y] = self.minesweeper_map[x][y]
        self.score += 1

        if self.check_won(self.player_map):
            return True
        else:
            return self.player_map