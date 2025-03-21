import random
import os
import time
import math
import sys
import keyboard

class AsteroidsGame:
    def __init__(self, width=40, height=20):
        self.width = width
        self.height = height
        self.player_pos = [width // 2, height // 2]
        self.player_angle = 0
        self.asteroids = []
        self.score = 0
        self.running = True
        self.generate_asteroids()

    def generate_asteroids(self):
        for _ in range(5):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            self.asteroids.append([x, y])

    def draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(self.height):
            for x in range(self.width):
                if [x, y] == self.player_pos:
                    print('^', end='')
                elif [x, y] in self.asteroids:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
        print(f"Score: {self.score}")

    def move_player(self, direction):
        if direction == 'left':
            self.player_angle -= 5
        elif direction == 'right':
            self.player_angle += 5

    def update(self):
        for asteroid in self.asteroids:
            if asteroid[0] < 0 or asteroid[0] >= self.width or asteroid[1] < 0 or asteroid[1] >= self.height:
                asteroid[0] = random.randint(0, self.width - 1)
                asteroid[1] = random.randint(0, self.height - 1)
            else:
                asteroid[0] += random.choice([-1, 0, 1])
                asteroid[1] += random.choice([-1, 0, 1])

            if asteroid == self.player_pos:
                self.running = False

    def play(self):
        print("Controls: Arrow Left / Arrow Right to rotate, Q to quit")
        while self.running:
            self.draw()
            if keyboard.is_pressed('left'):
                self.move_player('left')
            if keyboard.is_pressed('right'):
                self.move_player('right')
            if keyboard.is_pressed('q'):
                self.running = False
            self.update()
            time.sleep(0.1)
        print("Game Over!")

if __name__ == "__main__":
    game = AsteroidsGame()
    game.play()