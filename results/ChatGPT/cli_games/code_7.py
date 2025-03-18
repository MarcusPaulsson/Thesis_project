import os
import time
import random

class GameOfLife:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.board = self.create_board()

    def create_board(self):
        return [[random.choice([0, 1]) for _ in range(self.width)] for _ in range(self.height)]

    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.board:
            print(' '.join(['█' if cell else ' ' for cell in row]))
        print("\nPress Ctrl+C to stop.")

    def update_board(self):
        new_board = [[0] * self.width for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                alive_neighbors = self.count_alive_neighbors(x, y)
                if self.board[y][x] == 1:
                    new_board[y][x] = 1 if alive_neighbors in (2, 3) else 0
                else:
                    new_board[y][x] = 1 if alive_neighbors == 3 else 0
        self.board = new_board

    def count_alive_neighbors(self, x, y):
        alive_neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                nx, ny = x + i, y + j
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    alive_neighbors += self.board[ny][nx]
        return alive_neighbors

    def run(self):
        try:
            while True:
                self.print_board()
                self.update_board()
                time.sleep(0.5)
        except KeyboardInterrupt:
            print("\nGame Over!")

if __name__ == "__main__":
    game = GameOfLife()
    game.run()