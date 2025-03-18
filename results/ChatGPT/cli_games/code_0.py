class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_player = 'X'  # Starting player

    def print_board(self):
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("--+---+--")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("--+---+--")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

    def is_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
            (0, 4, 8), (2, 4, 6)               # Diagonal
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True
        return False

    def is_full(self):
        return ' ' not in self.board

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        while True:
            self.print_board()
            try:
                move = int(input(f"Player {self.current_player}, enter a position (1-9): ")) - 1
                if move < 0 or move > 8:
                    print("Invalid position! Please enter a number between 1 and 9.")
                    continue
                if not self.make_move(move):
                    print("Position already taken! Try again.")
                    continue
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 9.")
                continue

            if self.is_winner():
                self.print_board()
                print(f"Player {self.current_player} wins!")
                break

            if self.is_full():
                self.print_board()
                print("It's a tie!")
                break

            self.switch_player()

if __name__ == "__main__":
    game = TicTacToe()
    game.play()