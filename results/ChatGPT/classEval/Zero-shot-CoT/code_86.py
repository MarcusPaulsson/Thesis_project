class TicTacToe:
    """
    The class represents a game of Tic-Tac-Toe and its functions include making a move on the board, checking for a winner, and determining if the board is full.
    """

    def __init__(self, N=3):
        """
        Initialize a 3x3 game board with all empty spaces and current symbol player, default is 'X'.
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
        """
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_winner(self):
        """
        Check if there is a winner on the board in rows, columns and diagonals.
        :return: str or None, the mark of the winner ('X' or 'O'), or None if there is no winner yet
        """
        for i in range(self.N):
            if all(self.board[i][j] == 'X' for j in range(self.N)):
                return 'X'
            if all(self.board[i][j] == 'O' for j in range(self.N)):
                return 'O'
        
        for j in range(self.N):
            if all(self.board[i][j] == 'X' for i in range(self.N)):
                return 'X'
            if all(self.board[i][j] == 'O' for i in range(self.N)):
                return 'O'
        
        if all(self.board[i][i] == 'X' for i in range(self.N)):
            return 'X'
        if all(self.board[i][i] == 'O' for i in range(self.N)):
            return 'O'
        
        if all(self.board[i][self.N - 1 - i] == 'X' for i in range(self.N)):
            return 'X'
        if all(self.board[i][self.N - 1 - i] == 'O' for i in range(self.N)):
            return 'O'
        
        return None

    def is_board_full(self):
        """
        Check if the game board is completely filled.
        :return: bool, indicating whether the game board is full or not
        """
        return all(self.board[i][j] != ' ' for i in range(self.N) for j in range(self.N))