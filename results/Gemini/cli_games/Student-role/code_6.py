import random

class Battleship:
    def __init__(self, board_size=10):
        self.board_size = board_size
        self.player_board = [['.' for _ in range(board_size)] for _ in range(board_size)]
        self.computer_board = [['.' for _ in range(board_size)] for _ in range(board_size)]
        self.player_ships = []
        self.computer_ships = []
        self.ship_lengths = [5, 4, 3, 3, 2]  #lengths of ships: Aircraft Carrier, Battleship, Cruiser, Submarine, Destroyer

    def print_board(self, board, hidden=True):
        """Prints the board with row and column labels."""
        print("  " + " ".join([chr(65 + i) for i in range(self.board_size)])) #A,B,C..
        for i in range(self.board_size):
            row_str = str(i + 1).rjust(2) + " "  # Number rows starting from 1
            for j in range(self.board_size):
                if hidden and board[i][j] == 'S':
                    row_str += '. '
                else:
                    row_str += board[i][j] + " "
            print(row_str)

    def place_ship(self, board, ship_length, player):
        """Places a ship on the board."""
        while True:
            if player == "player":
                orientation = input(f"Enter orientation for ship of length {ship_length} (H/V): ").upper()
                start_row = input(f"Enter starting row (1-{self.board_size}): ")
                start_col = input(f"Enter starting column (A-{chr(64+self.board_size)}): ").upper()
                try:
                    start_row = int(start_row) - 1  # Adjust to 0-based index
                    start_col = ord(start_col) - ord('A')
                    if not (0 <= start_row < self.board_size and 0 <= start_col < self.board_size):
                        print("Invalid coordinates. Try again.")
                        continue
                except (ValueError, TypeError):
                    print("Invalid input. Try again.")
                    continue
            else:  # Computer placement
                orientation = random.choice(['H', 'V'])
                start_row = random.randint(0, self.board_size - 1)
                start_col = random.randint(0, self.board_size - 1)

            if orientation not in ['H', 'V']:
                if player == "player":
                    print("Invalid orientation. Use 'H' or 'V'.")
                continue

            if orientation == 'H':
                if start_col + ship_length > self.board_size:
                    if player == "player":
                        print("Ship goes off the board. Try again.")
                    continue
                valid = True
                for i in range(ship_length):
                    if board[start_row][start_col + i] == 'S':
                        valid = False
                        break
                if not valid:
                    if player == "player":
                        print("Ships are overlapping. Try again.")
                    continue

                for i in range(ship_length):
                    board[start_row][start_col + i] = 'S'
                return True  # Ship placed successfully

            else:  # orientation == 'V'
                if start_row + ship_length > self.board_size:
                    if player == "player":
                        print("Ship goes off the board. Try again.")
                    continue
                valid = True
                for i in range(ship_length):
                    if board[start_row + i][start_col] == 'S':
                        valid = False
                        break
                if not valid:
                    if player == "player":
                        print("Ships are overlapping. Try again.")
                    continue
                for i in range(ship_length):
                    board[start_row + i][start_col] = 'S'
                return True  # Ship placed successfully

    def setup_boards(self):
        """Sets up the player and computer boards with ships."""
        print("Player, place your ships:")
        for length in self.ship_lengths:
            while not self.place_ship(self.player_board, length, "player"):
                pass
            self.print_board(self.player_board)

        print("\nComputer is placing ships...")
        for length in self.ship_lengths:
            while not self.place_ship(self.computer_board, length, "computer"):
                pass
        print("Computer's ships placed.")

    def take_turn(self, board, player):
        """Takes a turn for the given player."""
        while True:
            if player == "player":
                target_row = input(f"Player, enter row to strike (1-{self.board_size}): ")
                target_col = input(f"Player, enter column to strike (A-{chr(64+self.board_size)}): ").upper()
                try:
                    target_row = int(target_row) - 1
                    target_col = ord(target_col) - ord('A')
                    if not (0 <= target_row < self.board_size and 0 <= target_col < self.board_size):
                        print("Invalid coordinates. Try again.")
                        continue
                except (ValueError, TypeError):
                    print("Invalid input. Try again.")
                    continue
            else:
                target_row = random.randint(0, self.board_size - 1)
                target_col = random.randint(0, self.board_size - 1)
                print(f"Computer attacks {chr(target_col + ord('A'))}{target_row+1}")

            if board[target_row][target_col] == 'X' or board[target_row][target_col] == 'O':
                if player == "player":
                    print("You already attacked that location. Try again.")
                else:
                    print("Computer already attacked that location.")
                continue

            if board[target_row][target_col] == 'S':
                print("Hit!")
                board[target_row][target_col] = 'X'  # Mark as hit
                return True  # Hit
            else:
                print("Miss!")
                board[target_row][target_col] = 'O'  # Mark as miss
                return False  # Miss

    def check_win(self, board):
        """Checks if all ships have been sunk on the given board."""
        for row in board:
            if 'S' in row:
                return False  # Ships still present
        return True  # All ships sunk

    def play_game(self):
        """Main game loop."""
        self.setup_boards()

        while True:
            print("\nPlayer's Board:")
            self.print_board(self.player_board)
            print("\nComputer's Board:")
            self.print_board(self.computer_board, hidden=True)

            print("\nPlayer's Turn:")
            self.take_turn(self.computer_board, "player")
            if self.check_win(self.computer_board):
                print("\nPlayer wins!")
                print("Final Computer's Board:")
                self.print_board(self.computer_board, hidden=False)
                break

            print("\nComputer's Turn:")
            self.take_turn(self.player_board, "computer")
            if self.check_win(self.player_board):
                print("\nComputer wins!")
                print("Final Player's Board:")
                self.print_board(self.player_board)
                break

if __name__ == "__main__":
    game = Battleship()
    game.play_game()