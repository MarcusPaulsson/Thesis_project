import numpy as np
import os
import time
import sys

class GameOfLife:
    def __init__(self, width=20, height=10):
        self.width = width
        self.height = height
        self.board = np.zeros((height, width), dtype=int)

    def randomize(self):
        self.board = np.random.choice([0, 1], size=(self.height, self.width))

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n".join("".join("█" if cell else " " for cell in row) for row in self.board))

    def update(self):
        new_board = np.copy(self.board)
        for y in range(self.height):
            for x in range(self.width):
                alive_neighbors = np.sum(self.board[y-1:y+2, x-1:x+2]) - self.board[y, x]
                if self.board[y, x] == 1:
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        new_board[y, x] = 0
                else:
                    if alive_neighbors == 3:
                        new_board[y, x] = 1
        self.board = new_board

    def run(self, iterations=100, delay=0.5):
        for _ in range(iterations):
            self.display()
            self.update()
            time.sleep(delay)

def main():
    width = 20
    height = 10
    game = GameOfLife(width, height)
    game.randomize()
    iterations = int(input("Enter number of iterations (default 100): ") or 100)
    delay = float(input("Enter delay in seconds (default 0.5): ") or 0.5)
    game.run(iterations, delay)

if __name__ == "__main__":
    main()