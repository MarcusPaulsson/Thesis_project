class TicTacToe:
    """
    The class represents a game of Tic-Tac-Toe and its functions include making a move on the board, checking for a winner, and determining if the board is full.
    """

    def __init__(self, N=3):
        """
        Initialize a game board with all empty spaces and the starting player.
        :param N: int, the size of the board (N x N), default is 3
        """
        self.N = N
        self.board = [[' ' for _ in range(N)] for _ in range(N)]
        self.current_player = 'X'

    def make_move(self, row, col):
        """
        Place the current player's mark at the specified position on the board and switch the player.
        :param row: int, the row index of the position (0-indexed)
        :param col: int, the column index of the position (0-indexed)
        :return: bool, indicating whether the move was successful or not
        """
        if not (0 <= row < self.N and 0 <= col < self.N):
            return False  # Invalid move: out of bounds
        if self.board[row][col] != ' ':
            return False  # Invalid move: space already occupied

        self.board[row][col] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return True

    def check_winner(self):
        """
        Check if there is a winner on the board.
        :return: str or None, the mark of the winner ('X' or 'O'), or None if there is no winner yet
        """

        # Check rows
        for row in range(self.N):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != ' ':
                return self.board[row][0]

        # Check columns
        for col in range(self.N):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        return None

    def is_board_full(self):
        """
        Check if the game board is completely filled.
        :return: bool, indicating whether the game board is full or not
        """
        for row in range(self.N):
            for col in range(self.N):
                if self.board[row][col] == ' ':
                    return False
        return True

    def print_board(self):
        """Prints the current state of the board."""
        for row in self.board:
            print("|" + "|".join(row) + "|")


if __name__ == '__main__':
    ttt = TicTacToe()
    moves = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0)]  # Corrected moves to win for X
    for move in moves:
        if ttt.make_move(move[0], move[1]):
            ttt.print_board()
        else:
            print(f"Invalid move at {move}")
            break
    winner = ttt.check_winner()
    if winner:
        print(f"The winner is {winner}!")
    elif ttt.is_board_full():
        print("It's a draw!")
    else:
        print("The game is still in progress.")