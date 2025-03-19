import os
import time
import random

class GameOfLife:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.grid = self._create_grid()

    def _create_grid(self):
        return [[random.choice([0, 1]) for _ in range(self.width)] for _ in range(self.height)]

    def _print_grid(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.grid:
            print(' '.join(['█' if cell else ' ' for cell in row]))

    def _count_neighbors(self, x, y):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.height and 0 <= ny < self.width:
                count += self.grid[nx][ny]
        return count

    def _update_grid(self):
        new_grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for x in range(self.height):
            for y in range(self.width):
                neighbors = self._count_neighbors(x, y)
                if self.grid[x][y] == 1 and neighbors in (2, 3):
                    new_grid[x][y] = 1
                elif self.grid[x][y] == 0 and neighbors == 3:
                    new_grid[x][y] = 1
        self.grid = new_grid

    def play(self, generations=10, delay=0.5):
        for _ in range(generations):
            self._print_grid()
            self._update_grid()
            time.sleep(delay)

if __name__ == "__main__":
    game = GameOfLife()
    game.play(generations=20, delay=0.5)