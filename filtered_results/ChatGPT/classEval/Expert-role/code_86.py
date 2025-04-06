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
        self.size = N

    def make_move(self, row, col):
        """
        Place the current player's mark at the specified position on the board and switch the mark.
        :param row: int, the row index of the position
        :param col: int, the column index of the position
        :return: bool, indicating whether the move was successful or not
        """
        if row < 0 or row >= self.size or col < 0 or col >= self.size or self.board[row][col] != ' ':
            return False
        self.board[row][col] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return True

    def check_winner(self):
        """
        Check if there is a winner on the board in rows, columns and diagonals.
        :return: str or None, the mark of the winner ('X' or 'O'), or None if there is no winner yet
        """
        lines = []
        # Check rows and columns
        for i in range(self.size):
            lines.append(self.board[i])  # Rows
            lines.append([self.board[j][i] for j in range(self.size)])  # Columns

        # Check diagonals
        lines.append([self.board[i][i] for i in range(self.size)])  # Main diagonal
        lines.append([self.board[i][self.size - 1 - i] for i in range(self.size)])  # Anti diagonal

        for line in lines:
            if line[0] != ' ' and all(cell == line[0] for cell in line):
                return line[0]
        return None

    def is_board_full(self):
        """
        Check if the game board is completely filled.
        :return: bool, indicating whether the game board is full or not
        """
        return all(cell != ' ' for row in self.board for cell in row)