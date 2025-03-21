import numpy as np
import os
import time

class GameOfLife:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.board = np.zeros((height, width), dtype=int)

    def randomize(self):
        self.board = np.random.choice([0, 1], size=(self.height, self.width))

    def update(self):
        new_board = self.board.copy()
        for i in range(self.height):
            for j in range(self.width):
                alive_neighbors = self.count_alive_neighbors(i, j)
                if self.board[i, j] == 1:  # Cell is alive
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        new_board[i, j] = 0  # Cell dies
                else:  # Cell is dead
                    if alive_neighbors == 3:
                        new_board[i, j] = 1  # Cell becomes alive
        self.board = new_board

    def count_alive_neighbors(self, x, y):
        neighbors = [
            (x-1, y-1), (x-1, y), (x-1, y+1),
            (x, y-1),           (x, y+1),
            (x+1, y-1), (x+1, y), (x+1, y+1)
        ]
        count = 0
        for nx, ny in neighbors:
            if 0 <= nx < self.height and 0 <= ny < self.width:
                count += self.board[nx, ny]
        return count

    def display(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        print(self.board)

    def run(self, generations=10, delay=1):
        for _ in range(generations):
            self.display()
            self.update()
            time.sleep(delay)

if __name__ == "__main__":
    game = GameOfLife(width=20, height=20)
    game.randomize()
    game.run(generations=50, delay=0.5)