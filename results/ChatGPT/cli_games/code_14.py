import random
import os
import sys
import time
import math
import threading

# Constants
WIDTH = 40
HEIGHT = 20
ASTEROID_COUNT = 5
SHIP_SYMBOL = 'A'
ASTEROID_SYMBOL = 'O'
BULLET_SYMBOL = '|'
BULLET_LIMIT = 5

# Directions
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

class Game:
    def __init__(self):
        self.ship_position = [WIDTH // 2, HEIGHT // 2]
        self.asteroids = []
        self.bullets = []
        self.score = 0
        self.is_running = True
        self.spawn_asteroids()

    def spawn_asteroids(self):
        for _ in range(ASTEROID_COUNT):
            x = random.randint(0, WIDTH - 1)
            y = random.randint(0, HEIGHT - 1)
            self.asteroids.append([x, y])

    def draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if [x, y] == self.ship_position:
                    print(SHIP_SYMBOL, end='')
                elif [x, y] in self.asteroids:
                    print(ASTEROID_SYMBOL, end='')
                elif any(bullet[0] == x and bullet[1] == y for bullet in self.bullets):
                    print(BULLET_SYMBOL, end='')
                else:
                    print(' ', end='')
            print()
        print(f'Score: {self.score}')

    def move_ship(self, direction):
        if direction == UP and self.ship_position[1] > 0:
            self.ship_position[1] -= 1
        elif direction == DOWN and self.ship_position[1] < HEIGHT - 1:
            self.ship_position[1] += 1
        elif direction == LEFT and self.ship_position[0] > 0:
            self.ship_position[0] -= 1
        elif direction == RIGHT and self.ship_position[0] < WIDTH - 1:
            self.ship_position[0] += 1

    def shoot(self):
        if len(self.bullets) < BULLET_LIMIT:
            self.bullets.append([self.ship_position[0], self.ship_position[1] - 1])

    def update_bullets(self):
        new_bullets = []
        for bullet in self.bullets:
            bullet[1] -= 1
            if bullet[1] >= 0:
                new_bullets.append(bullet)
                self.check_collision(bullet)
        self.bullets = new_bullets

    def check_collision(self, bullet):
        for asteroid in self.asteroids:
            if bullet[0] == asteroid[0] and bullet[1] == asteroid[1]:
                self.asteroids.remove(asteroid)
                self.score += 1
                self.spawn_asteroids()
                break

    def run(self):
        while self.is_running:
            self.draw()
            command = input("Move (WASD) or Shoot (Space): ").strip().lower()
            if command == 'w':
                self.move_ship(UP)
            elif command == 's':
                self.move_ship(DOWN)
            elif command == 'a':
                self.move_ship(LEFT)
            elif command == 'd':
                self.move_ship(RIGHT)
            elif command == ' ':
                self.shoot()
            self.update_bullets()
            time.sleep(0.1)

if __name__ == "__main__":
    game = Game()
    game.run()