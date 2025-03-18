import argparse
import time
import os
import random

def create_grid(rows, cols, random_fill=False, density=0.5):
    """Creates a grid for the Game of Life.

    Args:
        rows: Number of rows in the grid.
        cols: Number of columns in the grid.
        random_fill: If True, fills the grid randomly.
        density: Probability of a cell being alive if random_fill is True.

    Returns:
        A 2D list representing the grid.  Alive cells are 1, dead cells are 0.
    """
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    if random_fill:
        for i in range(rows):
            for j in range(cols):
                if random.random() < density:
                    grid[i][j] = 1
    return grid

def print_grid(grid):
    """Prints the grid to the console.

    Args:
        grid: The grid to print.
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    for row in grid:
        print(''.join(['#' if cell else ' ' for cell in row]))


def get_neighbors(grid, row, col):
    """Gets the number of live neighbors for a given cell.

    Args:
        grid: The grid.
        row: The row of the cell.
        col: The column of the cell.

    Returns:
        The number of live neighbors.
    """
    rows = len(grid)
    cols = len(grid[0])
    neighbors = 0
    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if (i, j) != (row, col):
                neighbors += grid[i][j]
    return neighbors


def next_generation(grid):
    """Calculates the next generation of the grid.

    Args:
        grid: The current grid.

    Returns:
        The next generation grid.
    """
    rows = len(grid)
    cols = len(grid[0])
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            neighbors = get_neighbors(grid, i, j)
            if grid[i][j] == 1:  # Alive cell
                if neighbors < 2 or neighbors > 3:
                    new_grid[i][j] = 0  # Dies
                else:
                    new_grid[i][j] = 1  # Survives
            else:  # Dead cell
                if neighbors == 3:
                    new_grid[i][j] = 1  # Becomes alive
    return new_grid


def game_of_life(rows, cols, generations, delay, random_fill, density):
    """Runs the Game of Life simulation.

    Args:
        rows: Number of rows in the grid.
        cols: Number of columns in the grid.
        generations: Number of generations to simulate.
        delay: Delay between generations in seconds.
        random_fill: If True, fills the grid randomly.
        density: Probability of a cell being alive if random_fill is True.
    """
    grid = create_grid(rows, cols, random_fill, density)
    for _ in range(generations):
        print_grid(grid)
        time.sleep(delay)
        grid = next_generation(grid)


def main():
    parser = argparse.ArgumentParser(description="Conway's Game of Life")
    parser.add_argument("-r", "--rows", type=int, default=20, help="Number of rows")
    parser.add_argument("-c", "--cols", type=int, default=40, help="Number of columns")
    parser.add_argument("-g", "--generations", type=int, default=100, help="Number of generations")
    parser.add_argument("-d", "--delay", type=float, default=0.1, help="Delay between generations (seconds)")
    parser.add_argument("-rand", "--random", action="store_true", help="Fill grid randomly")
    parser.add_argument("--density", type=float, default=0.5, help="Density of live cells for random fill")

    args = parser.parse_args()

    game_of_life(args.rows, args.cols, args.generations, args.delay, args.random, args.density)


if __name__ == "__main__":
    main()