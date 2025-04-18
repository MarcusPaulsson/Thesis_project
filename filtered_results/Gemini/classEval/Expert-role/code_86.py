class TicTacToe:
    """
    The class represents a game of Tic-Tac-Toe and its functions include making a move on the board, checking for a winner, and determining if the board is full.
    """

    def __init__(self, N=3):
        """
        Initialize a 3x3 game board with all empty spaces and current symble player, default is 'X'.
        """
        self.board = [[' ' for _ in range(N)] for _ in range(N)]
        self.current_player = 'X'
        self.N = N

    def make_move(self, row, col):
        """
        Place the current player's mark at the specified position on the board and switch the mark.
        :param row: int, the row index of the position
        :param col: int, the column index of the position
        :return: bool, indicating whether the move was successful or not
        >>> ttt.current_player
        'X'
        >>> ttt.make_move(1, 1)
        >>> ttt.current_player
        'O'
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
        Check if there is a winner on the board in rows, columns and diagonals three directions
        :return: str or None, the mark of the winner ('X' or 'O'), or None if there is no winner yet
        >>> moves = [(1, 0), (2, 0), (1, 1), (2, 1), (1, 2)]
        >>> for move in moves:
        ...     ttt.make_move(move[0], move[1])
        >>> ttt.check_winner()
        'X'
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
        Check if the game board is completely filled.
        :return: bool, indicating whether the game board is full or not
        >>> ttt.is_board_full()
        False
        """
        return all(self.board[row][col] != ' ' for row in range(self.N) for col in range(self.N))