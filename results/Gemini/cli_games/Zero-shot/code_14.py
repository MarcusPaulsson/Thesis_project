import math
import random
import time

class Asteroid:
    def __init__(self, x, y, size, dx, dy):
        self.x = x
        self.y = y
        self.size = size
        self.dx = dx
        self.dy = dy

    def move(self, width, height):
        self.x += self.dx
        self.y += self.dy

        if self.x < 0:
            self.x = width
        elif self.x > width:
            self.x = 0
        if self.y < 0:
            self.y = height
        elif self.y > height:
            self.y = 0

    def __repr__(self):
        return f"Asteroid(x={self.x}, y={self.y}, size={self.size})"



class Ship:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.thrust = 0
        self.lives = 3
        self.invulnerable_timer = 0

    def move(self, width, height):
        self.x += self.thrust * math.cos(self.angle)
        self.y += self.thrust * math.sin(self.angle)

        if self.x < 0:
            self.x = width
        elif self.x > width:
            self.x = 0
        if self.y < 0:
            self.y = height
        elif self.y > height:
            self.y = 0

        self.thrust *= 0.95  # Gradual deceleration
        if self.invulnerable_timer > 0:
            self.invulnerable_timer -= 1


    def rotate_left(self):
        self.angle -= 0.1

    def rotate_right(self):
        self.angle += 0.1

    def accelerate(self):
        self.thrust += 0.2

    def is_colliding(self, asteroid):
        distance = math.sqrt((self.x - asteroid.x)**2 + (self.y - asteroid.y)**2)
        return distance < asteroid.size + 10  # Approximation for ship size

    def hit(self):
        if self.invulnerable_timer == 0:
            self.lives -= 1
            self.invulnerable_timer = 100 # Invulnerable for a short time
            return True
        return False
    
    def __repr__(self):
        return f"Ship(x={self.x}, y={self.y}, angle={self.angle}, lives={self.lives})"

class AsteroidsGame:
    def __init__(self, width=80, height=24, num_asteroids=5):
        self.width = width
        self.height = height
        self.ship = Ship(width // 2, height // 2, 0)
        self.asteroids = []
        self.num_asteroids = num_asteroids
        self.game_over = False
        self.score = 0
        self.create_asteroids()

    def create_asteroids(self):
        self.asteroids = []
        for _ in range(self.num_asteroids):
            size = random.randint(1, 3)
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            dx = random.uniform(-0.5, 0.5)
            dy = random.uniform(-0.5, 0.5)
            self.asteroids.append(Asteroid(x, y, size, dx, dy))

    def update(self, action=None):
        if self.game_over:
            return

        if action == "left":
            self.ship.rotate_left()
        elif action == "right":
            self.ship.rotate_right()
        elif action == "up":
            self.ship.accelerate()

        self.ship.move(self.width, self.height)

        for asteroid in self.asteroids:
            asteroid.move(self.width, self.height)

        self.check_collisions()

    def check_collisions(self):
        for i in range(len(self.asteroids)):
            if self.ship.is_colliding(self.asteroids[i]):
                if self.ship.hit():
                    print("Ship hit!")
                    if self.ship.lives <= 0:
                        self.game_over = True
                        print("Game Over!")
                del self.asteroids[i]
                self.score += 10
                return # Only one collision per frame
    def draw(self):
        screen = [[' ' for _ in range(self.width)] for _ in range(self.height)]

        # Draw asteroids
        for asteroid in self.asteroids:
            x = int(asteroid.x)
            y = int(asteroid.y)
            if 0 <= x < self.width and 0 <= y < self.height:
                screen[y][x] = '*'

        # Draw ship
        ship_x = int(self.ship.x)
        ship_y = int(self.ship.y)
        if 0 <= ship_x < self.width and 0 <= ship_y < self.height:
            screen[ship_y][ship_x] = 'A'

        # Draw lives and score
        lives_str = f"Lives: {self.ship.lives}"
        score_str = f"Score: {self.score}"

        for i, char in enumerate(lives_str):
            if i < self.width:
                screen[0][i] = char

        for i, char in enumerate(score_str):
            if i < self.width:
                screen[1][i] = char

        # Draw invulnerability indicator
        if self.ship.invulnerable_timer > 0:
            invulnerable_str = "Invulnerable!"
            invulnerable_start_x = self.width - len(invulnerable_str)
            for i, char in enumerate(invulnerable_str):
                if invulnerable_start_x + i < self.width:
                    screen[0][invulnerable_start_x + i] = char


        # Print screen
        for row in screen:
            print("".join(row))

    def play(self):
        while not self.game_over:
            self.draw()
            print("Controls: left (a), right (d), up (w), quit (q)")
            action = input("Enter action: ").lower()

            if action == "q":
                self.game_over = True
                break

            self.update(action)
            time.sleep(0.1)  # Control game speed

        print("Final Score:", self.score)

if __name__ == "__main__":
    game = AsteroidsGame()
    game.play()