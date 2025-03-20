import random
import time
import os


class PacmanGame:
    """
    A simple command-line Pac-Man game.
    """

    def __init__(self, width=15, height=10):
        """
        Initializes the Pac-Man game.

        Args:
            width (int): The width of the game grid.
            height (int): The height of the game grid.
        """
        self.width = width
        self.height = height
        self.pacman_x = width // 2
        self.pacman_y = height // 2
        self.ghost_x = 1
        self.ghost_y = 1
        self.food = set()
        self.score = 0
        self.game_over = False
        self.level = 1
        self.ghost_speed = 0.5  # Ghost movement frequency (lower = faster)

        # Initialize food pellets
        for x in range(width):
            for y in range(height):
                if (x, y) != (self.pacman_x, self.pacman_y) and (x, y) != (self.ghost_x, self.ghost_y):
                    self.food.add((x, y))

    def display(self):
        """
        Displays the game grid in the console.
        """

        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen

        # Display game information
        print(f"Level: {self.level}  Score: {self.score}")

        # Create the grid
        grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]

        # Place food pellets
        for x, y in self.food:
            grid[y][x] = '.'

        # Place Pac-Man
        grid[self.pacman_y][self.pacman_x] = 'P'

        # Place the ghost
        grid[self.ghost_y][self.ghost_x] = 'G'

        # Draw the grid
        for row in grid:
            print(''.join(row))

    def move_pacman(self, direction):
        """
        Moves Pac-Man based on the given direction.

        Args:
            direction (str): The direction to move (up, down, left, right).
        """
        new_x, new_y = self.pacman_x, self.pacman_y

        if direction == 'up':
            new_y -= 1
        elif direction == 'down':
            new_y += 1
        elif direction == 'left':
            new_x -= 1
        elif direction == 'right':
            new_x += 1

        # Check for boundaries
        if 0 <= new_x < self.width and 0 <= new_y < self.height:
            self.pacman_x = new_x
            self.pacman_y = new_y

            # Check if Pac-Man eats food
            if (self.pacman_x, self.pacman_y) in self.food:
                self.food.remove((self.pacman_x, self.pacman_y))
                self.score += 10

            # Check if Pac-Man collides with the ghost
            if self.pacman_x == self.ghost_x and self.pacman_y == self.ghost_y:
                self.game_over = True

            # Check if the level is complete
            if not self.food:
                self.level_complete()

    def move_ghost(self):
        """
        Moves the ghost randomly.
        """
        possible_moves = []
        if self.ghost_x > 0:
            possible_moves.append('left')
        if self.ghost_x < self.width - 1:
            possible_moves.append('right')
        if self.ghost_y > 0:
            possible_moves.append('up')
        if self.ghost_y < self.height - 1:
            possible_moves.append('down')

        direction = random.choice(possible_moves)
        new_x, new_y = self.ghost_x, self.ghost_y

        if direction == 'up':
            new_y -= 1
        elif direction == 'down':
            new_y += 1
        elif direction == 'left':
            new_x -= 1
        elif direction == 'right':
            new_x += 1

        self.ghost_x = new_x
        self.ghost_y = new_y

        # Check for collision with pacman
        if self.pacman_x == self.ghost_x and self.pacman_y == self.ghost_y:
            self.game_over = True

    def level_complete(self):
        """
        Advances the game to the next level.
        """
        self.level += 1
        print("Level Complete!")
        time.sleep(1)  # Pause briefly

        # Reset Pac-Man and Ghost positions
        self.pacman_x = self.width // 2
        self.pacman_y = self.height // 2
        self.ghost_x = 1
        self.ghost_y = 1

        # Refill the food
        self.food = set()
        for x in range(self.width):
            for y in range(self.height):
                if (x, y) != (self.pacman_x, self.pacman_y) and (x, y) != (self.ghost_x, self.ghost_y):
                    self.food.add((x, y))

        # Optionally increase ghost speed each level
        self.ghost_speed = max(0.1, self.ghost_speed - 0.05)

    def play(self):
        """
        Starts the main game loop.
        """
        last_ghost_move = time.time()

        while not self.game_over:
            self.display()

            # Get player input
            direction = input("Enter move (up, down, left, right, quit): ").lower()

            if direction == 'quit':
                break

            # Move Pac-Man
            self.move_pacman(direction)

            # Move ghost based on the timer
            current_time = time.time()
            if current_time - last_ghost_move > self.ghost_speed:
                self.move_ghost()
                last_ghost_move = current_time

            time.sleep(0.1)  # Control game speed

        if self.game_over:
            self.display()
            print("Game Over! Final Score:", self.score)
        else:
            print("Game quit. Final Score:", self.score)


if __name__ == "__main__":
    game = PacmanGame()
    game.play()