import random

class Battleship:
    def __init__(self, board_size=10, num_ships=5):
        self.board_size = board_size
        self.num_ships = num_ships
        self.player_board = self.create_board()
        self.computer_board = self.create_board()
        self.player_ships = self.place_ships(self.player_board)
        self.computer_ships = self.place_ships(self.computer_board)
        self.player_guesses = set()
        self.computer_guesses = set()

    def create_board(self):
        """Creates an empty game board."""
        return [['.' for _ in range(self.board_size)] for _ in range(self.board_size)]

    def place_ships(self, board):
        """Randomly places ships on the board."""
        ships = []
        for _ in range(self.num_ships):
            while True:
                row = random.randint(0, self.board_size - 1)
                col = random.randint(0, self.board_size - 1)
                orientation = random.choice(['horizontal', 'vertical'])
                ship_length = random.randint(2, 4)  # Ships can be 2-4 units long

                if self.is_valid_placement(board, row, col, orientation, ship_length):
                    ship = []
                    if orientation == 'horizontal':
                        for i in range(ship_length):
                            board[row][col + i] = 'S'
                            ship.append((row, col + i))
                    else:
                        for i in range(ship_length):
                            board[row + i][col] = 'S'
                            ship.append((row + i, col))
                    ships.append(ship)
                    break
        return ships

    def is_valid_placement(self, board, row, col, orientation, ship_length):
        """Checks if a ship placement is valid."""
        if orientation == 'horizontal':
            if col + ship_length > self.board_size:
                return False
            for i in range(ship_length):
                if board[row][col + i] != '.':
                    return False
        else:
            if row + ship_length > self.board_size:
                return False
            for i in range(ship_length):
                if board[row + i][col] != '.':
                    return False
        return True

    def print_board(self, board, hide_ships=True):
        """Prints the board to the console."""
        print("  " + " ".join([chr(65 + i) for i in range(self.board_size)]))  # Print column letters
        for i, row in enumerate(board):
            row_str = str(i).rjust(2) + " "  # Row number, right-aligned
            for cell in row:
                if hide_ships and cell == 'S':
                    row_str += '. '
                else:
                    row_str += cell + " "
            print(row_str)

    def get_player_guess(self):
        """Gets a valid guess from the player."""
        while True:
            try:
                guess = input("Enter your guess (e.g., A3): ").upper()
                if len(guess) < 2 or len(guess) > 3:
                    raise ValueError
                col = ord(guess[0]) - ord('A')
                row = int(guess[1:])
                if not (0 <= row < self.board_size and 0 <= col < self.board_size):
                    raise ValueError
                if (row, col) in self.player_guesses:
                    print("You already guessed that location.")
                    continue
                return row, col
            except ValueError:
                print("Invalid guess.  Enter a coordinate like A3 or B7.")
            except IndexError:
                print("Invalid guess. Enter a valid coordinate. ")

    def computer_guess(self):
        """Generates a random guess for the computer."""
        while True:
            row = random.randint(0, self.board_size - 1)
            col = random.randint(0, self.board_size - 1)
            if (row, col) not in self.computer_guesses:
                return row, col

    def check_hit(self, board, ships, row, col):
        """Checks if a guess is a hit."""
        for ship in ships:
            if (row, col) in ship:
                return True
        return False

    def update_board(self, board, row, col, hit):
        """Updates the board with a hit or miss."""
        if hit:
            board[row][col] = 'X'
        else:
            board[row][col] = 'O'

    def sink_ship(self, ships, row, col):
        """Checks if a ship has been sunk."""
        for ship in ships:
            if (row, col) in ship:
                ship.remove((row, col))
                if not ship:
                    return True
                break
        return False

    def all_ships_sunk(self, ships):
        """Checks if all ships have been sunk."""
        return all(not ship for ship in ships)

    def play_game(self):
        """Main game loop."""
        print("Welcome to Battleship!")
        print("Board size:", self.board_size)
        print("Number of ships:", self.num_ships)
        print("Ships are of length 2-4")
        print("Try to sink all of the computer's ships.")

        while True:
            # Player's turn
            print("\nYour Board:")
            self.print_board(self.player_board)
            print("\nComputer's Board:")
            self.print_board(self.computer_board, hide_ships=True)

            print("\nYour Turn:")
            row, col = self.get_player_guess()
            self.player_guesses.add((row, col))

            hit = self.check_hit(self.computer_board, self.computer_ships, row, col)
            self.update_board(self.computer_board, row, col, hit)

            if hit:
                print("Hit!")
                if self.sink_ship(self.computer_ships, row, col):
                    print("You sunk a ship!")
                if self.all_ships_sunk(self.computer_ships):
                    print("\nCongratulations! You sunk all the computer's ships!")
                    break
            else:
                print("Miss!")

            # Computer's turn
            print("\nComputer's Turn:")
            row, col = self.computer_guess()
            self.computer_guesses.add((row, col))

            hit = self.check_hit(self.player_board, self.player_ships, row, col)
            self.update_board(self.player_board, row, col, hit)

            if hit:
                print("Computer hit your ship!")
                if self.sink_ship(self.player_ships, row, col):
                    print("Computer sunk one of your ships!")
                if self.all_ships_sunk(self.player_ships):
                    print("\nComputer sunk all of your ships! You lose!")
                    break
            else:
                print("Computer missed!")


if __name__ == "__main__":
    game = Battleship()
    game.play_game()