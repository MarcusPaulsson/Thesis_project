import numpy as np
import os
import time

class GameOfLife:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.board = np.zeros((height, width), dtype=int)

    def initialize(self, live_cells):
        for cell in live_cells:
            self.board[cell[0], cell[1]] = 1

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.board:
            print(' '.join(['#' if cell else '.' for cell in row]))
        print("\n")

    def update(self):
        new_board = self.board.copy()
        for y in range(self.height):
            for x in range(self.width):
                live_neighbors = self.count_live_neighbors(x, y)
                if self.board[y, x] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_board[y, x] = 0
                else:
                    if live_neighbors == 3:
                        new_board[y, x] = 1
        self.board = new_board

    def count_live_neighbors(self, x, y):
        neighbors = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        count = 0
        for dx, dy in neighbors:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                count += self.board[ny, nx]
        return count

    def run(self, generations=10, delay=0.5):
        for _ in range(generations):
            self.display()
            self.update()
            time.sleep(delay)

if __name__ == "__main__":
    game = GameOfLife(20, 20)
    initial_live_cells = [(1, 1), (1, 2), (1, 3), (2, 1), (3, 2)]
    game.initialize(initial_live_cells)
    game.run(generations=50, delay=0.5)