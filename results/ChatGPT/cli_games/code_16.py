import random
import os
import sys
import time
import keyboard

# Constants
WIDTH = 10
HEIGHT = 10
NUM_GHOSTS = 3
NUM_DOTS = 20

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

class Game:
    def __init__(self):
        self.pacman_pos = [1, 1]
        self.dots = self.generate_dots()
        self.ghosts = self.generate_ghosts()
        self.score = 0
        self.is_game_over = False

    def generate_dots(self):
        dots = set()
        while len(dots) < NUM_DOTS:
            pos = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
            if pos != (1, 1) and pos not in dots:
                dots.add(pos)
        return dots

    def generate_ghosts(self):
        ghosts = set()
        while len(ghosts) < NUM_GHOSTS:
            pos = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
            if pos != (1, 1) and pos not in ghosts:
                ghosts.add(pos)
        return ghosts

    def move(self, direction):
        new_x = self.pacman_pos[0] + direction[0]
        new_y = self.pacman_pos[1] + direction[1]

        if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT:
            self.pacman_pos = [new_x, new_y]
            self.check_collision()

    def check_collision(self):
        if tuple(self.pacman_pos) in self.dots:
            self.dots.remove(tuple(self.pacman_pos))
            self.score += 1
        if tuple(self.pacman_pos) in self.ghosts:
            self.is_game_over = True

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if [x, y] == self.pacman_pos:
                    print('P', end=' ')
                elif (x, y) in self.ghosts:
                    print('G', end=' ')
                elif (x, y) in self.dots:
                    print('.', end=' ')
                else:
                    print(' ', end=' ')
            print()
        print(f"Score: {self.score}")

    def play(self):
        while not self.is_game_over:
            self.display()
            time.sleep(0.1)
            if keyboard.is_pressed('w'):
                self.move(UP)
            elif keyboard.is_pressed('s'):
                self.move(DOWN)
            elif keyboard.is_pressed('a'):
                self.move(LEFT)
            elif keyboard.is_pressed('d'):
                self.move(RIGHT)
        print("Game Over! Your score was:", self.score)


if __name__ == "__main__":
    game = Game()
    game.play()