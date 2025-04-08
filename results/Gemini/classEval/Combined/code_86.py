class TicTacToe:
    """
    The class represents a game of Tic-Tac-Toe.
    It includes functions for making a move, checking for a winner, and determining if the board is full.
    """

    def __init__(self, N=3):
        """
        Initializes the game board.

        Args:
            N (int): The size of the board (N x N). Defaults to 3.
        """
        self.N = N
        self.board = [[' ' for _ in range(N)] for _ in range(N)]
        self.current_player = 'X'

    def make_move(self, row, col):
        """
        Places the current player's mark at the specified position on the board and switches to the other player.

        Args:
            row (int): The row index of the position (0-indexed).
            col (int): The column index of the position (0-indexed).

        Returns:
            bool: True if the move was successful, False otherwise (invalid row/col or cell already occupied).
        """
        if not (0 <= row < self.N and 0 <= col < self.N):
            return False

        if self.board[row][col] != ' ':
            return False

        self.board[row][col] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return True

    def check_winner(self):
        """
        Checks if there is a winner on the board.

        Returns:
            str or None: The mark of the winner ('X' or 'O'), or None if there is no winner yet.
        """

        # Check rows
        for row in range(self.N):
            if self.board[row][0] != ' ' and all(self.board[row][col] == self.board[row][0] for col in range(self.N)):
                return self.board[row][0]

        # Check columns
        for col in range(self.N):
            if self.board[0][col] != ' ' and all(self.board[row][col] == self.board[0][col] for row in range(self.N)):
                return self.board[0][col]

        # Check main diagonal
        if self.board[0][0] != ' ' and all(self.board[i][i] == self.board[0][0] for i in range(self.N)):
            return self.board[0][0]

        # Check secondary diagonal
        if self.board[0][self.N - 1] != ' ' and all(self.board[i][self.N - 1 - i] == self.board[0][self.N - 1] for i in range(self.N)):
            return self.board[0][self.N - 1]

        return None

    def is_board_full(self):
        """
        Checks if the game board is completely filled.

        Returns:
            bool: True if the board is full, False otherwise.
        """
        for row in range(self.N):
            for col in range(self.N):
                if self.board[row][col] == ' ':
                    return False
        return True