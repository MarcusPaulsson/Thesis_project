class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_player = 'X'

    def print_board(self):
        print("Current board:")
        for i in range(3):
            print(f"{self.board[i * 3]} | {self.board[i * 3 + 1]} | {self.board[i * 3 + 2]}")
            if i < 2:
                print("---------")
        print()

    def is_winner(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
            [0, 4, 8], [2, 4, 6]              # diagonal
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                return True
        return False

    def is_board_full(self):
        return ' ' not in self.board

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            if not self.is_winner():
                self.current_player = 'O' if self.current_player == 'X' else 'X'
            else:
                self.print_board()
                print(f"Player {self.current_player} wins!")
                return True
        else:
            print("Invalid move, try again.")
        return False

    def play(self):
        while True:
            self.print_board()
            try:
                move = int(input(f"Player {self.current_player}, enter your move (0-8): "))
                if move < 0 or move > 8:
                    print("Invalid input, please enter a number between 0 and 8.")
                    continue
            except ValueError:
                print("Invalid input, please enter a number between 0 and 8.")
                continue

            if self.make_move(move):
                break

            if self.is_board_full():
                self.print_board()
                print("It's a draw!")
                break


if __name__ == "__main__":
    game = TicTacToe()
    game.play()