import random
import os
import sys
import time
import math

class AsteroidGame:
    def __init__(self):
        self.width = 40
        self.height = 20
        self.player_pos = [self.width // 2, self.height // 2]
        self.asteroids = []
        self.score = 0
        self.game_over = False
        self.generate_asteroids()

    def generate_asteroids(self, count=5):
        for _ in range(count):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            self.asteroids.append([x, y])

    def draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(self.height):
            for x in range(self.width):
                if [x, y] == self.player_pos:
                    print('A', end='')
                elif [x, y] in self.asteroids:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
        print(f'Score: {self.score}')

    def move_player(self, direction):
        if direction == 'w' and self.player_pos[1] > 0:
            self.player_pos[1] -= 1
        elif direction == 's' and self.player_pos[1] < self.height - 1:
            self.player_pos[1] += 1
        elif direction == 'a' and self.player_pos[0] > 0:
            self.player_pos[0] -= 1
        elif direction == 'd' and self.player_pos[0] < self.width - 1:
            self.player_pos[0] += 1

    def check_collision(self):
        if self.player_pos in self.asteroids:
            self.game_over = True

    def run(self):
        while not self.game_over:
            self.draw()
            command = input('Move (w/a/s/d): ').strip().lower()
            if command in ['w', 'a', 's', 'd']:
                self.move_player(command)
                self.check_collision()
                self.score += 1
            else:
                print('Invalid command!')
            time.sleep(0.1)
        
        print('Game Over! Your score:', self.score)

if __name__ == "__main__":
    game = AsteroidGame()
    game.run()