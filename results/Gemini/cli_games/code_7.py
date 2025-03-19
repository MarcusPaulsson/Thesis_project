import argparse
import time
import os
import random


class GameOfLife:
    """
    Implementation of Conway's Game of Life.
    """

    def __init__(self, width, height, initial_density=0.3):
        """
        Initializes the Game of Life grid.

        Args:
            width (int): Width of the grid.
            height (int): Height of the grid.
            initial_density (float): Probability of a cell being alive initially (0 to 1).
        """
        self.width = width
        self.height = height
        self.grid = [[(random.random() < initial_density) for _ in range(width)] for _ in range(height)]

    def __str__(self):
        """
        Returns a string representation of the grid.
        """
        output = ""
        for row in self.grid:
            output += "".join(["#" if cell else " " for cell in row]) + "\n"
        return output

    def clear_screen(self):
        """
        Clears the console screen.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_neighbors(self, row, col):
        """
        Gets the number of alive neighbors for a given cell.

        Args:
            row (int): Row index of the cell.
            col (int): Column index of the cell.

        Returns:
            int: Number of alive neighbors.
        """
        neighbors = 0
        for i in range(max(0, row - 1), min(self.height, row + 2)):
            for j in range(max(0, col - 1), min(self.width, col + 2)):
                if (i, j) != (row, col) and self.grid[i][j]:
                    neighbors += 1
        return neighbors

    def update(self):
        """
        Updates the grid to the next generation.
        """
        new_grid = [[False for _ in range(self.width)] for _ in range(self.height)]

        for row in range(self.height):
            for col in range(self.width):
                neighbors = self.get_neighbors(row, col)
                if self.grid[row][col]:  # Alive cell
                    if neighbors == 2 or neighbors == 3:
                        new_grid[row][col] = True
                else:  # Dead cell
                    if neighbors == 3:
                        new_grid[row][col] = True

        self.grid = new_grid

    def run(self, generations, delay=0.1):
        """
        Runs the Game of Life for a specified number of generations.

        Args:
            generations (int): Number of generations to run.
            delay (float): Delay in seconds between each generation.
        """
        for _ in range(generations):
            self.clear_screen()
            print(self)
            self.update()
            time.sleep(delay)


def main():
    """
    Main function to parse command-line arguments and run the Game of Life.
    """
    parser = argparse.ArgumentParser(description="Conway's Game of Life in Python")
    parser.add_argument("--width", type=int, default=60, help="Width of the grid (default: 60)")
    parser.add_argument("--height", type=int, default=30, help="Height of the grid (default: 30)")
    parser.add_argument("--generations", type=int, default=100, help="Number of generations to run (default: 100)")
    parser.add_argument("--delay", type=float, default=0.1, help="Delay between generations in seconds (default: 0.1)")
    parser.add_argument("--density", type=float, default=0.3, help="Initial density of alive cells (default: 0.3)")

    args = parser.parse_args()

    game = GameOfLife(args.width, args.height, args.density)
    game.run(args.generations, args.delay)


if __name__ == "__main__":
    main()