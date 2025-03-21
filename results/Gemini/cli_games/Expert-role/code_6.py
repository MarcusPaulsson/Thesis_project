import random

class Battleship:
    """
    A command-line Battleship game.
    """

    def __init__(self, grid_size=10, num_ships=5):
        """
        Initializes the game.

        Args:
            grid_size (int): The size of the game board (grid_size x grid_size).
            num_ships (int): The number of ships each player has.
        """
        self.grid_size = grid_size
        self.num_ships = num_ships
        self.player_grid = self._create_grid()
        self.computer_grid = self._create_grid()
        self.player_ships = self._place_ships(self.player_grid)
        self.computer_ships = self._place_ships(self.computer_grid)
        self.player_guesses = set()
        self.computer_guesses = set()

    def _create_grid(self):
        """
        Creates an empty grid for the game.

        Returns:
            list[list[str]]: A 2D list representing the grid.
        """
        return [['.' for _ in range(self.grid_size)] for _ in range(self.grid_size)]

    def _place_ships(self, grid):
        """
        Randomly places ships on the grid.

        Args:
            grid (list[list[str]]): The grid to place the ships on.

        Returns:
            list[tuple[int, int]]: A list of ship coordinates (row, col).
        """
        ships = []
        for _ in range(self.num_ships):
            while True:
                row = random.randint(0, self.grid_size - 1)
                col = random.randint(0, self.grid_size - 1)
                if (row, col) not in ships:
                    ships.append((row, col))
                    break
            grid[row][col] = 'S'  # Mark ship location on the grid (for debugging)
        return ships

    def print_grid(self, grid, hide_ships=True):
        """
        Prints the grid to the console.

        Args:
            grid (list[list[str]]): The grid to print.
            hide_ships (bool): Whether to hide the ships or show them.
        """
        header = "   " + " ".join([chr(65 + i) for i in range(self.grid_size)])
        print(header)
        for i, row in enumerate(grid):
            row_str = str(i).rjust(2) + " "
            for cell in row:
                if hide_ships and cell == 'S':
                    row_str += '. '  # Hide ships from the player
                else:
                    row_str += cell + ' '
            print(row_str)

    def get_player_guess(self):
        """
        Gets a valid guess from the player.

        Returns:
            tuple[int, int]: The player's guess (row, col).
        """
        while True:
            try:
                guess = input(f"Enter your guess (e.g., A0): ").upper()
                if len(guess) < 2 or len(guess) > 3:
                    raise ValueError
                col = ord(guess[0]) - 65
                row = int(guess[1:])

                if not (0 <= row < self.grid_size and 0 <= col < self.grid_size):
                    raise ValueError

                if (row, col) in self.player_guesses:
                    print("You already guessed that location. Try again.")
                    continue

                return row, col

            except ValueError:
                print("Invalid input. Please enter a valid guess (e.g., A0).")

    def computer_turn(self):
        """
        The computer's turn to guess.

        Returns:
            tuple[int, int]: The computer's guess (row, col).
        """
        while True:
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - 1)
            if (row, col) not in self.computer_guesses:
                self.computer_guesses.add((row, col))
                return row, col

    def play_round(self):
        """
        Plays a single round of the game.
        """
        # Player's turn
        print("\nYour Turn:")
        self.print_grid(self.computer_grid)  # Print computer's grid (hidden ships)
        row, col = self.get_player_guess()
        self.player_guesses.add((row, col))

        if (row, col) in self.computer_ships:
            print("Hit!")
            self.computer_grid[row][col] = 'X'  # Mark hit on the computer's grid
            self.computer_ships.remove((row, col))
        else:
            print("Miss!")
            self.computer_grid[row][col] = 'O'  # Mark miss on the computer's grid

        # Computer's turn
        print("\nComputer's Turn:")
        row, col = self.computer_turn()
        print(f"Computer guessed {chr(col + 65)}{row}")

        if (row, col) in self.player_ships:
            print("Computer hit your ship!")
            self.player_grid[row][col] = 'X'  # Mark hit on the player's grid
            self.player_ships.remove((row, col))
        else:
            print("Computer missed!")
            self.player_grid[row][col] = 'O'  # Mark miss on the player's grid

        self.print_grid(self.player_grid, hide_ships=False) #show player their own board

    def check_winner(self):
        """
        Checks if there is a winner.

        Returns:
            str: 'player' if the player won, 'computer' if the computer won, None if no winner.
        """
        if not self.computer_ships:
            return 'player'
        if not self.player_ships:
            return 'computer'
        return None

    def play_game(self):
        """
        The main game loop.
        """
        print("Welcome to Battleship!")
        print(f"Grid size: {self.grid_size}x{self.grid_size}, Number of ships: {self.num_ships}")

        while True:
            self.play_round()
            winner = self.check_winner()

            if winner:
                print(f"\n{winner.capitalize()} wins!")
                if winner == 'player':
                    print("Computer's Board:")
                    self.print_grid(self.computer_grid, hide_ships=False) # Show computer's board
                else:
                    print("Your Board:")
                    self.print_grid(self.player_grid, hide_ships=False) #Show player their own board
                break


if __name__ == '__main__':
    game = Battleship()
    game.play_game()