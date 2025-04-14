class TicTacToe:
    """
    The class represents a game of Tic-Tac-Toe and its functions include making a move on the board, 
    checking for a winner, and determining if the board is full.
    """

    def __init__(self, size=3):
        """
        Initialize a game board with all empty spaces and set the current player to 'X'.
        :param size: int, the size of the game board (default is 3 for a standard Tic-Tac-Toe)
        """
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.current_player = 'X'

    def make_move(self, row, col):
        """
        Place the current player's mark at the specified position on the board and switch players.
        :param row: int, the row index of the position
        :param col: int, the column index of the position
        :return: bool, indicating whether the move was successful or not
        """
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def is_valid_move(self, row, col):
        """
        Validate if a move is within bounds and the position is empty.
        :param row: int, the row index of the position
        :param col: int, the column index of the position
        :return: bool, indicating whether the move is valid
        """
        return 0 <= row < self.size and 0 <= col < self.size and self.board[row][col] == ' '

    def check_winner(self):
        """
        Check if there is a winner on the board in rows, columns, and diagonals.
        :return: str or None, the mark of the winner ('X' or 'O'), or None if there is no winner yet
        """
        lines = self.board + list(zip(*self.board))  # Rows + Columns
        lines.append([self.board[i][i] for i in range(self.size)])  # Main diagonal
        lines.append([self.board[i][self.size - 1 - i] for i in range(self.size)])  # Secondary diagonal

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