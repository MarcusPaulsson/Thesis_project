import numpy as np
import os
import time

class GameOfLife:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros((rows, cols), dtype=int)

    def randomize(self):
        self.grid = np.random.randint(2, size=(self.rows, self.cols))

    def update(self):
        new_grid = self.grid.copy()
        for r in range(self.rows):
            for c in range(self.cols):
                live_neighbors = self.count_live_neighbors(r, c)
                if self.grid[r, c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[r, c] = 0
                else:
                    if live_neighbors == 3:
                        new_grid[r, c] = 1
        self.grid = new_grid

    def count_live_neighbors(self, r, c):
        total = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i == 0 and j == 0) or not (0 <= r + i < self.rows) or not (0 <= c + j < self.cols):
                    continue
                total += self.grid[r + i, c + j]
        return total

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.grid)

    def run(self, generations):
        self.randomize()
        for _ in range(generations):
            self.display()
            self.update()
            time.sleep(0.5)

if __name__ == "__main__":
    rows, cols = 20, 20
    game = GameOfLife(rows, cols)
    generations = 100
    game.run(generations)