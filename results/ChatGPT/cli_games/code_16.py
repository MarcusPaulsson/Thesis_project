import random
import sys
import os
import time

# Constants
WIDTH = 10
HEIGHT = 10
NUM_GHOSTS = 2
NUM_DOTS = 5

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Game:
    def __init__(self):
        self.pacman_pos = [0, 0]
        self.dots = []
        self.ghosts = []
        self.score = 0
        self.running = True
        self.generate_items()

    def generate_items(self):
        # Place dots
        while len(self.dots) < NUM_DOTS:
            pos = [random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)]
            if pos not in self.dots and pos != self.pacman_pos:
                self.dots.append(pos)

        # Place ghosts
        while len(self.ghosts) < NUM_GHOSTS:
            pos = [random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)]
            if pos not in self.dots and pos != self.pacman_pos:
                self.ghosts.append(pos)

    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if [x, y] == self.pacman_pos:
                    print('P', end=' ')
                elif [x, y] in self.dots:
                    print('.', end=' ')
                elif [x, y] in self.ghosts:
                    print('G', end=' ')
                else:
                    print(' ', end=' ')
            print()
        print(f'Score: {self.score}')

    def move_pacman(self, direction):
        new_pos = [self.pacman_pos[0] + direction[0], self.pacman_pos[1] + direction[1]]
        if 0 <= new_pos[0] < WIDTH and 0 <= new_pos[1] < HEIGHT:
            self.pacman_pos = new_pos
            self.check_collision()

    def check_collision(self):
        if self.pacman_pos in self.dots:
            self.dots.remove(self.pacman_pos)
            self.score += 1
        if self.pacman_pos in self.ghosts:
            self.running = False

    def move_ghosts(self):
        for ghost in self.ghosts:
            direction = random.choice([UP, DOWN, LEFT, RIGHT])
            new_pos = [ghost[0] + direction[0], ghost[1] + direction[1]]
            if 0 <= new_pos[0] < WIDTH and 0 <= new_pos[1] < HEIGHT and new_pos not in self.dots:
                ghost[0], ghost[1] = new_pos

    def play(self):
        while self.running:
            self.print_board()
            move = input("Move (W/A/S/D): ").strip().upper()
            if move == 'W':
                self.move_pacman(UP)
            elif move == 'S':
                self.move_pacman(DOWN)
            elif move == 'A':
                self.move_pacman(LEFT)
            elif move == 'D':
                self.move_pacman(RIGHT)

            self.move_ghosts()

        print("Game Over! Final Score:", self.score)

if __name__ == "__main__":
    game = Game()
    game.play()