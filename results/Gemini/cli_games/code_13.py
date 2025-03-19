import random
import os

class Tetris:
    """
    A command-line Tetris game.
    """

    WIDTH = 10
    HEIGHT = 20
    PIECES = [
        [[1, 1, 1, 1]],  # I
        [[1, 1], [1, 1]],  # O
        [[0, 1, 1], [1, 1, 0]],  # S
        [[1, 1, 0], [0, 1, 1]],  # Z
        [[1, 0, 0], [1, 1, 1]],  # L
        [[0, 0, 1], [1, 1, 1]],  # J
        [[0, 1, 0], [1, 1, 1]]   # T
    ]
    COLORS = ['cyan', 'yellow', 'green', 'red', 'orange', 'blue', 'purple']

    def __init__(self):
        self.grid = [[0] * self.WIDTH for _ in range(self.HEIGHT)]
        self.current_piece = None
        self.current_x = 0
        self.current_y = 0
        self.next_piece = None
        self.game_over = False
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.new_piece()
        self.next_piece = self.random_piece()  # Initialize the next piece

    def random_piece(self):
        """
        Returns a random piece and its corresponding color.
        """
        index = random.randint(0, len(self.PIECES) - 1)
        return self.PIECES[index], self.COLORS[index]

    def new_piece(self):
        """
        Generates a new piece at the top of the grid.
        """
        self.current_piece, self.current_color = self.next_piece # Use the next piece
        self.next_piece = self.random_piece() # Get a new next piece
        self.current_x = self.WIDTH // 2 - len(self.current_piece[0]) // 2
        self.current_y = 0

        if not self.is_valid_position(self.current_piece, self.current_x, self.current_y):
            self.game_over = True

    def rotate_piece(self):
        """
        Rotates the current piece clockwise.
        """
        rotated_piece = list(zip(*self.current_piece[::-1]))
        if self.is_valid_position(rotated_piece, self.current_x, self.current_y):
            self.current_piece = rotated_piece

    def move(self, dx):
        """
        Moves the current piece horizontally.
        """
        new_x = self.current_x + dx
        if self.is_valid_position(self.current_piece, new_x, self.current_y):
            self.current_x = new_x

    def drop(self):
        """
        Moves the current piece down one row.
        """
        new_y = self.current_y + 1
        if self.is_valid_position(self.current_piece, self.current_x, new_y):
            self.current_y = new_y
        else:
            self.lock_piece()

    def hard_drop(self):
        """
        Drops the piece to the lowest possible position.
        """
        while not self.game_over:
            new_y = self.current_y + 1
            if self.is_valid_position(self.current_piece, self.current_x, new_y):
                self.current_y = new_y
            else:
                self.lock_piece()
                break

    def is_valid_position(self, piece, x, y):
        """
        Checks if the given piece can be placed at the given position.
        """
        for i in range(len(piece)):
            for j in range(len(piece[0])):
                if piece[i][j]:
                    grid_x = x + j
                    grid_y = y + i

                    if grid_x < 0 or grid_x >= self.WIDTH or grid_y >= self.HEIGHT:
                        return False
                    if grid_y >= 0 and self.grid[grid_y][grid_x] != 0:
                        return False
        return True

    def lock_piece(self):
        """
        Locks the current piece into the grid.
        """
        for i in range(len(self.current_piece)):
            for j in range(len(self.current_piece[0])):
                if self.current_piece[i][j]:
                    self.grid[self.current_y + i][self.current_x + j] = self.current_color

        self.clear_lines()
        self.new_piece()

    def clear_lines(self):
        """
        Clears any full lines from the grid.
        """
        lines_to_clear = []
        for i in range(self.HEIGHT):
            if all(self.grid[i]):
                lines_to_clear.append(i)

        for line in lines_to_clear:
            del self.grid[line]
            self.grid.insert(0, [0] * self.WIDTH)

        num_lines = len(lines_to_clear)
        if num_lines > 0:
            self.lines_cleared += num_lines
            self.score += self.level * (num_lines ** 2) * 100
            if self.lines_cleared >= self.level * 10:
                self.level += 1

    def display(self):
        """
        Displays the game grid in the console.
        """
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        print("Tetris")
        print(f"Score: {self.score}, Level: {self.level}, Lines: {self.lines_cleared}")
        print("Next piece:")
        self.display_piece(self.next_piece[0])

        for i in range(self.HEIGHT):
            row = ""
            for j in range(self.WIDTH):
                cell = self.grid[i][j]
                if cell:
                    row += self.color_to_symbol(cell)
                else:
                    # Check if current piece is occupying this cell
                    occupied = False
                    for piece_row in range(len(self.current_piece)):
                        for piece_col in range(len(self.current_piece[0])):
                            if self.current_piece[piece_row][piece_col]:
                                grid_x = self.current_x + piece_col
                                grid_y = self.current_y + piece_row
                                if grid_x == j and grid_y == i:
                                    row += self.color_to_symbol(self.current_color)
                                    occupied = True
                                    break
                        if occupied:
                            break
                    if not occupied:
                        row += "."
            print(row)
        print("Controls: A - Left, D - Right, S - Down, W - Rotate, Space - Hard Drop, Q - Quit")


    def display_piece(self, piece):
        """
        Displays a piece in the console.
        """
        for row in piece:
            line = ""
            for cell in row:
                if cell:
                    line += "#"
                else:
                    line += " "
            print(line)


    def color_to_symbol(self, color):
        """
        Converts a color name to a symbol for display.
        """
        if color == 'cyan':
            return 'C'
        elif color == 'yellow':
            return 'Y'
        elif color == 'green':
            return 'G'
        elif color == 'red':
            return 'R'
        elif color == 'orange':
            return 'O'
        elif color == 'blue':
            return 'B'
        elif color == 'purple':
            return 'P'
        else:
            return '?'  # Unknown color

    def play(self):
        """
        Runs the main game loop.
        """
        while not self.game_over:
            self.display()
            action = input("Enter action (A - Left, D - Right, S - Down, W - Rotate, Space - Hard Drop, Q - Quit): ").upper()

            if action == 'A':
                self.move(-1)
            elif action == 'D':
                self.move(1)
            elif action == 'S':
                self.drop()
            elif action == 'W':
                self.rotate_piece()
            elif action == ' ':
                self.hard_drop()
            elif action == 'Q':
                self.game_over = True
            else:
                print("Invalid input.")

            if self.game_over:
                self.display()
                print("Game Over!  Final Score:", self.score)

if __name__ == "__main__":
    game = Tetris()
    game.play()