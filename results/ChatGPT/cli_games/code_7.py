import numpy as np
import os
import time
import sys

class GameOfLife:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=int)

    def randomize(self, density=0.2):
        for i in range(self.height):
            for j in range(self.width):
                self.grid[i][j] = 1 if np.random.rand() < density else 0

    def update(self):
        new_grid = self.grid.copy()
        for i in range(self.height):
            for j in range(self.width):
                total = int(
                    self.grid[i, (j-1) % self.width] + 
                    self.grid[i, (j+1) % self.width] + 
                    self.grid[(i-1) % self.height, j] + 
                    self.grid[(i+1) % self.height, j] + 
                    self.grid[(i-1) % self.height, (j-1) % self.width] + 
                    self.grid[(i-1) % self.height, (j+1) % self.width] + 
                    self.grid[(i+1) % self.height, (j-1) % self.width] + 
                    self.grid[(i+1) % self.height, (j+1) % self.width]
                )

                if self.grid[i, j] == 1:
                    if total < 2 or total > 3:
                        new_grid[i, j] = 0
                else:
                    if total == 3:
                        new_grid[i, j] = 1

        self.grid = new_grid

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n".join("".join("█" if cell else " " for cell in row) for row in self.grid))

def main():
    width = 40
    height = 20
    game = GameOfLife(width, height)
    game.randomize(density=0.2)

    try:
        while True:
            game.display()
            game.update()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Game exited.")

if __name__ == "__main__":
    main()