import argparse
import time
import random
import os


class GameOfLife:
    """
    Implements Conway's Game of Life.
    """

    def __init__(self, width, height, initial_density=0.3):
        """
        Initializes the game board.

        Args:
            width (int): The width of the board.
            height (int): The height of the board.
            initial_density (float): The probability of a cell being alive at the start (0.0 to 1.0).
        """
        self.width = width
        self.height = height
        self.board = self.create_initial_board(initial_density)

    def create_initial_board(self, initial_density):
        """
        Creates the initial game board with a random distribution of live cells.

        Args:
            initial_density (float): The probability of a cell being alive.

        Returns:
            list[list[int]]: A 2D list representing the game board.
        """
        board = []
        for _ in range(self.height):
            row = [1 if random.random() < initial_density else 0 for _ in range(self.width)]
            board.append(row)
        return board

    def get_neighbors(self, row, col):
        """
        Gets the number of live neighbors for a given cell.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.

        Returns:
            int: The number of live neighbors.
        """
        neighbors = 0
        for i in range(max(0, row - 1), min(self.height, row + 2)):
            for j in range(max(0, col - 1), min(self.width, col + 2)):
                if (i, j) != (row, col):
                    neighbors += self.board[i][j]
        return neighbors

    def update_board(self):
        """
        Updates the game board to the next generation based on the rules of the Game of Life.
        """
        new_board = []
        for row in range(self.height):
            new_row = []
            for col in range(self.width):
                neighbors = self.get_neighbors(row, col)
                if self.board[row][col] == 1:  # Alive cell
                    if neighbors < 2 or neighbors > 3:
                        new_row.append(0)  # Dies
                    else:
                        new_row.append(1)  # Stays alive
                else:  # Dead cell
                    if neighbors == 3:
                        new_row.append(1)  # Becomes alive
                    else:
                        new_row.append(0)  # Stays dead
            new_board.append(new_row)
        self.board = new_board

    def display_board(self):
        """
        Displays the game board in the console.
        """
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        for row in self.board:
            print(''.join(['#' if cell == 1 else ' ' for cell in row]))

    def run_simulation(self, num_generations, delay=0.1):
        """
        Runs the simulation for a specified number of generations.

        Args:
            num_generations (int): The number of generations to simulate.
            delay (float): The delay between generations in seconds.
        """
        for _ in range(num_generations):
            self.display_board()
            self.update_board()
            time.sleep(delay)


def main():
    """
    Main function to parse command-line arguments and run the Game of Life simulation.
    """
    parser = argparse.ArgumentParser(description="Conway's Game of Life")
    parser.add_argument("--width", type=int, default=60, help="Width of the board")
    parser.add_argument("--height", type=int, default=30, help="Height of the board")
    parser.add_argument("--generations", type=int, default=100, help="Number of generations to simulate")
    parser.add_argument("--density", type=float, default=0.3, help="Initial density of live cells (0.0 to 1.0)")
    parser.add_argument("--delay", type=float, default=0.1, help="Delay between generations in seconds")

    args = parser.parse_args()

    game = GameOfLife(args.width, args.height, args.density)
    game.run_simulation(args.generations, args.delay)


if __name__ == "__main__":
    main()