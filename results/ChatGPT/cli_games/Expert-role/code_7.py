import os
import time
from typing import List

class GameOfLife:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.board = self.create_empty_board()

    def create_empty_board(self) -> List[List[int]]:
        return [[0 for _ in range(self.width)] for _ in range(self.height)]

    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.board:
            print(' '.join('█' if cell else ' ' for cell in row))
        print("\n")

    def set_initial_state(self, initial_state: List[tuple]):
        for x, y in initial_state:
            self.board[y][x] = 1

    def get_neighbors_count(self, x: int, y: int) -> int:
        neighbors = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        count = 0
        for dx, dy in neighbors:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                count += self.board[ny][nx]
        return count

    def update_board(self):
        new_board = self.create_empty_board()
        for y in range(self.height):
            for x in range(self.width):
                neighbors_count = self.get_neighbors_count(x, y)
                if self.board[y][x] == 1:
                    if neighbors_count in (2, 3):
                        new_board[y][x] = 1
                else:
                    if neighbors_count == 3:
                        new_board[y][x] = 1
        self.board = new_board

    def run(self, iterations: int = 10, delay: float = 0.5):
        for _ in range(iterations):
            self.print_board()
            self.update_board()
            time.sleep(delay)

if __name__ == "__main__":
    game = GameOfLife(width=10, height=10)
    initial_state = [(1, 1), (1, 2), (1, 3), (2, 2), (3, 1), (3, 2), (3, 3)]
    game.set_initial_state(initial_state)
    game.run(iterations=50, delay=0.2)