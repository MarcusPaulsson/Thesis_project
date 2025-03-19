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

    def draw(self):
        print(f"Asteroid at ({self.x:.1f}, {self.y:.1f}), size: {self.size:.1f}")


class Bullet:
    def __init__(self, x, y, angle, speed):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.dx = math.cos(self.angle) * self.speed
        self.dy = math.sin(self.angle) * self.speed

    def move(self, width, height):
        self.x += self.dx
        self.y += self.dy

        if self.x < 0 or self.x > width or self.y < 0 or self.y > height:
            return True  # Indicate out of bounds

        return False

    def draw(self):
        print(f"Bullet at ({self.x:.1f}, {self.y:.1f})")


class Spaceship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0  # Radians
        self.thrust = 0
        self.dx = 0
        self.dy = 0

    def rotate_left(self, amount):
        self.angle -= amount

    def rotate_right(self, amount):
        self.angle += amount

    def apply_thrust(self, amount):
        self.thrust = amount

    def move(self, width, height):
        # Update velocity based on thrust
        self.dx += math.cos(self.angle) * self.thrust
        self.dy += math.sin(self.angle) * self.thrust

        # Apply friction (damping)
        self.dx *= 0.98
        self.dy *= 0.98

        self.x += self.dx
        self.y += self.dy

        # Keep within bounds (wrap around)
        if self.x < 0:
            self.x = width
        elif self.x > width:
            self.x = 0
        if self.y < 0:
            self.y = height
        elif self.y > height:
            self.y = 0

    def draw(self):
        print(f"Spaceship at ({self.x:.1f}, {self.y:.1f}), angle: {math.degrees(self.angle):.1f}")

    def shoot(self, bullet_speed):
        return Bullet(self.x, self.y, self.angle, bullet_speed)


class AsteroidsGame:
    def __init__(self, width=80, height=24, num_asteroids=5, bullet_speed=5):
        self.width = width
        self.height = height
        self.spaceship = Spaceship(width // 2, height // 2)
        self.asteroids = []
        self.bullets = []
        self.score = 0
        self.game_over = False
        self.bullet_speed = bullet_speed

        for _ in range(num_asteroids):
            x = random.uniform(0, width)
            y = random.uniform(0, height)
            size = random.uniform(2, 5)
            dx = random.uniform(-1, 1)
            dy = random.uniform(-1, 1)
            self.asteroids.append(Asteroid(x, y, size, dx, dy))

    def handle_input(self, action):
        if action == "left":
            self.spaceship.rotate_left(0.2)
        elif action == "right":
            self.spaceship.rotate_right(0.2)
        elif action == "thrust":
            self.spaceship.apply_thrust(0.1)
        elif action == "shoot":
            self.bullets.append(self.spaceship.shoot(self.bullet_speed))
        elif action == "quit":
            self.game_over = True

    def update(self):
        if self.game_over:
            return

        self.spaceship.move(self.width, self.height)

        for asteroid in self.asteroids:
            asteroid.move(self.width, self.height)

        # Move bullets and remove out-of-bounds bullets
        new_bullets = []
        for bullet in self.bullets:
            if not bullet.move(self.width, self.height):
                new_bullets.append(bullet)
        self.bullets = new_bullets


        # Collision detection (Asteroids and Bullets)
        for bullet in self.bullets[:]: # Iterate over a copy
            for asteroid in self.asteroids[:]: # Iterate over a copy
                distance = math.sqrt((bullet.x - asteroid.x)**2 + (bullet.y - asteroid.y)**2)
                if distance < asteroid.size:
                    self.asteroids.remove(asteroid)
                    self.bullets.remove(bullet)
                    self.score += int(asteroid.size * 10)  # Score based on asteroid size
                    break  # Only one asteroid can be hit by a bullet at a time

        # Collision detection (Asteroids and Spaceship)
        for asteroid in self.asteroids:
            distance = math.sqrt((self.spaceship.x - asteroid.x)**2 + (self.spaceship.y - asteroid.y)**2)
            if distance < asteroid.size:
                self.game_over = True
                print("Game Over! Ship hit by asteroid.")
                break


    def draw(self):
        print("\n" * 5)  # Clear screen (crude)
        print("-" * self.width)
        print(f"Score: {self.score}")
        self.spaceship.draw()
        for asteroid in self.asteroids:
            asteroid.draw()
        for bullet in self.bullets:
            bullet.draw()
        print("-" * self.width)

        if self.game_over:
            print("GAME OVER!")

    def play(self):
        while not self.game_over:
            self.draw()
            action = input("Enter action (left, right, thrust, shoot, quit): ").lower()
            self.handle_input(action)
            self.update()
            time.sleep(0.1)  # Control game speed

        print(f"Final Score: {self.score}")


if __name__ == "__main__":
    game = AsteroidsGame()
    game.play()