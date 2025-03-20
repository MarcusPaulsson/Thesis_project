import random

class Battleship:
    def __init__(self, board_size=10, num_ships=5):
        """
        Initializes the Battleship game.

        Args:
            board_size (int): The size of the game board (e.g., 10 for a 10x10 board).
            num_ships (int): The number of ships each player will have.
        """
        self.board_size = board_size
        self.num_ships = num_ships
        self.player_board = self.create_board()
        self.computer_board = self.create_board()
        self.player_ships = self.place_ships(self.player_board)
        self.computer_ships = self.place_ships(self.computer_board)
        self.computer_guesses = set()  # To avoid redundant guesses
        self.player_ships_sunk = 0
        self.computer_ships_sunk = 0

    def create_board(self):
        """
        Creates an empty game board represented as a 2D list.

        Returns:
            list: A 2D list representing the game board.
        """
        return [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]

    def place_ships(self, board):
        """
        Randomly places ships on the given board.

        Args:
            board (list): The game board to place ships on.

        Returns:
            list: A list of ship coordinates (tuples) representing the ships placed.
        """
        ships = []
        for _ in range(self.num_ships):
            while True:
                orientation = random.choice(['horizontal', 'vertical'])
                if orientation == 'horizontal':
                    row = random.randint(0, self.board_size - 1)
                    col = random.randint(0, self.board_size - 2) # At least 2 spaces for a ship of size 2
                    if all(board[row][col + i] == ' ' for i in range(2)):
                        for i in range(2):
                            board[row][col + i] = 'S'
                            ships.append((row, col + i))
                        break
                else:  # Vertical
                    row = random.randint(0, self.board_size - 2) # At least 2 spaces for a ship of size 2
                    col = random.randint(0, self.board_size - 1)
                    if all(board[row + i][col] == ' ' for i in range(2)):
                        for i in range(2):
                            board[row + i][col] = 'S'
                            ships.append((row + i, col))
                        break
        return ships

    def print_board(self, board, hide_ships=False):
        """
        Prints the game board to the console.

        Args:
            board (list): The game board to print.
            hide_ships (bool): Whether to hide the ships ('S') on the board.
                                 Defaults to False (ships are shown).
        """
        print("  " + " ".join([chr(65 + i) for i in range(self.board_size)])) # A, B, C...
        for i in range(self.board_size):
            row_str = str(i + 1).rjust(2) + " "  # Row numbers, right-aligned
            for j in range(self.board_size):
                if hide_ships and board[i][j] == 'S':
                    row_str += ' ' + " "
                else:
                    row_str += board[i][j] + " "
            print(row_str)

    def get_player_guess(self):
        """
        Gets the player's guess for a coordinate.

        Returns:
            tuple: The (row, col) coordinates of the player's guess, or None if invalid.
        """
        while True:
            try:
                guess = input("Enter your guess (e.g., A1): ").upper()
                if len(guess) < 2:
                    print("Invalid guess.  Try again (e.g., A1).")
                    continue
                col = ord(guess[0]) - 65  # Convert letter to column index (A=0, B=1, ...)
                row = int(guess[1:]) - 1    # Convert number to row index (1=0, 2=1, ...)

                if 0 <= row < self.board_size and 0 <= col < self.board_size:
                    return (row, col)
                else:
                    print("Invalid guess. Coordinates out of bounds.")
            except ValueError:
                print("Invalid guess.  Try again (e.g., A1).")
            except IndexError:
                print("Invalid guess.  Try again (e.g., A1).")

    def computer_make_guess(self):
        """
        Generates a random guess for the computer.

        Returns:
            tuple: The (row, col) coordinates of the computer's guess.
        """
        while True:
            row = random.randint(0, self.board_size - 1)
            col = random.randint(0, self.board_size - 1)
            if (row, col) not in self.computer_guesses:
                self.computer_guesses.add((row, col))
                return (row, col)

    def check_hit(self, board, row, col):
        """
        Checks if a guess hits a ship on the board.

        Args:
            board (list): The game board.
            row (int): The row coordinate of the guess.
            col (int): The column coordinate of the guess.

        Returns:
            bool: True if the guess hits a ship, False otherwise.
        """
        if board[row][col] == 'S':
            board[row][col] = 'X'  # Mark as hit
            return True
        elif board[row][col] == ' ':
            board[row][col] = 'O'  # Mark as miss
            return False
        else:  # Already hit or missed
            return False

    def play_round(self):
        """
        Plays a single round of the game.
        """
        # Player's turn
        print("\nYour board:")
        self.print_board(self.player_board)
        print("\nComputer's board:")
        self.print_board(self.computer_board, hide_ships=True)  # Hide computer's ships

        player_guess = self.get_player_guess()
        if player_guess:
            row, col = player_guess
            if self.check_hit(self.computer_board, row, col):
                print("Hit!")
                self.computer_ships = [(r, c) for r, c in self.computer_ships if (r, c) != (row, col)]
                if (row, col) in self.computer_ships:
                    self.computer_ships.remove((row, col))
                if self.computer_board[row][col] == 'X':
                    self.computer_ships_sunk += 1
                if self.computer_ships_sunk == self.num_ships * 2:
                    return "player_wins"
            else:
                print("Miss!")


        # Computer's turn
        print("\nComputer's turn...")
        computer_guess = self.computer_make_guess()
        row, col = computer_guess
        if self.check_hit(self.player_board, row, col):
            print("Computer hit your ship at", chr(col + 65), row + 1, "!")
            self.player_ships = [(r, c) for r, c in self.player_ships if (r, c) != (row, col)]
            if (row, col) in self.player_ships:
                self.player_ships.remove((row, col))

            if self.player_board[row][col] == 'X':
                self.player_ships_sunk += 1
            if self.player_ships_sunk == self.num_ships * 2:
                return "computer_wins"

        else:
            print("Computer missed at", chr(col + 65), row + 1, ".")

        return None  # No winner yet

    def play_game(self):
        """
        Starts and runs the main game loop.
        """
        print("Welcome to Battleship!")
        print(f"Board size: {self.board_size}x{self.board_size}, Number of ships: {self.num_ships}")

        while True:
            winner = self.play_round()
            if winner:
                if winner == "player_wins":
                    print("\nCongratulations! You sunk all the computer's ships!")
                elif winner == "computer_wins":
                    print("\nOh no! The computer sunk all your ships!")
                break


if __name__ == "__main__":
    game = Battleship()
    game.play_game()