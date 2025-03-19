import random
import time
import os

class PacmanGame:
    """
    A command-line Pac-Man game implementation.
    """

    def __init__(self, width=15, height=10, num_ghosts=2):
        """
        Initializes the game board, Pac-Man, ghosts, and food.

        Args:
            width (int): The width of the game board.
            height (int): The height of the game board.
            num_ghosts (int): The number of ghosts in the game.
        """
        self.width = width
        self.height = height
        self.num_ghosts = num_ghosts
        self.board = [[' ' for _ in range(width)] for _ in range(height)]
        self.pacman_x = width // 2
        self.pacman_y = height // 2
        self.board[self.pacman_y][self.pacman_x] = 'P'
        self.ghosts = []
        for _ in range(num_ghosts):
            self.ghosts.append(self.create_ghost())
        self.food_count = 0
        self.place_food()
        self.score = 0
        self.game_over = False
        self.won = False

    def create_ghost(self):
        """
        Creates a ghost at a random location on the board, avoiding Pac-Man's starting position.

        Returns:
            tuple: The (x, y) coordinates of the new ghost.
        """
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if (x, y) != (self.pacman_x, self.pacman_y) and self.board[y][x] != 'G':
                return (x, y)

    def place_food(self):
        """
        Places food ('o') on the board at empty locations.
        """
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == ' ':
                    self.board[y][x] = 'o'
                    self.food_count += 1

    def print_board(self):
        """
        Prints the current state of the game board to the console.
        """
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        print("-" * (self.width + 2))
        for row in self.board:
            print("|" + "".join(row) + "|")
        print("-" * (self.width + 2))
        print(f"Score: {self.score}")
        print("Use WASD to move. Press Q to quit.")

    def move_pacman(self, direction):
        """
        Moves Pac-Man based on the given direction (W, A, S, D).

        Args:
            direction (str): The direction to move Pac-Man ('W', 'A', 'S', 'D').
        """
        new_x = self.pacman_x
        new_y = self.pacman_y

        if direction == 'W':
            new_y -= 1
        elif direction == 'S':
            new_y += 1
        elif direction == 'A':
            new_x -= 1
        elif direction == 'D':
            new_x += 1

        if 0 <= new_x < self.width and 0 <= new_y < self.height:
            if self.board[new_y][new_x] == 'o':
                self.score += 10
                self.food_count -= 1
            elif self.board[new_y][new_x] == 'G':
                self.game_over = True
                return

            self.board[self.pacman_y][self.pacman_x] = ' '
            self.pacman_x = new_x
            self.pacman_y = new_y
            self.board[self.pacman_y][self.pacman_x] = 'P'

            if self.food_count == 0:
                self.won = True
                self.game_over = True

    def move_ghosts(self):
        """
        Moves each ghost randomly to an adjacent empty location.
        """
        for i in range(len(self.ghosts)):
            x, y = self.ghosts[i]
            possible_moves = []
            if x > 0 and self.board[y][x - 1] != 'G' and self.board[y][x - 1] != 'P':
                possible_moves.append((x - 1, y))
            if x < self.width - 1 and self.board[y][x + 1] != 'G' and self.board[y][x + 1] != 'P':
                possible_moves.append((x + 1, y))
            if y > 0 and self.board[y - 1][x] != 'G' and self.board[y - 1][x] != 'P':
                possible_moves.append((x, y - 1))
            if y < self.height - 1 and self.board[y + 1][x] != 'G' and self.board[y + 1][x] != 'P':
                possible_moves.append((x, y + 1))

            if possible_moves:
                new_x, new_y = random.choice(possible_moves)
                self.board[y][x] = ' '  # Clear the ghost's previous position

                if (new_x, new_y) == (self.pacman_x, self.pacman_y):
                    self.game_over = True
                    return

                self.ghosts[i] = (new_x, new_y)
                self.board[new_y][new_x] = 'G'

    def run(self):
        """
        Runs the main game loop.
        """
        while not self.game_over:
            self.print_board()
            move = input("Enter move (W/A/S/D) or Q to quit: ").upper()

            if move == 'Q':
                self.game_over = True
                break

            self.move_pacman(move)
            if self.game_over:
                break
            self.move_ghosts()
            if self.game_over:
                break
            time.sleep(0.2)

        self.print_board()
        if self.won:
            print("Congratulations! You won!")
        elif self.game_over:
            print("Game Over! You were caught by a ghost.")
        print(f"Final Score: {self.score}")


if __name__ == "__main__":
    game = PacmanGame()
    game.run()