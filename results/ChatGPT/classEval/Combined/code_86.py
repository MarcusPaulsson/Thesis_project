class TicTacToe:
    """
    The class represents a game of Tic-Tac-Toe and its functions include making a move on the board, 
    checking for a winner, and determining if the board is full.
    """

    def __init__(self, size=3):
        """
        Initialize a game board of given size with all empty spaces and set the current player to 'X'.
        :param size: int, the dimension of the game board (size x size)
        """
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.current_player = 'X'

    def make_move(self, row, col):
        """
        Place the current player's mark at the specified position on the board and switch the mark.
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
        Check if the proposed move is valid.
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
        for i in range(self.size):
            # Check rows
            if self.all_equal(self.board[i]):
                return self.board[i][0]
            # Check columns
            if self.all_equal([self.board[j][i] for j in range(self.size)]):
                return self.board[0][i]

        # Check diagonals
        if self.all_equal([self.board[i][i] for i in range(self.size)]):
            return self.board[0][0]
        if self.all_equal([self.board[i][self.size - 1 - i] for i in range(self.size)]):
            return self.board[0][self.size - 1]

        return None

    def all_equal(self, lst):
        """
        Check if all elements in the list are the same and not empty.
        :param lst: list, the list to check
        :return: bool, indicating whether all elements are equal and not empty
        """
        return lst[0] != ' ' and all(x == lst[0] for x in lst)

    def is_board_full(self):
        """
        Check if the game board is completely filled.
        :return: bool, indicating whether the game board is full or not
        """
        return all(cell != ' ' for row in self.board for cell in row)