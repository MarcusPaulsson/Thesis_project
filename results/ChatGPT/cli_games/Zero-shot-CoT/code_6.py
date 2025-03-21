import random

class Battleship:
    def __init__(self):
        self.board_size = 5
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.ship_position = self.place_ship()
        self.guesses = 0
        self.max_guesses = 10
        self.game_over = False

    def place_ship(self):
        x = random.randint(0, self.board_size - 1)
        y = random.randint(0, self.board_size - 1)
        return (x, y)

    def print_board(self):
        print("  " + " ".join(str(i) for i in range(self.board_size)))
        for idx, row in enumerate(self.board):
            print(idx, " ".join(row))

    def make_guess(self, x, y):
        if self.game_over:
            print("Game over! Start a new game.")
            return

        if x < 0 or x >= self.board_size or y < 0 or y >= self.board_size:
            print("Invalid coordinates! Try again.")
            return

        self.guesses += 1

        if (x, y) == self.ship_position:
            print("Congratulations! You've sunk the battleship!")
            self.board[x][y] = 'X'
            self.game_over = True
        else:
            print("Miss!")
            self.board[x][y] = 'O'

        if self.guesses >= self.max_guesses:
            print("Game over! You've run out of guesses.")
            self.game_over = True

        self.print_board()

    def reset_game(self):
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.ship_position = self.place_ship()
        self.guesses = 0
        self.game_over = False
        print("Game reset! Start guessing again.")

def main():
    game = Battleship()
    game.print_board()

    while not game.game_over:
        try:
            guess = input("Enter your guess (row and column, e.g., 2 3): ")
            if guess.lower() == 'reset':
                game.reset_game()
                continue
            x, y = map(int, guess.split())
            game.make_guess(x, y)
        except ValueError:
            print("Invalid input! Please enter row and column as numbers.")

if __name__ == "__main__":
    main()