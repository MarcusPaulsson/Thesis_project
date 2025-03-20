class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_player = 'X'  # Starting player

    def display_board(self):
        print("Current board:")
        for i in range(3):
            print(f"{self.board[i * 3]} | {self.board[i * 3 + 1]} | {self.board[i * 3 + 2]}")
            if i < 2:
                print("---------")

    def player_move(self):
        valid_move = False
        while not valid_move:
            try:
                move = int(input(f"Player {self.current_player}, enter your move (1-9): ")) - 1
                if 0 <= move < 9 and self.board[move] == ' ':
                    self.board[move] = self.current_player
                    valid_move = True
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter a number between 1 and 9.")

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
            (0, 4, 8), (2, 4, 6)              # diagonal
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]
        return None

    def is_board_full(self):
        return ' ' not in self.board

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play_game(self):
        while True:
            self.display_board()
            self.player_move()
            winner = self.check_winner()
            if winner:
                self.display_board()
                print(f"Player {winner} wins!")
                break
            if self.is_board_full():
                self.display_board()
                print("It's a tie!")
                break
            self.switch_player()


if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()