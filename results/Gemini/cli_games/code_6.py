import random

class Battleship:
    def __init__(self, size=10):
        self.size = size
        self.player_board = self.create_board()
        self.computer_board = self.create_board()
        self.player_ships = []
        self.computer_ships = []
        self.ship_lengths = [5, 4, 3, 3, 2]  # Carrier, Battleship, Cruiser, Submarine, Destroyer
        self.player_guesses = set()
        self.computer_guesses = set()

    def create_board(self):
        return [['~' for _ in range(self.size)] for _ in range(self.size)]

    def print_board(self, board, hide_ships=True):
        header = "   " + " ".join([chr(65 + i) for i in range(self.size)])
        print(header)
        for i, row in enumerate(board):
            row_str = f"{i+1:2} " + " ".join(['~' if hide_ships and cell == 'S' else cell for cell in row])
            print(row_str)

    def place_ships(self, board, ships, is_player=True):
        for length in self.ship_lengths:
            while True:
                if is_player:
                    print(f"\nPlacing ship of length {length}.")
                    orientation = input("Enter orientation (H for horizontal, V for vertical): ").upper()
                    while orientation not in ('H', 'V'):
                        orientation = input("Invalid orientation. Enter H or V: ").upper()
                    try:
                        row = int(input("Enter starting row (1-{}): ".format(self.size))) - 1
                        col = ord(input("Enter starting column (A-{}): ".format(chr(64+self.size))).upper()) - 65
                        if not (0 <= row < self.size and 0 <= col < self.size):
                            print("Invalid coordinates. Try again.")
                            continue
                    except ValueError:
                        print("Invalid input. Please enter a number for the row and a letter for the column.")
                        continue

                else:
                    orientation = random.choice(['H', 'V'])
                    row = random.randint(0, self.size - 1)
                    col = random.randint(0, self.size - 1)

                if self.is_valid_placement(board, row, col, orientation, length):
                    self.place_ship(board, row, col, orientation, length)
                    if is_player:
                        ships.append((row, col, orientation, length))
                    else:
                        ships.append((row, col, orientation, length))
                    break
                else:
                    if is_player:
                        print("Invalid placement. Ship overlaps or goes out of bounds. Try again.")

    def is_valid_placement(self, board, row, col, orientation, length):
        if orientation == 'H':
            if col + length > self.size:
                return False
            for i in range(length):
                if board[row][col + i] == 'S':
                    return False
        else:  # orientation == 'V'
            if row + length > self.size:
                return False
            for i in range(length):
                if board[row + i][col] == 'S':
                    return False
        return True

    def place_ship(self, board, row, col, orientation, length):
        if orientation == 'H':
            for i in range(length):
                board[row][col + i] = 'S'
        else:  # orientation == 'V'
            for i in range(length):
                board[row + i][col] = 'S'

    def get_player_guess(self):
        while True:
            try:
                row = int(input("Enter row to strike (1-{}): ".format(self.size))) - 1
                col = ord(input("Enter column to strike (A-{}): ".format(chr(64+self.size))).upper()) - 65
                if not (0 <= row < self.size and 0 <= col < self.size):
                    print("Invalid coordinates. Try again.")
                    continue
                if (row, col) in self.player_guesses:
                    print("You've already guessed that location. Try again.")
                    continue
                return row, col
            except ValueError:
                print("Invalid input. Please enter a number for the row and a letter for the column.")

    def computer_guess(self):
        while True:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            if (row, col) not in self.computer_guesses:
                return row, col

    def check_hit(self, board, row, col):
        if board[row][col] == 'S':
            board[row][col] = 'X'  # Mark as hit
            return True
        elif board[row][col] == '~':
            board[row][col] = 'O'  # Mark as miss
            return False
        else:
            return False  # Already hit or missed

    def is_sunk(self, board, ships, row, col):
        for ship_row, ship_col, orientation, length in ships:
            if orientation == 'H':
                if ship_row == row and ship_col <= col < ship_col + length:
                    # Check if all parts of the ship are hit
                    sunk = all(board[ship_row][ship_col + i] == 'X' for i in range(length))
                    return sunk
            else:  # orientation == 'V'
                if ship_col == col and ship_row <= row < ship_row + length:
                    # Check if all parts of the ship are hit
                    sunk = all(board[ship_row + i][ship_col] == 'X' for i in range(length))
                    return sunk
        return False

    def all_ships_sunk(self, board):
        for row in board:
            if 'S' in row:
                return False
        return True

    def play(self):
        print("Welcome to Battleship!")

        # Player setup
        print("\nPlayer, place your ships:")
        self.place_ships(self.player_board, self.player_ships, is_player=True)

        # Computer setup
        print("\nComputer placing ships...")
        self.place_ships(self.computer_board, self.computer_ships, is_player=False)

        turn = 0
        while True:
            turn += 1
            print(f"\n--- Turn {turn} ---")

            # Player's turn
            print("\nYour board:")
            self.print_board(self.player_board)
            print("\nComputer's board (your guesses):")
            self.print_board(self.computer_board, hide_ships=True)

            print("\nYour turn to strike!")
            row, col = self.get_player_guess()
            self.player_guesses.add((row, col))

            hit = self.check_hit(self.computer_board, row, col)
            if hit:
                print("Hit!")
                if self.is_sunk(self.computer_board, self.computer_ships, row, col):
                    print("You sunk a ship!")
                if self.all_ships_sunk(self.computer_board):
                    print("\nCongratulations! You sunk all the computer's ships!")
                    break
            else:
                print("Miss!")

            # Computer's turn
            print("\nComputer's turn to strike...")
            row, col = self.computer_guess()
            self.computer_guesses.add((row, col))
            hit = self.check_hit(self.player_board, row, col)
            if hit:
                print("Computer hit your ship at {}, {}!".format(chr(col + 65), row + 1))
                if self.is_sunk(self.player_board, self.player_ships, row, col):
                    print("Computer sunk one of your ships!")
                if self.all_ships_sunk(self.player_board):
                    print("\nComputer sunk all your ships! You lose!")
                    break
            else:
                print("Computer missed at {}, {}!".format(chr(col + 65), row + 1))


if __name__ == "__main__":
    game = Battleship()
    game.play()