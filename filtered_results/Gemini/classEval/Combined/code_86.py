class TicTacToe:
    """
    The class represents a game of Tic-Tac-Toe and its functions include making a move on the board, checking for a winner, and determining if the board is full.
    """

    def __init__(self, N=3):
        """
        Initialize a 3x3 game board with all empty spaces and current player, default is 'X'.
        """
        self.board = [[' ' for _ in range(N)] for _ in range(N)]
        self.current_player = 'X'
        self.size = N

    def make_move(self, row, col):
        """
        Place the current player's mark at the specified position on the board and switch the player.
        :param row: int, the row index of the position
        :param col: int, the column index of the position
        :return: bool, indicating whether the move was successful or not
        """
        if not (0 <= row < self.size and 0 <= col < self.size):
            return False

        if self.board[row][col] != ' ':
            return False

        self.board[row][col] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return True

    def check_winner(self):
        """
        Check if there is a winner on the board in rows, columns and diagonals.
        :return: str or None, the mark of the winner ('X' or 'O'), or None if there is no winner yet
        """
        # Check rows
        for row in range(self.size):
            if self.board[row][0] != ' ' and all(self.board[row][col] == self.board[row][0] for col in range(self.size)):
                return self.board[row][0]

        # Check columns
        for col in range(self.size):
            if self.board[0][col] != ' ' and all(self.board[row][col] == self.board[0][col] for row in range(self.size)):
                return self.board[0][col]

        # Check main diagonal
        if self.board[0][0] != ' ' and all(self.board[i][i] == self.board[0][0] for i in range(self.size)):
            return self.board[0][0]

        # Check secondary diagonal
        if self.board[0][self.size - 1] != ' ' and all(self.board[i][self.size - 1 - i] == self.board[0][self.size - 1] for i in range(self.size)):
            return self.board[0][self.size - 1]

        return None

    def is_board_full(self):
        """
        Check if the game board is completely filled.
        :return: bool, indicating whether the game board is full or not
        """
        return all(self.board[row][col] != ' ' for row in range(self.size) for col in range(self.size))