import random

class MinesweeperGame:
    """
    This class implements a Minesweeper game, including mine placement, sweeping, and win checking.
    """

    def __init__(self, n: int, k: int) -> None:
        """
        Initializes the MinesweeperGame class with the size of the board and the number of mines.
        :param n: The size of the board (n x n).
        :param k: The number of mines.
        """
        self.n = n
        self.k = k
        self.minesweeper_map = self._generate_mine_sweeper_map()
        self.player_map = self._generate_player_map()
        self.score = 0

    def _generate_mine_sweeper_map(self) -> list:
        """
        Generates a minesweeper map with the specified size and number of mines.
        :return: The minesweeper map as a 2D list.
        """
        board = [['0' for _ in range(self.n)] for _ in range(self.n)]
        mines = set()

        while len(mines) < self.k:
            x, y = random.randint(0, self.n - 1), random.randint(0, self.n - 1)
            if (x, y) not in mines:
                mines.add((x, y))
                board[x][y] = 'X'
                self._update_adjacent_cells(board, x, y)

        return board

    def _update_adjacent_cells(self, board: list, x: int, y: int) -> None:
        """
        Updates the adjacent cells around a mine.
        :param board: The current minesweeper board.
        :param x: The x coordinate of the mine.
        :param y: The y coordinate of the mine.
        """
        for i in range(max(0, x - 1), min(self.n, x + 2)):
            for j in range(max(0, y - 1), min(self.n, y + 2)):
                if board[i][j] != 'X':
                    board[i][j] = str(int(board[i][j]) + 1)

    def _generate_player_map(self) -> list:
        """
        Generates a player map with the specified size.
        :return: The player map as a 2D list.
        """
        return [['-' for _ in range(self.n)] for _ in range(self.n)]

    def check_won(self) -> bool:
        """
        Checks whether the player has won the game.
        :return: True if the player has won, False otherwise.
        """
        for i in range(self.n):
            for j in range(self.n):
                if self.player_map[i][j] == '-' and self.minesweeper_map[i][j] != 'X':
                    return False
        return True

    def sweep(self, x: int, y: int):
        """
        Sweeps the specified position.
        :param x: The x coordinate of the position.
        :param y: The y coordinate of the position.
        :return: True if the player has won, False if a mine was hit, or the current player map if the game continues.
        """
        if self.minesweeper_map[x][y] == 'X':
            return False  # Hit a mine

        self.player_map[x][y] = self.minesweeper_map[x][y]
        self.score += 1

        if self.check_won():
            return True

        return self.player_map