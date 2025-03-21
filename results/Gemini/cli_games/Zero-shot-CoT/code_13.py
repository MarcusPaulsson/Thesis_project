import random
import os
import time

class Tetris:
    """
    A command-line implementation of the Tetris game.
    """

    WIDTH = 10
    HEIGHT = 20
    SHAPES = [
        [[1, 1, 1, 1]],  # I
        [[1, 1], [1, 1]],  # O
        [[0, 1, 1], [1, 1, 0]],  # S
        [[1, 1, 0], [0, 1, 1]],  # Z
        [[1, 1, 1], [0, 0, 1]],  # J
        [[1, 1, 1], [1, 0, 0]],  # L
        [[1, 1, 1], [0, 1, 0]]  # T
    ]
    SHAPE_COLORS = ['cyan', 'yellow', 'green', 'red', 'blue', 'orange', 'purple']

    def __init__(self):
        self.board = [[' ' for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]
        self.current_piece = None
        self.current_piece_x = 0
        self.current_piece_y = 0
        self.current_piece_shape = None
        self.current_piece_color = None
        self.game_over = False
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.delay = 0.5  # Initial delay between piece drops
        self.next_piece = self.new_piece()  # Generate the next piece

    def new_piece(self):
        """
        Generates a new random piece.
        """
        shape_index = random.randint(0, len(self.SHAPES) - 1)
        shape = self.SHAPES[shape_index]
        color = self.SHAPE_COLORS[shape_index]
        return shape, color

    def spawn_piece(self):
        """
        Spawns a new piece at the top of the board.
        """
        self.current_piece_shape, self.current_piece_color = self.next_piece
        self.next_piece = self.new_piece()  # Generate the next piece
        self.current_piece = self.current_piece_shape  # Assign shape
        self.current_piece_x = self.WIDTH // 2 - len(self.current_piece[0]) // 2
        self.current_piece_y = 0
        if self.check_collision(self.current_piece, self.current_piece_x, self.current_piece_y):
            self.game_over = True
            return False
        return True

    def rotate_piece(self):
        """
        Rotates the current piece clockwise.
        """
        rotated_piece = list(zip(*self.current_piece[::-1]))
        if not self.check_collision(rotated_piece, self.current_piece_x, self.current_piece_y):
            self.current_piece = rotated_piece

    def move_piece(self, dx):
        """
        Moves the current piece horizontally.
        """
        new_x = self.current_piece_x + dx
        if not self.check_collision(self.current_piece, new_x, self.current_piece_y):
            self.current_piece_x = new_x

    def drop_piece(self):
        """
        Moves the current piece down one row.
        """
        new_y = self.current_piece_y + 1
        if not self.check_collision(self.current_piece, self.current_piece_x, new_y):
            self.current_piece_y = new_y
            return True
        else:
            self.lock_piece()
            return False

    def check_collision(self, piece, x, y):
        """
        Checks if the given piece collides with the board or the boundaries.
        """
        for row_index, row in enumerate(piece):
            for col_index, cell in enumerate(row):
                if cell:
                    board_x = x + col_index
                    board_y = y + row_index
                    if board_x < 0 or board_x >= self.WIDTH or board_y >= self.HEIGHT or (board_y >= 0 and self.board[board_y][board_x] != ' '):
                        return True
        return False

    def lock_piece(self):
        """
        Locks the current piece on the board.
        """
        for row_index, row in enumerate(self.current_piece):
            for col_index, cell in enumerate(row):
                if cell:
                    self.board[self.current_piece_y + row_index][self.current_piece_x + col_index] = self.current_piece_color[0].upper()

        self.clear_lines()
        if not self.spawn_piece():
            self.game_over = True

    def clear_lines(self):
        """
        Clears any completed lines on the board.
        """
        lines_to_clear = []
        for row_index, row in enumerate(self.board):
            if all(cell != ' ' for cell in row):
                lines_to_clear.append(row_index)

        for row_index in lines_to_clear:
            del self.board[row_index]
            self.board.insert(0, [' ' for _ in range(self.WIDTH)])

        num_lines_cleared = len(lines_to_clear)
        self.lines_cleared += num_lines_cleared
        self.score += self.calculate_score(num_lines_cleared)
        self.update_level()

    def calculate_score(self, num_lines):
        """
        Calculates the score based on the number of lines cleared.
        """
        if num_lines == 1:
            return 40 * self.level
        elif num_lines == 2:
            return 100 * self.level
        elif num_lines == 3:
            return 300 * self.level
        elif num_lines == 4:
            return 1200 * self.level
        else:
            return 0

    def update_level(self):
        """
        Updates the game level based on the number of lines cleared.
        """
        self.level = self.lines_cleared // 10 + 1
        self.delay = max(0.1, 0.5 - (self.level - 1) * 0.05)  # Decrease delay

    def print_board(self):
        """
        Prints the game board to the console.
        """
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        print("Tetris")
        print(f"Score: {self.score}  Level: {self.level}  Lines: {self.lines_cleared}")
        print("Next Piece:")
        self.print_piece(self.next_piece[0], self.next_piece[1])

        # Create a temporary board with the current piece
        temp_board = [row[:] for row in self.board]
        for row_index, row in enumerate(self.current_piece):
            for col_index, cell in enumerate(row):
                if cell:
                    try:
                        temp_board[self.current_piece_y + row_index][self.current_piece_x + col_index] = self.current_piece_color[0].upper()
                    except IndexError:
                        pass

        # Print the board with borders
        print("-" * (self.WIDTH + 2))
        for row in temp_board:
            print("|" + "".join(row) + "|")
        print("-" * (self.WIDTH + 2))

    def print_piece(self, piece, color):
        """
        Prints a piece to the console.
        """
        for row in piece:
            print("".join([color[0].upper() if cell else ' ' for cell in row]))

    def run(self):
        """
        Runs the main game loop.
        """
        self.spawn_piece()
        while not self.game_over:
            self.print_board()
            start_time = time.time()
            command = input("Enter command (a=left, d=right, s=down, w=rotate, q=quit): ").lower()
            elapsed_time = time.time() - start_time

            if command == 'a':
                self.move_piece(-1)
            elif command == 'd':
                self.move_piece(1)
            elif command == 's':
                self.drop_piece()
            elif command == 'w':
                self.rotate_piece()
            elif command == 'q':
                self.game_over = True
                break

            if not self.game_over:
                time_to_sleep = max(0, self.delay - elapsed_time)
                time.sleep(time_to_sleep)

                if not self.drop_piece():
                    self.lock_piece()

        print("Game Over!")
        print(f"Final Score: {self.score}")


if __name__ == '__main__':
    game = Tetris()
    game.run()