import math
import random
import time
import sys

class GameObject:
    def __init__(self, x, y, velocity_x, velocity_y, size, symbol):
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.size = size
        self.symbol = symbol

    def move(self, width, height):
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Wrap around the screen
        if self.x < 0:
            self.x = width
        elif self.x > width:
            self.x = 0
        if self.y < 0:
            self.y = height
        elif self.y > height:
            self.y = 0

    def draw(self, screen):
        x = int(round(self.x))
        y = int(round(self.y))
        screen[y][x] = self.symbol

    def check_collision(self, other):
        distance = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        return distance < (self.size + other.size)

class Asteroid(GameObject):
    def __init__(self, x, y, velocity_x, velocity_y, size):
        super().__init__(x, y, velocity_x, velocity_y, size, '*')

class Ship(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 0, 0, 1, '^') # '^' for ship pointing upwards
        self.rotation = 0  # Angle in radians

    def rotate_left(self):
        self.rotation -= 0.1

    def rotate_right(self):
        self.rotation += 0.1

    def accelerate(self):
        self.velocity_x += 0.2 * math.sin(self.rotation)
        self.velocity_y -= 0.2 * math.cos(self.rotation)  # Y-axis is inverted

    def draw(self, screen):
        x = int(round(self.x))
        y = int(round(self.y))

        # Convert rotation to a "pointing" symbol
        if abs(self.rotation) < 0.2:
            symbol = '^'
        elif abs(self.rotation - math.pi/2) < 0.2:
            symbol = '>'
        elif abs(self.rotation - math.pi) < 0.2 or abs(self.rotation + math.pi) < 0.2:
            symbol = 'v'
        elif abs(self.rotation + math.pi/2) < 0.2:
            symbol = '<'
        else:
             symbol = 'X' #Generic symbol if the angle doesn't match known angles

        screen[y][x] = symbol


class Bullet(GameObject):
    def __init__(self, x, y, velocity_x, velocity_y):
        super().__init__(x, y, velocity_x, velocity_y, 0, '.')

class AsteroidsGame:
    def __init__(self, width=80, height=24):
        self.width = width
        self.height = height
        self.ship = Ship(width // 2, height // 2)
        self.asteroids = [Asteroid(random.randint(0, width), random.randint(0, height),
                                   random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5),
                                   random.randint(1, 3)) for _ in range(5)]
        self.bullets = []
        self.game_over = False
        self.score = 0

    def create_screen(self):
        return [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def draw_objects(self, screen):
        self.ship.draw(screen)
        for asteroid in self.asteroids:
            asteroid.draw(screen)
        for bullet in self.bullets:
            bullet.draw(screen)

    def move_objects(self):
        self.ship.move(self.width, self.height)
        for asteroid in self.asteroids:
            asteroid.move(self.width, self.height)
        for bullet in self.bullets:
            bullet.move(self.width, self.height)

        # Remove bullets that are out of bounds
        self.bullets = [bullet for bullet in self.bullets if 0 <= bullet.x < self.width and 0 <= bullet.y < self.height]

    def handle_collisions(self):
        # Ship - Asteroid collisions
        for asteroid in self.asteroids:
            if self.ship.check_collision(asteroid):
                self.game_over = True
                return

        # Bullet - Asteroid collisions
        for bullet in self.bullets[:]: #Iterate over a copy
            for asteroid in self.asteroids[:]: #Iterate over a copy
                if bullet.check_collision(asteroid):
                    self.bullets.remove(bullet)
                    self.asteroids.remove(asteroid)
                    self.score += 10
                    # Create new asteroids if the asteroid was large enough
                    if asteroid.size > 1:
                        new_asteroids = self.split_asteroid(asteroid)
                        self.asteroids.extend(new_asteroids)
                    break # Important: Break inner loop after removing asteroid


    def split_asteroid(self, asteroid):
        new_asteroids = []
        for _ in range(2): # Split into two smaller asteroids
            new_size = asteroid.size - 1
            if new_size > 0:
                new_asteroids.append(Asteroid(asteroid.x, asteroid.y,
                                              random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5),
                                              new_size))
        return new_asteroids


    def handle_input(self, key):
        if key == 'a':
            self.ship.rotate_left()
        elif key == 'd':
            self.ship.rotate_right()
        elif key == 'w':
            self.ship.accelerate()
        elif key == ' ':
            # Fire a bullet.  Velocity is based on ship's rotation.
            bullet_speed = 2
            bullet_velocity_x = bullet_speed * math.sin(self.ship.rotation)
            bullet_velocity_y = -bullet_speed * math.cos(self.ship.rotation)
            self.bullets.append(Bullet(self.ship.x, self.ship.y, bullet_velocity_x, bullet_velocity_y))


    def display_screen(self, screen):
        # Clear the screen (OS specific)
        if sys.platform in ['linux', 'darwin']:  # Linux or MacOS
            print("\033[2J\033[H", end="")
        elif sys.platform in ['win32', 'cygwin']:
            import os
            os.system('cls')
        else: # Fallback - just print newlines
            print('\n' * self.height)

        print("\n".join("".join(row) for row in screen))
        print(f"Score: {self.score}")
        print("Controls: W (Accelerate), A (Rotate Left), D (Rotate Right), Space (Fire)")

    def run(self):
        while not self.game_over:
            screen = self.create_screen()
            self.move_objects()
            self.handle_collisions()
            self.draw_objects(screen)
            self.display_screen(screen)

            # Get user input (non-blocking)
            key = get_input()  # Use the get_input function defined below
            if key:
                self.handle_input(key)

            time.sleep(0.05)
        print("Game Over! Final Score:", self.score)


# Non-blocking input (platform specific)
import select
import tty
import termios

def get_input():
    if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
        old_settings = termios.tcgetattr(sys.stdin)
        try:
            tty.setcbreak(sys.stdin.fileno())
            char = sys.stdin.read(1)
        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
        return char
    return None

if __name__ == "__main__":
    game = AsteroidsGame()
    game.run()