import random

class Battleship:
    def __init__(self):
        self.board_size = 5
        self.board = [['~'] * self.board_size for _ in range(self.board_size)]
        self.ship_position = self.place_ship()
        self.guesses = []
        self.max_guesses = 7

    def place_ship(self):
        x = random.randint(0, self.board_size - 1)
        y = random.randint(0, self.board_size - 1)
        return (x, y)

    def print_board(self):
        print("Current Board:")
        for row in self.board:
            print(" ".join(row))
        print()

    def make_guess(self, x, y):
        if (x, y) in self.guesses:
            print("You've already guessed that position.")
            return False

        self.guesses.append((x, y))

        if (x, y) == self.ship_position:
            print("Congratulations! You sunk my battleship!")
            return True
        else:
            print("Miss!")
            self.board[x][y] = 'X'
            return False

    def is_game_over(self):
        return len(self.guesses) >= self.max_guesses

    def start_game(self):
        print("Welcome to Battleship!")
        while True:
            self.print_board()
            print(f"You have {self.max_guesses - len(self.guesses)} guesses left.")
            try:
                x = int(input("Enter your guess row (0-4): "))
                y = int(input("Enter your guess column (0-4): "))
            except ValueError:
                print("Please enter valid integers.")
                continue

            if x < 0 or x >= self.board_size or y < 0 or y >= self.board_size:
                print("Guess out of bounds. Please try again.")
                continue

            if self.make_guess(x, y):
                self.print_board()
                break

            if self.is_game_over():
                print("Game Over! You've run out of guesses.")
                print(f"The ship was at {self.ship_position}.")
                self.print_board()
                break


if __name__ == "__main__":
    game = Battleship()
    game.start_game()