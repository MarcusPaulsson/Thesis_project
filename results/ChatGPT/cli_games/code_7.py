import numpy as np
import os
import time

class GameOfLife:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = np.zeros((height, width), dtype=int)

    def initialize_random(self):
        self.board = np.random.choice([0, 1], size=(self.height, self.width))

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.board:
            print(' '.join(['█' if cell else ' ' for cell in row]))
        print("\nPress Ctrl+C to exit.")

    def update(self):
        new_board = self.board.copy()
        for y in range(self.height):
            for x in range(self.width):
                alive_neighbors = self.count_alive_neighbors(x, y)
                if self.board[y, x] == 1:
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        new_board[y, x] = 0
                else:
                    if alive_neighbors == 3:
                        new_board[y, x] = 1
        self.board = new_board

    def count_alive_neighbors(self, x, y):
        neighbors = [
            (x-1, y-1), (x-1, y), (x-1, y+1),
            (x, y-1),               (x, y+1),
            (x+1, y-1), (x+1, y), (x+1, y+1)
        ]
        count = 0
        for nx, ny in neighbors:
            if 0 <= nx < self.width and 0 <= ny < self.height:
                count += self.board[ny, nx]
        return count

def main():
    width = 20
    height = 10
    game = GameOfLife(width, height)
    game.initialize_random()
    
    try:
        while True:
            game.display()
            game.update()
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Game exited.")

if __name__ == "__main__":
    main()