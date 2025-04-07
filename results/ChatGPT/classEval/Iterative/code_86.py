class TicTacToe:
    """
    The class represents a game of Tic-Tac-Toe and its functions include making a move on the board, checking for a winner, and determining if the board is full.
    """

    def __init__(self, N=3):
        """
        Initialize a NxN game board with all empty spaces and current symbol player, default is 'X'.
        """
        self.N = N
        self.board = [[' ' for _ in range(N)] for _ in range(N)]
        self.current_player = 'X'

    def make_move(self, row, col):
        """
        Place the current player's mark at the specified position on the board and switch the mark.
        :param row: int, the row index of the position
        :param col: int, the column index of the position
        :return: bool, indicating whether the move was successful or not
        """
        if 0 <= row < self.N and 0 <= col < self.N and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_winner(self):
        """
        Check if there is a winner on the board in rows, columns and diagonals.
        :return: str or None, the mark of the winner ('X' or 'O'), or None if there is no winner yet
        """
        # Check rows
        for row in self.board:
            if row.count(row[0]) == self.N and row[0] != ' ':
                return row[0]
        
        # Check columns
        for col in range(self.N):
            if all(self.board[row][col] == self.board[0][col] for row in range(self.N)) and self.board[0][col] != ' ':
                return self.board[0][col]
        
        # Check diagonals
        if all(self.board[i][i] == self.board[0][0] for i in range(self.N)) and self.board[0][0] != ' ':
            return self.board[0][0]
        if all(self.board[i][self.N-1-i] == self.board[0][self.N-1] for i in range(self.N)) and self.board[0][self.N-1] != ' ':
            return self.board[0][self.N-1]

        return None

    def is_board_full(self):
        """
        Check if the game board is completely filled.
        :return: bool, indicating whether the game board is full or not
        """
        return all(cell != ' ' for row in self.board for cell in row)