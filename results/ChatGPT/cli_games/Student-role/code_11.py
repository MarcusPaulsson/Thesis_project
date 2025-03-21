import random

class LightsOut:
    def __init__(self, size=5):
        self.size = size
        self.grid = [[random.choice([0, 1]) for _ in range(size)] for _ in range(size)]

    def display(self):
        for row in self.grid:
            print(' '.join(['*' if cell else ' ' for cell in row]))
        print()

    def toggle(self, x, y):
        self.grid[x][y] ^= 1  # Toggle the selected light
        # Toggle adjacent lights
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size:
                self.grid[nx][ny] ^= 1

    def is_solved(self):
        return all(cell == 0 for row in self.grid for cell in row)

    def play(self):
        print("Welcome to Lights Out!")
        while not self.is_solved():
            self.display()
            try:
                x, y = map(int, input("Enter coordinates to toggle (row col): ").split())
                if 0 <= x < self.size and 0 <= y < self.size:
                    self.toggle(x, y)
                else:
                    print("Coordinates out of bounds. Try again.")
            except ValueError:
                print("Invalid input. Please enter row and column as two integers.")

        print("Congratulations! You've turned off all the lights!")

if __name__ == "__main__":
    game = LightsOut()
    game.play()