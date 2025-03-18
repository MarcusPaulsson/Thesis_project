import random
import os
import time

class Tetris:
    """
    A command-line Tetris game.
    """

    GRID_WIDTH = 10
    GRID_HEIGHT = 20
    SHAPES = [
        [[1, 1, 1, 1]],  # I
        [[1, 1], [1, 1]],  # O
        [[0, 1, 1], [1, 1, 0]],  # S
        [[1, 1, 0], [0, 1, 1]],  # Z
        [[1, 1, 1], [0, 0, 1]],  # J
        [[1, 1, 1], [1, 0, 0]],  # L
        [[1, 1, 1], [0, 1, 0]]   # T
    ]
    COLORS = ["\033[0m", "\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m", "\033[37m"]  # ANSI color codes

    def __init__(self):
        self.grid = [[0] * self.GRID_WIDTH for _ in range(self.GRID_HEIGHT)]
        self.current_shape = None
        self.current_x = 0
        self.current_y = 0
        self.score = 0
        self.game_over = False
        self.next_shape = self.get_random_shape()
        self.level = 1
        self.drop_interval = 0.8  # Initial drop interval in seconds

    def get_random_shape(self):
        """Returns a random shape from the SHAPES list."""
        shape_index = random.randint(0, len(self.SHAPES) - 1)
        return (self.SHAPES[shape_index], shape_index + 1)  # Return shape and color index

    def spawn_shape(self):
        """Spawns a new shape at the top of the grid."""
        self.current_shape, self.current_color = self.next_shape
        self.next_shape = self.get_random_shape()
        self.current_x = self.GRID_WIDTH // 2 - len(self.current_shape[0]) // 2
        self.current_y = 0
        if not self.is_valid_position(self.current_shape, self.current_x, self.current_y):
            self.game_over = True
            return False
        return True

    def rotate_shape(self):
        """Rotates the current shape 90 degrees clockwise."""
        rotated_shape = list(zip(*self.current_shape[::-1]))
        if self.is_valid_position(rotated_shape, self.current_x, self.current_y):
            self.current_shape = rotated_shape

    def move_shape(self, dx):
        """Moves the current shape horizontally."""
        new_x = self.current_x + dx
        if self.is_valid_position(self.current_shape, new_x, self.current_y):
            self.current_x = new_x

    def drop_shape(self):
        """Drops the current shape down one row."""
        new_y = self.current_y + 1
        if self.is_valid_position(self.current_shape, self.current_x, new_y):
            self.current_y = new_y
        else:
            self.lock_shape()
            self.clear_lines()
            if not self.spawn_shape():
                self.game_over = True
            return False
        return True

    def is_valid_position(self, shape, x, y):
        """Checks if the given shape can be placed at the given position."""
        for row_index, row in enumerate(shape):
            for col_index, cell in enumerate(row):
                if cell:
                    grid_x = x + col_index
                    grid_y = y + row_index

                    if grid_x < 0 or grid_x >= self.GRID_WIDTH or grid_y >= self.GRID_HEIGHT:
                        return False
                    if grid_y >= 0 and self.grid[grid_y][grid_x] != 0:
                        return False
        return True

    def lock_shape(self):
        """Locks the current shape into the grid."""
        for row_index, row in enumerate(self.current_shape):
            for col_index, cell in enumerate(row):
                if cell:
                    self.grid[self.current_y + row_index][self.current_x + col_index] = self.current_color

    def clear_lines(self):
        """Clears any full lines from the grid."""
        lines_cleared = 0
        for row_index in range(self.GRID_HEIGHT):
            if all(self.grid[row_index]):
                del self.grid[row_index]
                self.grid.insert(0, [0] * self.GRID_WIDTH)
                lines_cleared += 1

        if lines_cleared > 0:
            self.score += self.level * (lines_cleared ** 2) * 100
            self.update_level(lines_cleared)

    def update_level(self, lines_cleared):
        """Updates the game level and drop interval based on lines cleared."""
        if self.score >= self.level * 1000:
            self.level += 1
            self.drop_interval *= 0.9  # Increase speed by decreasing interval
            print(f"Level Up!  Current Level: {self.level}")
            time.sleep(1)  # Wait for a second to display the level up message

    def draw_grid(self):
        """Draws the grid with the current shape."""
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console

        # Print score and level information
        print(f"Score: {self.score}   Level: {self.level}")

        # Print the next shape
        print("Next Shape:")
        for row in self.next_shape[0]:
            print("".join(self.COLORS[self.next_shape[1]] + "[]" + self.COLORS[0] if cell else "  " for cell in row))
        print()

        # Create a copy of the grid to draw the current shape on
        display_grid = [row[:] for row in self.grid]

        # Draw the current shape
        if self.current_shape:
            for row_index, row in enumerate(self.current_shape):
                for col_index, cell in enumerate(row):
                    if cell:
                        grid_x = self.current_x + col_index
                        grid_y = self.current_y + row_index
                        if 0 <= grid_x < self.GRID_WIDTH and 0 <= grid_y < self.GRID_HEIGHT:
                            display_grid[grid_y][grid_x] = self.current_color

        # Print the grid with colors
        print("-" * (self.GRID_WIDTH * 2 + 2))  # Top border
        for row in display_grid:
            print("|" + "".join(self.COLORS[cell] + "[]" + self.COLORS[0] if cell else "  " for cell in row) + "|")
        print("-" * (self.GRID_WIDTH * 2 + 2))  # Bottom border

    def run(self):
        """Runs the main game loop."""
        if not self.spawn_shape():
            self.game_over = True

        last_drop_time = time.time()

        while not self.game_over:
            self.draw_grid()

            # Handle user input
            user_input = input("Enter command (a=left, d=right, s=down, w=rotate, q=quit): ").lower()

            if user_input == 'a':
                self.move_shape(-1)
            elif user_input == 'd':
                self.move_shape(1)
            elif user_input == 's':
                self.drop_shape()
                last_drop_time = time.time() #Reset timer after manual drop
            elif user_input == 'w':
                self.rotate_shape()
            elif user_input == 'q':
                self.game_over = True
                break

            # Automatic drop
            current_time = time.time()
            if current_time - last_drop_time >= self.drop_interval:
                if not self.drop_shape():
                    if self.game_over:
                        break
                last_drop_time = current_time

        # Game over message
        self.draw_grid()
        print("Game Over! Your score:", self.score)


if __name__ == "__main__":
    game = Tetris()
    game.run()