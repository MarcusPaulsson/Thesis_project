import random
import time
import math
import sys

class AsteroidGame:
    """
    A simple Asteroid game implemented in the command line.
    """

    def __init__(self, width=80, height=20, asteroid_count=5, max_shots=3):
        """
        Initializes the game.

        Args:
            width (int): The width of the game board.
            height (int): The height of the game board.
            asteroid_count (int): The number of asteroids in the game.
            max_shots (int): The maximum number of simultaneous shots allowed.
        """

        self.width = width
        self.height = height
        self.asteroid_count = asteroid_count
        self.max_shots = max_shots

        self.ship_x = width // 2
        self.ship_y = height // 2
        self.ship_char = "^"  # Ship represented by a caret

        self.asteroids = []
        self.shots = []

        self.game_over = False
        self.score = 0

        self._initialize_asteroids()

    def _initialize_asteroids(self):
        """
        Creates the initial set of asteroids at random positions.
        """
        for _ in range(self.asteroid_count):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            # Ensure asteroids aren't too close to the ship initially
            while abs(x - self.ship_x) < self.width // 4 and abs(y - self.ship_y) < self.height // 4:
                 x = random.randint(0, self.width - 1)
                 y = random.randint(0, self.height - 1)

            self.asteroids.append({
                'x': x,
                'y': y,
                'char': 'O',  # Asteroids represented by 'O'
                'x_velocity': random.choice([-1, 1]),
                'y_velocity': random.choice([-1, 1])
            })

    def _draw_board(self):
        """
        Draws the game board in the console.
        """
        board = [[' ' for _ in range(self.width)] for _ in range(self.height)]

        # Draw asteroids
        for asteroid in self.asteroids:
            board[asteroid['y']][asteroid['x']] = asteroid['char']

        # Draw shots
        for shot in self.shots:
            board[shot['y']][shot['x']] = '*'  # Shots represented by '*'

        # Draw ship
        board[self.ship_y][self.ship_x] = self.ship_char

        # Print the board
        for row in board:
            print("".join(row))

        # Print score and instructions
        print(f"Score: {self.score}")
        print("Controls: A (Left), D (Right), W (Shoot), Q (Quit)")

    def _move_ship(self, direction):
        """
        Moves the ship left or right.

        Args:
            direction (str): 'left' or 'right'.
        """
        if direction == 'left':
            self.ship_x = max(0, self.ship_x - 1)
        elif direction == 'right':
            self.ship_x = min(self.width - 1, self.ship_x + 1)

    def _move_asteroids(self):
        """
        Moves the asteroids based on their velocity.
        Wraps around the edges of the screen.
        """
        for asteroid in self.asteroids:
            asteroid['x'] += asteroid['x_velocity']
            asteroid['y'] += asteroid['y_velocity']

            # Wrap around the edges
            if asteroid['x'] < 0:
                asteroid['x'] = self.width - 1
            elif asteroid['x'] >= self.width:
                asteroid['x'] = 0
            if asteroid['y'] < 0:
                asteroid['y'] = self.height - 1
            elif asteroid['y'] >= self.height:
                asteroid['y'] = 0

    def _move_shots(self):
        """
        Moves the shots upwards. Removes shots that go off-screen.
        """
        for shot in self.shots:
            shot['y'] -= 1  # Move upwards
        self.shots = [shot for shot in self.shots if shot['y'] >= 0] # Remove off-screen shots

    def _shoot(self):
        """
        Fires a shot from the ship's position.
        """
        if len(self.shots) < self.max_shots:
            self.shots.append({'x': self.ship_x, 'y': self.ship_y - 1})

    def _check_collisions(self):
        """
        Checks for collisions between shots and asteroids, and between the ship and asteroids.
        """
        # Shot-Asteroid collisions
        for shot in list(self.shots): # Iterate over a *copy* of the list
            for asteroid in list(self.asteroids): #Iterate over a *copy* of the list
                if abs(shot['x'] - asteroid['x']) <= 0 and abs(shot['y'] - asteroid['y']) <= 0:
                    self.asteroids.remove(asteroid)
                    self.shots.remove(shot)
                    self.score += 10
                    break # Avoid double-counting collisions

        # Ship-Asteroid collisions
        for asteroid in self.asteroids:
            if abs(self.ship_x - asteroid['x']) <= 0 and abs(self.ship_y - asteroid['y']) <= 0:
                self.game_over = True
                break

        #Handle game winning condition
        if not self.asteroids:
            print("You Win!")
            self.game_over = True

    def play(self):
        """
        The main game loop.
        """
        while not self.game_over:
            self._draw_board()

            # Get player input
            action = input("Enter action (A=Left, D=Right, W=Shoot, Q=Quit): ").upper()

            # Process input
            if action == 'A':
                self._move_ship('left')
            elif action == 'D':
                self._move_ship('right')
            elif action == 'W':
                self._shoot()
            elif action == 'Q':
                self.game_over = True
            else:
                print("Invalid input.")

            # Update game state
            self._move_asteroids()
            self._move_shots()
            self._check_collisions()

            # Add a small delay for better visibility
            time.sleep(0.1)

        print("Game Over! Final Score:", self.score)


if __name__ == '__main__':
    game = AsteroidGame()
    game.play()