import random

class Battleship:
    def __init__(self, board_size=10, num_ships=5):
        """
        Initializes the Battleship game.

        Args:
            board_size (int): The size of the game board (e.g., 10 for a 10x10 grid).
            num_ships (int): The number of ships each player has.
        """
        self.board_size = board_size
        self.num_ships = num_ships
        self.player_board = self._create_board()
        self.computer_board = self._create_board()
        self.player_ships = self._place_ships(self.player_board)
        self.computer_ships = self._place_ships(self.computer_board)
        self.player_guesses = set()  # Track player's guesses
        self.computer_guesses = set() # Track computer's guesses
        self.player_ship_locations = set() # Track player ship locations
        self.computer_ship_locations = set() # Track computer ship locations
        for ship in self.player_ships:
            self.player_ship_locations.update(ship)
        for ship in self.computer_ships:
            self.computer_ship_locations.update(ship)


    def _create_board(self):
        """Creates an empty game board."""
        return [['.' for _ in range(self.board_size)] for _ in range(self.board_size)]

    def _place_ships(self, board):
        """Randomly places ships on the board."""
        ships = []
        for _ in range(self.num_ships):
            while True:
                ship_length = random.randint(2, 4)  # Ships of length 2, 3, or 4
                orientation = random.choice(['horizontal', 'vertical'])
                if orientation == 'horizontal':
                    row = random.randint(0, self.board_size - 1)
                    col = random.randint(0, self.board_size - ship_length)
                    positions = [(row, col + i) for i in range(ship_length)]
                else:  # vertical
                    row = random.randint(0, self.board_size - ship_length)
                    col = random.randint(0, self.board_size - 1)
                    positions = [(row + i, col) for i in range(ship_length)]

                # Check for overlap
                valid_placement = True
                for r, c in positions:
                    if board[r][c] == 'S':
                        valid_placement = False
                        break

                if valid_placement:
                    for r, c in positions:
                        board[r][c] = 'S'
                    ships.append(set(positions)) # Store ships as sets of coordinates
                    break
        return ships

    def print_board(self, board, hide_ships=True):
        """Prints the game board."""
        print("  " + " ".join([chr(65 + i) for i in range(self.board_size)]))  # A B C ...
        for i, row in enumerate(board):
            print(str(i).rjust(2) + " " + " ".join(['~' if cell == 'S' and hide_ships else cell for cell in row]))

    def get_player_guess(self):
        """Gets a valid guess from the player."""
        while True:
            try:
                guess = input("Enter your guess (e.g., A0): ").upper()
                if len(guess) < 2:
                    print("Invalid input. Please enter a coordinate like A0 or B5.")
                    continue

                col = ord(guess[0]) - ord('A')
                row = int(guess[1:])

                if not (0 <= row < self.board_size and 0 <= col < self.board_size):
                    print("Invalid coordinates. Please enter valid row and column values.")
                    continue

                if (row, col) in self.player_guesses:
                    print("You already guessed that location. Try again.")
                    continue

                return row, col

            except (ValueError, IndexError):
                print("Invalid input. Please enter a coordinate like A0 or B5.")


    def process_player_guess(self, row, col):
        """Processes the player's guess and updates the computer's board."""
        self.player_guesses.add((row, col))
        if self.computer_board[row][col] == 'S':
            print("Hit!")
            self.computer_board[row][col] = 'X'  # Mark as hit
            for ship in self.computer_ships:
                if (row, col) in ship:
                    ship.remove((row, col))
                    if not ship:
                        print("You sunk a battleship!")
            return True
        else:
            print("Miss!")
            self.computer_board[row][col] = 'O'  # Mark as miss
            return False

    def get_computer_guess(self):
        """Generates a random guess for the computer."""
        while True:
            row = random.randint(0, self.board_size - 1)
            col = random.randint(0, self.board_size - 1)
            if (row, col) not in self.computer_guesses:
                return row, col

    def process_computer_guess(self, row, col):
        """Processes the computer's guess and updates the player's board."""
        self.computer_guesses.add((row, col))
        if self.player_board[row][col] == 'S':
            print("Computer hit your ship at", chr(col + ord('A')) + str(row))
            self.player_board[row][col] = 'X'  # Mark as hit
            for ship in self.player_ships:
                if (row, col) in ship:
                    ship.remove((row, col))
                    if not ship:
                        print("Computer sunk your battleship!")
            return True
        else:
            print("Computer missed at", chr(col + ord('A')) + str(row))
            self.player_board[row][col] = 'O'  # Mark as miss
            return False

    def check_win(self):
        """Checks if either player has won the game."""
        player_ships_sunk = all(not ship for ship in self.player_ships)
        computer_ships_sunk = all(not ship for ship in self.computer_ships)

        if player_ships_sunk:
            print("Computer wins! All your battleships have been sunk.")
            return "computer"
        elif computer_ships_sunk:
            print("You win! All computer's battleships have been sunk.")
            return "player"
        else:
            return None

    def play_game(self):
        """Plays the Battleship game."""
        print("Welcome to Battleship!")
        print("Your board:")
        self.print_board(self.player_board)
        print("\nComputer's board:")
        self.print_board(self.computer_board, hide_ships=True)  # Hide computer's ships initially

        while True:
            # Player's turn
            print("\nYour turn:")
            row, col = self.get_player_guess()
            self.process_player_guess(row, col)
            print("\nComputer's board:")
            self.print_board(self.computer_board, hide_ships=True)

            winner = self.check_win()
            if winner:
                break

            # Computer's turn
            print("\nComputer's turn:")
            row, col = self.get_computer_guess()
            self.process_computer_guess(row, col)
            print("\nYour board:")
            self.print_board(self.player_board)

            winner = self.check_win()
            if winner:
                break



if __name__ == '__main__':
    game = Battleship()
    game.play_game()