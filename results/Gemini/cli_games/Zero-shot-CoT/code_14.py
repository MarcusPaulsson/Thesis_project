import math
import random
import sys
import time


class AsteroidGame:
    """
    A command-line Asteroids game.
    """

    def __init__(self, width=80, height=20, asteroid_count=5, max_speed=1.0, turn_speed=0.1):
        """
        Initializes the game.

        Args:
            width (int): The width of the game board.
            height (int): The height of the game board.
            asteroid_count (int): The initial number of asteroids.
            max_speed (float): The maximum speed of the spaceship and asteroids.
        """
        self.width = width
        self.height = height
        self.asteroid_count = asteroid_count
        self.max_speed = max_speed
        self.turn_speed = turn_speed
        self.spaceship = Spaceship(self.width // 2, self.height // 2, 0.0, max_speed=self.max_speed)
        self.asteroids = []
        self.bullets = []
        self.score = 0
        self.game_over = False

        for _ in range(self.asteroid_count):
            self.asteroids.append(self._create_asteroid())

    def _create_asteroid(self):
        """
        Creates a new asteroid at a random location, avoiding the spaceship's initial position.

        Returns:
            Asteroid: The newly created asteroid.
        """
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if abs(x - self.spaceship.x) > self.width // 4 or abs(y - self.spaceship.y) > self.height // 4:
                break
        angle = random.uniform(0, 2 * math.pi)
        return Asteroid(x, y, angle, size=3, max_speed=self.max_speed)

    def run(self):
        """
        Runs the main game loop.
        """
        while not self.game_over:
            self.print_board()
            self.process_input()
            self.update_game_state()
            time.sleep(0.1)  # Adjust for game speed
        self.print_game_over()

    def print_board(self):
        """
        Prints the game board to the console.
        """
        board = [[' ' for _ in range(self.width)] for _ in range(self.height)]

        # Draw spaceship
        spaceship_x = int(round(self.spaceship.x)) % self.width
        spaceship_y = int(round(self.spaceship.y)) % self.height

        if 0 <= spaceship_x < self.width and 0 <= spaceship_y < self.height:
            board[spaceship_y][spaceship_x] = '^'

        # Draw asteroids
        for asteroid in self.asteroids:
            asteroid_x = int(round(asteroid.x)) % self.width
            asteroid_y = int(round(asteroid.y)) % self.height
            if 0 <= asteroid_x < self.width and 0 <= asteroid_y < self.height:
                board[asteroid_y][asteroid_x] = 'O'

        # Draw bullets
        for bullet in self.bullets:
            bullet_x = int(round(bullet.x)) % self.width
            bullet_y = int(round(bullet.y)) % self.height
            if 0 <= bullet_x < self.width and 0 <= bullet_y < self.height:
                board[bullet_y][bullet_x] = '.'

        # Print the board
        print("\033c", end="")  # Clear the screen (works in most terminals)
        for row in board:
            print("".join(row))
        print(f"Score: {self.score}")

    def process_input(self):
        """
        Processes user input to control the spaceship.
        """
        action = input("Action (a=left, d=right, w=forward, s=shoot, q=quit): ").lower()
        if action == 'a':
            self.spaceship.turn_left(self.turn_speed)
        elif action == 'd':
            self.spaceship.turn_right(self.turn_speed)
        elif action == 'w':
            self.spaceship.accelerate()
        elif action == 's':
            self.bullets.append(self.spaceship.shoot())
        elif action == 'q':
            self.game_over = True

    def update_game_state(self):
        """
        Updates the positions of all game objects, checks for collisions, and removes destroyed objects.
        """
        # Update spaceship position
        self.spaceship.update(self.width, self.height)

        # Update asteroid positions
        for asteroid in self.asteroids:
            asteroid.update(self.width, self.height)

        # Update bullet positions
        for bullet in self.bullets:
            bullet.update(self.width, self.height)

        # Check for collisions between bullets and asteroids
        bullets_to_remove = []
        asteroids_to_remove = []
        for bullet in self.bullets:
            for asteroid in self.asteroids:
                if self._check_collision(bullet, asteroid):
                    bullets_to_remove.append(bullet)
                    asteroids_to_remove.append(asteroid)
                    self.score += 10
                    break  # Only one asteroid can be hit per bullet
        for bullet in bullets_to_remove:
            if bullet in self.bullets:
                self.bullets.remove(bullet)
        for asteroid in asteroids_to_remove:
            if asteroid in self.asteroids:
                self.asteroids.remove(asteroid)

        # Check for collisions between spaceship and asteroids
        for asteroid in self.asteroids:
            if self._check_collision(self.spaceship, asteroid):
                self.game_over = True
                break

        # Remove bullets that are out of bounds
        self.bullets = [
            bullet for bullet in self.bullets if 0 <= bullet.x < self.width and 0 <= bullet.y < self.height
        ]

        # Spawn new asteroids if necessary
        while len(self.asteroids) < self.asteroid_count:
            self.asteroids.append(self._create_asteroid())

    def _check_collision(self, obj1, obj2):
        """
        Checks for collision between two game objects.  Simple distance check.

        Args:
            obj1: The first game object (must have x and y attributes).
            obj2: The second game object (must have x and y attributes).

        Returns:
            bool: True if the objects are colliding, False otherwise.
        """
        distance = math.sqrt((obj1.x - obj2.x) ** 2 + (obj1.y - obj2.y) ** 2)
        return distance < 2  # Simple collision detection radius

    def print_game_over(self):
        """
        Prints the game over message and final score.
        """
        print("Game Over!")
        print(f"Final Score: {self.score}")


class GameObject:
    """
    Base class for game objects (spaceship, asteroids, bullets).
    """

    def __init__(self, x, y, angle, speed=0.0, max_speed=1.0):
        """
        Initializes a game object.

        Args:
            x (float): The x-coordinate of the object.
            y (float): The y-coordinate of the object.
            angle (float): The angle of the object in radians.
            speed (float): The speed of the object.
            max_speed (float): The maximum speed of the object.
        """
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.max_speed = max_speed

    def update(self, width, height):
        """
        Updates the position of the object.

        Args:
            width (int): The width of the game board.
            height (int): The height of the game board.
        """
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

        # Wrap around the edges of the screen
        self.x %= width
        self.y %= height


class Spaceship(GameObject):
    """
    Represents the player's spaceship.
    """

    def __init__(self, x, y, angle, max_speed=1.0):
        """
        Initializes the spaceship.

        Args:
            x (float): The x-coordinate of the spaceship.
            y (float): The y-coordinate of the spaceship.
            angle (float): The angle of the spaceship in radians.
            max_speed (float): The maximum speed of the spaceship.
        """
        super().__init__(x, y, angle, max_speed=max_speed)
        self.acceleration = 0.05
        self.bullet_speed = self.max_speed * 2

    def accelerate(self):
        """
        Increases the spaceship's speed.
        """
        self.speed = min(self.speed + self.acceleration, self.max_speed)

    def turn_left(self, turn_speed):
        """
        Turns the spaceship left.

        Args:
            turn_speed (float): The amount to turn the spaceship in radians.
        """
        self.angle -= turn_speed

    def turn_right(self, turn_speed):
        """
        Turns the spaceship right.

        Args:
            turn_speed (float): The amount to turn the spaceship in radians.
        """
        self.angle += turn_speed

    def shoot(self):
        """
        Fires a bullet from the spaceship.

        Returns:
            Bullet: The newly created bullet.
        """
        return Bullet(self.x, self.y, self.angle, speed=self.bullet_speed)


class Asteroid(GameObject):
    """
    Represents an asteroid.
    """

    def __init__(self, x, y, angle, size=3, max_speed=1.0):
        """
        Initializes an asteroid.

        Args:
            x (float): The x-coordinate of the asteroid.
            y (float): The y-coordinate of the asteroid.
            angle (float): The angle of the asteroid in radians.
            size (int): The size of the asteroid (not currently used, but could be used for splitting).
            max_speed (float): The maximum speed of the asteroid.
        """
        super().__init__(x, y, angle, speed=random.uniform(0.1, max_speed), max_speed=max_speed)
        self.size = size


class Bullet(GameObject):
    """
    Represents a bullet fired by the spaceship.
    """

    def __init__(self, x, y, angle, speed):
        """
        Initializes a bullet.

        Args:
            x (float): The x-coordinate of the bullet.
            y (float): The y-coordinate of the bullet.
            angle (float): The angle of the bullet in radians.
            speed (float): The speed of the bullet.
        """
        super().__init__(x, y, angle, speed=speed)


if __name__ == "__main__":
    game = AsteroidGame()
    game.run()