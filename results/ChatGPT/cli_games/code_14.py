import random
import os
import time
import sys
import tty
import termios

# Constants
WIDTH = 40
HEIGHT = 20
ASTEROID_COUNT = 5
SHIP_SYMBOL = '^'
ASTEROID_SYMBOL = 'O'
EMPTY_SPACE = ' '

class Game:
    def __init__(self):
        self.ship_position = WIDTH // 2
        self.asteroids = self.generate_asteroids()
        self.score = 0
        self.game_over = False

    def generate_asteroids(self):
        return [random.randint(0, WIDTH - 1) for _ in range(ASTEROID_COUNT)]

    def draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(HEIGHT):
            if y == HEIGHT - 1:
                row = [' '] * WIDTH
                row[self.ship_position] = SHIP_SYMBOL
                print(''.join(row))
            else:
                row = [' '] * WIDTH
                for asteroid in self.asteroids:
                    if asteroid == y:
                        row[random.randint(0, WIDTH - 1)] = ASTEROID_SYMBOL
                print(''.join(row))
        print(f'Score: {self.score}')

    def update(self):
        for i in range(len(self.asteroids)):
            if self.asteroids[i] < HEIGHT - 1:
                self.asteroids[i] += 1
            else:
                self.asteroids[i] = 0
                self.asteroids[i] = random.randint(0, WIDTH - 1)
                self.score += 1
            
            # Check for collision
            if self.asteroids[i] == HEIGHT - 1 and self.ship_position == self.asteroids[i]:
                self.game_over = True

    def run(self):
        try:
            print("Use 'a' to move left, 'd' to move right, 'q' to quit.")
            while not self.game_over:
                self.draw()
                self.update()
                time.sleep(0.1)
                self.handle_input()
        finally:
            print("Game Over! Your score was:", self.score)

    def handle_input(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            if sys.stdin.read(1) == 'a':
                self.ship_position = max(0, self.ship_position - 1)
            elif sys.stdin.read(1) == 'd':
                self.ship_position = min(WIDTH - 1, self.ship_position + 1)
            elif sys.stdin.read(1) == 'q':
                self.game_over = True
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

if __name__ == '__main__':
    game = Game()
    game.run()