import random
import time
import os

class PacManGame:
    """
    A command-line Pac-Man game implementation.
    """

    def __init__(self, width=15, height=10, num_ghosts=2, initial_food_percentage=0.2):
        """
        Initializes the Pac-Man game.

        Args:
            width (int): The width of the game board.
            height (int): The height of the game board.
            num_ghosts (int): The number of ghosts in the game.
            initial_food_percentage (float): The initial percentage of the board filled with food.
        """

        self.width = width
        self.height = height
        self.num_ghosts = num_ghosts
        self.initial_food_percentage = initial_food_percentage
        self.board = [[' ' for _ in range(width)] for _ in range(height)]
        self.pacman_x = width // 2
        self.pacman_y = height // 2
        self.ghosts = []
        self.food_count = 0
        self.score = 0
        self.game_over = False
        self.won = False

        self.directions = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}  # row, col
        self.ghost_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # row, col

        self.initialize_board()

    def initialize_board(self):
        """
        Initializes the game board with walls, food, Pac-Man, and ghosts.
        """

        # Create walls around the board
        for i in range(self.width):
            self.board[0][i] = '#'
            self.board[self.height - 1][i] = '#'
        for i in range(self.height):
            self.board[i][0] = '#'
            self.board[i][self.width - 1] = '#'

        # Place food randomly
        for i in range(1, self.height - 1):
            for j in range(1, self.width - 1):
                if random.random() < self.initial_food_percentage:
                    self.board[i][j] = '.'
                    self.food_count += 1

        # Place Pac-Man in the center
        self.board[self.pacman_y][self.pacman_x] = 'P'

        # Place ghosts randomly
        for _ in range(self.num_ghosts):
            while True:
                x = random.randint(1, self.width - 2)
                y = random.randint(1, self.height - 2)
                if self.board[y][x] == ' ':  # Or '.' if you want ghosts on food
                    self.ghosts.append((y, x))
                    self.board[y][x] = 'G'
                    break

    def print_board(self):
        """
        Prints the current state of the game board to the console.
        """
        os.system('cls' if os.name == 'nt' else 'clear') # Clear the console
        print("-" * (self.width + 2))
        for row in self.board:
            print("|" + "".join(row) + "|")
        print("-" * (self.width + 2))
        print(f"Score: {self.score}  Food Remaining: {self.food_count}")
        print("Use 'w' (up), 's' (down), 'a' (left), 'd' (right) to move.  'q' to quit.")


    def move_pacman(self, direction):
        """
        Moves Pac-Man in the specified direction.

        Args:
            direction (str): The direction to move ('w', 'a', 's', 'd').
        """

        dy, dx = self.directions.get(direction, (0, 0))  # Default to no movement
        new_x = self.pacman_x + dx
        new_y = self.pacman_y + dy

        if 0 < new_x < self.width - 1 and 0 < new_y < self.height - 1 and self.board[new_y][new_x] != '#':
            # Clear Pac-Man's previous position
            self.board[self.pacman_y][self.pacman_x] = ' '

            # Update Pac-Man's position
            self.pacman_x = new_x
            self.pacman_y = new_y

            # Check for food
            if self.board[self.pacman_y][self.pacman_x] == '.':
                self.score += 10
                self.food_count -= 1

            # Check for ghosts (game over)
            if self.board[self.pacman_y][self.pacman_x] == 'G':
                self.game_over = True
                return

            # Place Pac-Man on the board
            self.board[self.pacman_y][self.pacman_x] = 'P'


    def move_ghosts(self):
        """
        Moves the ghosts randomly.
        """

        for i in range(len(self.ghosts)):
            y, x = self.ghosts[i]
            self.board[y][x] = ' '  # Clear the ghost's previous position

            while True:
                dy, dx = random.choice(self.ghost_directions)
                new_x = x + dx
                new_y = y + dy

                if 0 < new_x < self.width - 1 and 0 < new_y < self.height - 1 and self.board[new_y][new_x] != '#':
                    # Update ghost's position
                    self.ghosts[i] = (new_y, new_x)

                    # Check for collision with Pac-Man
                    if new_x == self.pacman_x and new_y == self.pacman_y:
                        self.game_over = True
                        return

                    self.board[new_y][new_x] = 'G'
                    break

    def check_win(self):
        """
        Checks if the player has won the game.
        """
        if self.food_count == 0:
            self.won = True
            self.game_over = True


    def play(self):
        """
        Starts and runs the Pac-Man game loop.
        """
        while not self.game_over:
            self.print_board()
            direction = input("Enter direction (w/a/s/d) or q to quit: ").lower()

            if direction == 'q':
                print("Quitting the game.")
                self.game_over = True
                break

            self.move_pacman(direction)
            if self.game_over:
                break  # Game over because Pac-Man hit a ghost

            self.move_ghosts()
            if self.game_over:
                break  # Game over because a ghost hit Pac-Man


            self.check_win()
            time.sleep(0.2)  # Add a short delay to control game speed

        self.print_board() # Print the final board state

        if self.won:
            print("Congratulations! You won!")
        elif self.game_over:
            print("Game Over! You were caught by a ghost.")
        else:
            print("Game ended.")
        print(f"Final Score: {self.score}")


if __name__ == "__main__":
    game = PacManGame(width=20, height=12, num_ghosts=3, initial_food_percentage=0.15)
    game.play()