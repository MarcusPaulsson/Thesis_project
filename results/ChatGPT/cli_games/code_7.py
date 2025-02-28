import os
import time
import random

class GameOfLife:
    def __init__(self, width=20, height=20, live_cells=None):
        self.width = width
        self.height = height
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        if live_cells:
            for x, y in live_cells:
                self.set_cell(x, y, 1)

    def set_cell(self, x, y, state):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.board[y][x] = state

    def get_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.board[y][x]
        return 0

    def count_live_neighbors(self, x, y):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        count = 0
        for dx, dy in directions:
            count += self.get_cell(x + dx, y + dy)
        return count

    def update(self):
        new_board = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                live_neighbors = self.count_live_neighbors(x, y)
                if self.get_cell(x, y) == 1:
                    if live_neighbors in (2, 3):
                        new_board[y][x] = 1
                else:
                    if live_neighbors == 3:
                        new_board[y][x] = 1
        self.board = new_board

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.board:
            print(' '.join(['#' if cell else '.' for cell in row]))
        print(f"Press Ctrl+C to stop.")

    def randomize(self, density=0.2):
        for y in range(self.height):
            for x in range(self.width):
                self.set_cell(x, y, 1 if random.random() < density else 0)

def main():
    width = 20
    height = 20
    game = GameOfLife(width, height)
    game.randomize(density=0.3)

    try:
        while True:
            game.display()
            game.update()
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Game stopped.")

if __name__ == "__main__":
    main()