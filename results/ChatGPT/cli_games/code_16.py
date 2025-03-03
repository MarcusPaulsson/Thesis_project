import random
import os
import time
import keyboard

# Constants
WIDTH = 20
HEIGHT = 10
NUM_GHOSTS = 3
NUM_DOTS = 10
EMPTY = ' '
WALL = '#'
DOT = '.'
PACMAN = 'P'
GHOST = 'G'

class Game:
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.pacman_pos = [1, 1]
        self.ghosts = []
        self.dots = []
        self.score = 0
        self.game_over = False
        self.generate_map()

    def generate_map(self):
        self.map = [[EMPTY for _ in range(self.width)] for _ in range(self.height)]
        for i in range(self.width):
            self.map[0][i] = WALL
            self.map[self.height - 1][i] = WALL
        for i in range(1, self.height - 1):
            self.map[i][0] = WALL
            self.map[i][self.width - 1] = WALL
        self.place_dots()
        self.place_ghosts()

    def place_dots(self):
        while len(self.dots) < NUM_DOTS:
            x = random.randint(1, self.width - 2)
            y = random.randint(1, self.height - 2)
            if self.map[y][x] == EMPTY:
                self.map[y][x] = DOT
                self.dots.append((x, y))

    def place_ghosts(self):
        while len(self.ghosts) < NUM_GHOSTS:
            x = random.randint(1, self.width - 2)
            y = random.randint(1, self.height - 2)
            if self.map[y][x] == EMPTY:
                self.map[y][x] = GHOST
                self.ghosts.append((x, y))

    def draw_map(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.map[self.pacman_pos[1]][self.pacman_pos[0]] = PACMAN
        for row in self.map:
            print(''.join(row))
        self.map[self.pacman_pos[1]][self.pacman_pos[0]] = EMPTY
        print(f'Score: {self.score}')

    def move_pacman(self, dx, dy):
        new_x = self.pacman_pos[0] + dx
        new_y = self.pacman_pos[1] + dy
        if self.map[new_y][new_x] != WALL:
            if (new_x, new_y) in self.dots:
                self.score += 1
                self.dots.remove((new_x, new_y))
                self.map[new_y][new_x] = EMPTY
            self.pacman_pos = [new_x, new_y]

    def move_ghosts(self):
        for i, (gx, gy) in enumerate(self.ghosts):
            direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
            new_gx = gx + direction[0]
            new_gy = gy + direction[1]
            if self.map[new_gy][new_gx] != WALL:
                self.ghosts[i] = (new_gx, new_gy)
                if self.pacman_pos == [new_gx, new_gy]:
                    self.game_over = True

    def play(self):
        while not self.game_over:
            self.draw_map()
            if keyboard.is_pressed('w'):
                self.move_pacman(0, -1)
            elif keyboard.is_pressed('s'):
                self.move_pacman(0, 1)
            elif keyboard.is_pressed('a'):
                self.move_pacman(-1, 0)
            elif keyboard.is_pressed('d'):
                self.move_pacman(1, 0)
            self.move_ghosts()
            time.sleep(0.2)

        print("Game Over! Final Score:", self.score)

if __name__ == '__main__':
    game = Game()
    game.play()