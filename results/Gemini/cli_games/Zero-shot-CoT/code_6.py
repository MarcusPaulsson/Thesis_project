import random

class Battleship:
    def __init__(self, grid_size=10, num_ships=5, ship_lengths=[2, 3, 3, 4, 5]):
        self.grid_size = grid_size
        self.num_ships = num_ships
        self.ship_lengths = ship_lengths
        self.player_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
        self.computer_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
        self.computer_ships = []
        self.player_ships = []
        self.player_guesses = set()
        self.computer_guesses = set()
        self.ship_symbols = ['S' for _ in range(num_ships)]  # Use 'S' for ship representation
        self.player_ships_placed = False

    def print_grid(self, grid):
        """Prints the given grid to the console."""
        header = "   " + " ".join([chr(65 + i) for i in range(self.grid_size)])
        print(header)
        for i, row in enumerate(grid):
            print(f"{i+1:2} {' '.join(row)}")

    def place_ship(self, grid, ship_length, ship_symbol, is_computer=False):
        """Places a ship of given length on the grid."""
        while True:
            if is_computer:
                orientation = random.choice(['horizontal', 'vertical'])
                row = random.randint(0, self.grid_size - 1)
                col = random.randint(0, self.grid_size - 1)
            else:
                orientation = input("Enter orientation (horizontal or vertical): ").lower()
                row = int(input("Enter starting row (1-{}): ".format(self.grid_size))) - 1
                col = ord(input("Enter starting column (A-{}): ".format(chr(65 + self.grid_size - 1))).upper()) - 65

            if orientation not in ['horizontal', 'vertical']:
                print("Invalid orientation. Please enter 'horizontal' or 'vertical'.")
                continue

            if row < 0 or row >= self.grid_size or col < 0 or col >= self.grid_size:
                print("Invalid coordinates.  Please enter valid coordinates within the grid.")
                continue

            if (orientation == 'horizontal' and col + ship_length > self.grid_size) or \
               (orientation == 'vertical' and row + ship_length > self.grid_size):
                print("Ship placement exceeds grid boundaries.")
                continue

            # Check for collisions
            valid_placement = True
            if orientation == 'horizontal':
                for i in range(ship_length):
                    if grid[row][col + i] != '.':
                        valid_placement = False
                        break
            else:  # vertical
                for i in range(ship_length):
                    if grid[row + i][col] != '.':
                        valid_placement = False
                        break

            if not valid_placement:
                print("Ship overlaps with another ship.  Try again.")
                continue

            # Place the ship
            if orientation == 'horizontal':
                for i in range(ship_length):
                    grid[row][col + i] = ship_symbol
            else:  # vertical
                for i in range(ship_length):
                    grid[row + i][col] = ship_symbol

            # Store ship coordinates
            ship_coordinates = []
            if orientation == 'horizontal':
                for i in range(ship_length):
                    ship_coordinates.append((row, col + i))
            else:
                for i in range(ship_length):
                    ship_coordinates.append((row + i, col))

            return ship_coordinates

    def place_computer_ships(self):
        """Places the computer's ships randomly on the grid."""
        for i, length in enumerate(self.ship_lengths):
            ship_coordinates = self.place_ship(self.computer_grid, length, self.ship_symbols[i], is_computer=True)
            self.computer_ships.append(ship_coordinates)

    def place_player_ships(self):
        """Places the player's ships based on user input."""
        print("Place your ships:")
        for i, length in enumerate(self.ship_lengths):
            print(f"Placing ship of length {length}:")
            self.print_grid(self.player_grid)
            ship_coordinates = self.place_ship(self.player_grid, length, self.ship_symbols[i])
            self.player_ships.append(ship_coordinates)
        self.player_ships_placed = True
        print("Your ships have been placed:")
        self.print_grid(self.player_grid)

    def get_player_guess(self):
        """Gets the player's guess from the console."""
        while True:
            try:
                guess_str = input("Enter your guess (e.g., A1): ").upper()
                col = ord(guess_str[0]) - 65
                row = int(guess_str[1:]) - 1
                if row < 0 or row >= self.grid_size or col < 0 or col >= self.grid_size:
                    print("Invalid coordinates.  Please enter valid coordinates within the grid.")
                    continue
                if (row, col) in self.player_guesses:
                    print("You already guessed that location. Try again.")
                    continue
                return row, col
            except (ValueError, IndexError):
                print("Invalid input. Please enter a guess in the format A1, B2, etc.")

    def handle_player_turn(self):
        """Handles the player's turn."""
        row, col = self.get_player_guess()
        self.player_guesses.add((row, col))

        if self.computer_grid[row][col] != '.':
            print("Hit!")
            self.computer_grid[row][col] = 'X'  # Mark hit on the computer's grid
            # Check if ship is sunk
            for ship in self.computer_ships:
                if (row, col) in ship:
                    ship.remove((row, col))
                    if not ship:
                        print("You sunk a computer's ship!")
                        self.computer_ships.remove(ship)
                    break

        else:
            print("Miss!")
            self.computer_grid[row][col] = 'O'  # Mark miss on the computer's grid

    def computer_make_guess(self):
        """The computer makes a guess."""
        while True:
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - 1)
            if (row, col) not in self.computer_guesses:
                self.computer_guesses.add((row, col))
                return row, col

    def handle_computer_turn(self):
        """Handles the computer's turn."""
        row, col = self.computer_make_guess()
        print(f"Computer guesses {chr(col + 65)}{row + 1}")

        if self.player_grid[row][col] != '.':
            print("Computer hit your ship!")
            self.player_grid[row][col] = 'X'  # Mark hit on the player's grid

            # Check if ship is sunk
            for ship in self.player_ships:
                if (row, col) in ship:
                    ship.remove((row, col))
                    if not ship:
                        print("Computer sunk one of your ships!")
                        self.player_ships.remove(ship)
                    break

        else:
            print("Computer missed!")
            self.player_grid[row][col] = 'O'  # Mark miss on the player's grid

    def check_game_over(self):
        """Checks if the game is over."""
        if not self.computer_ships:
            print("Congratulations! You sunk all the computer's ships!")
            return True
        if not self.player_ships:
            print("Game over! The computer sunk all your ships!")
            return True
        return False

    def play_game(self):
        """Main game loop."""
        print("Welcome to Battleship!")
        self.place_computer_ships()
        self.place_player_ships()

        while True:
            print("\nYour turn:")
            print("Your Grid:")
            self.print_grid(self.player_grid)
            print("Computer's Grid:")
            self.print_grid(self.computer_grid)
            self.handle_player_turn()

            if self.check_game_over():
                break

            print("\nComputer's turn:")
            self.handle_computer_turn()

            if self.check_game_over():
                break

if __name__ == "__main__":
    game = Battleship()
    game.play_game()