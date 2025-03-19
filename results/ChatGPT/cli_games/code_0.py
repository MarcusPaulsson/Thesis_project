class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_winner = None  # Keep track of the winner!

    def print_board(self):
        for i in range(3):
            print('|'.join(self.board[i * 3:(i + 1) * 3]))
            if i < 2:
                print('-' * 5)

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

    def play(self):
        print("Welcome to Tic-Tac-Toe!")
        self.print_board()
        letter = 'X'
        while self.empty_squares():
            move = input(f"{letter}'s turn. Enter a position (0-8): ")
            try:
                move = int(move)
                if move not in self.available_moves():
                    print("Invalid move. Try again.")
                    continue
                self.make_move(move, letter)
                self.print_board()
                if self.current_winner:
                    print(f"{letter} wins!")
                    return
                letter = 'O' if letter == 'X' else 'X'
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 8.")
        print("It's a tie!")

if __name__ == '__main__':
    game = TicTacToe()
    game.play()