import random

class MinesweeperGame:
    """
    This class implements a Minesweeper game, including game setup, sweeping functionality, 
    and win detection.
    """

    def __init__(self, n: int, k: int) -> None:
        """
        Initializes the MinesweeperGame class with the size of the board and the number of mines.
        :param n: Size of the board (n x n).
        :param k: Number of mines to place on the board.
        """
        self.n = n
        self.k = k
        self.minesweeper_map = self._generate_mine_sweeper_map()
        self.player_map = self._generate_player_map()
        self.score = 0

    def _generate_mine_sweeper_map(self) -> list:
        """
        Generates a minesweeper map with the given size and number of mines.
        :return: A 2D list representing the minesweeper map.
        """
        board = [[0 for _ in range(self.n)] for _ in range(self.n)]
        mine_positions = random.sample(range(self.n * self.n), self.k)
        for pos in mine_positions:
            x, y = divmod(pos, self.n)
            board[x][y] = 'X'
            self._update_adjacent_cells(board, x, y)
        return board

    def _update_adjacent_cells(self, board: list, x: int, y: int) -> None:
        """
        Updates the counts of adjacent cells around a mine.
        :param board: The current minesweeper board.
        :param x: The x-coordinate of the mine.
        :param y: The y-coordinate of the mine.
        """
        for i in range(max(0, x-1), min(self.n, x+2)):
            for j in range(max(0, y-1), min(self.n, y+2)):
                if board[i][j] != 'X':
                    board[i][j] += 1

    def _generate_player_map(self) -> list:
        """
        Generates an initial player map with all positions hidden.
        :return: A 2D list representing the player map.
        """
        return [['-' for _ in range(self.n)] for _ in range(self.n)]

    def check_won(self) -> bool:
        """
        Checks whether the player has won the game by uncovering all non-mine cells.
        :return: True if the player has won, otherwise False.
        """
        for i in range(self.n):
            for j in range(self.n):
                if self.player_map[i][j] == '-' and self.minesweeper_map[i][j] != 'X':
                    return False
        return True

    def sweep(self, x: int, y: int) -> list or bool:
        """
        Sweeps the given position on the board.
        :param x: The x-coordinate of the position.
        :param y: The y-coordinate of the position.
        :return: True if the player has won, False if a mine was hit, otherwise the updated player map.
        """
        if self.minesweeper_map[x][y] == 'X':
            return False
        
        self.player_map[x][y] = self.minesweeper_map[x][y]
        self.score += 1
        
        if self.check_won():
            return True
        
        return self.player_map