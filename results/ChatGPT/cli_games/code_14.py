import random
import os
import time
import sys
import math

class AsteroidGame:
    def __init__(self, width=40, height=20, num_asteroids=5):
        self.width = width
        self.height = height
        self.player_x = width // 2
        self.player_y = height // 2
        self.asteroids = self.generate_asteroids(num_asteroids)
        self.score = 0
        self.game_over = False

    def generate_asteroids(self, num):
        return [(random.randint(0, self.width - 1), random.randint(0, self.height - 1)) for _ in range(num)]

    def draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) == (self.player_x, self.player_y):
                    print('^', end='')
                elif (x, y) in self.asteroids:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
        print(f'Score: {self.score}')

    def move_player(self, direction):
        if direction == 'w' and self.player_y > 0:
            self.player_y -= 1
        elif direction == 's' and self.player_y < self.height - 1:
            self.player_y += 1
        elif direction == 'a' and self.player_x > 0:
            self.player_x -= 1
        elif direction == 'd' and self.player_x < self.width - 1:
            self.player_x += 1

    def update(self):
        if (self.player_x, self.player_y) in self.asteroids:
            self.game_over = True
        else:
            self.score += 1
            self.asteroids = self.generate_asteroids(len(self.asteroids))

    def play(self):
        while not self.game_over:
            self.draw()
            direction = input("Move (w/a/s/d): ").lower()
            self.move_player(direction)
            self.update()
            time.sleep(0.1)
        print("Game Over! Final Score:", self.score)

if __name__ == "__main__":
    game = AsteroidGame()
    game.play()