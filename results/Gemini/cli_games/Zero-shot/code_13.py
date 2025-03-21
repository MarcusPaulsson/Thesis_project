import random
import os

class Tetris:
    """
    Implements the Tetris game with a command-line interface.
    """

    WIDTH = 10
    HEIGHT = 20
    PIECES = [
        [[1, 1, 1, 1]],  # I
        [[1, 1], [1, 1]],  # O
        [[0, 1, 1], [1, 1, 0]],  # S
        [[1, 1, 0], [0, 1, 1]],  # Z
        [[1, 1, 1], [0, 0, 1]],  # L
        [[1, 1, 1], [1, 0, 0]],  # J
        [[1, 1, 1], [0, 1, 0]]   # T
    ]

    def __init__(self):
        """
        Initializes the Tetris game.
        """
        self.board = [[0] * self.WIDTH for _ in range(self.HEIGHT)]
        self.current_piece = None
        self.current_x = 0
        self.current_y = 0
        self.game_over = False
        self.score = 0
        self.next_piece = self.new_piece()  # Store the next piece
        self.level = 1  # Initial level
        self.lines_cleared = 0  # Total lines cleared
        self.speed = 500  # Initial speed (milliseconds)
        self.delay = self.speed  # Current delay (milliseconds)

    def new_piece(self):
        """
        Generates a new random piece.
        """
        return random.choice(self.PIECES)

    def spawn_piece(self):
        """
        Spawns a new piece at the top of the board.
        """
        self.current_piece = self.next_piece
        self.next_piece = self.new_piece()
        self.current_x = self.WIDTH // 2 - len(self.current_piece[0]) // 2
        self.current_y = 0

        if self.check_collision(self.current_piece, self.current_x, self.current_y):
            self.game_over = True

    def rotate_piece(self):
        """
        Rotates the current piece clockwise.
        """
        rotated_piece = list(zip(*self.current_piece[::-1]))
        if not self.check_collision(rotated_piece, self.current_x, self.current_y):
            self.current_piece = rotated_piece

    def check_collision(self, piece, x, y):
        """
        Checks if the given piece collides with the board at the given position.
        """
        for i, row in enumerate(piece):
            for j, cell in enumerate(row):
                if cell:
                    board_x = x + j
                    board_y = y + i

                    if board_x < 0 or board_x >= self.WIDTH or board_y >= self.HEIGHT or \
                       (board_y >= 0 and self.board[board_y][board_x]):
                        return True
        return False

    def move_piece(self, dx):
        """
        Moves the current piece horizontally.
        """
        new_x = self.current_x + dx
        if not self.check_collision(self.current_piece, new_x, self.current_y):
            self.current_x = new_x

    def drop_piece(self):
        """
        Moves the current piece down one row.
        """
        new_y = self.current_y + 1
        if not self.check_collision(self.current_piece, self.current_x, new_y):
            self.current_y = new_y
            return True
        else:
            return False

    def hard_drop(self):
        """
        Drops the piece to the lowest possible position.
        """
        while not self.check_collision(self.current_piece, self.current_x, self.current_y + 1):
            self.current_y += 1
        self.fix_piece()

    def fix_piece(self):
        """
        Fixes the current piece to the board.
        """
        for i, row in enumerate(self.current_piece):
            for j, cell in enumerate(row):
                if cell:
                    self.board[self.current_y + i][self.current_x + j] = cell
        self.clear_lines()
        self.spawn_piece()

    def clear_lines(self):
        """
        Clears any full lines from the board.
        """
        lines_cleared = 0
        new_board = []
        for row in self.board:
            if all(row):
                lines_cleared += 1
            else:
                new_board.append(row)

        for _ in range(lines_cleared):
            new_board.insert(0, [0] * self.WIDTH)

        self.board = new_board
        self.lines_cleared += lines_cleared

        if lines_cleared > 0:
            self.score += self.calculate_score(lines_cleared, self.level)

        # Update level every 10 lines
        if self.lines_cleared >= self.level * 10:
            self.level += 1
            self.speed = max(100, 500 - (self.level - 1) * 20)  # Increase speed, minimum 100
            print(f"Level Up! New level: {self.level}, Speed: {self.speed}ms")

    def calculate_score(self, lines, level):
        """
        Calculates the score based on the number of lines cleared and the level.
        """
        if lines == 1:
            return 40 * level
        elif lines == 2:
            return 100 * level
        elif lines == 3:
            return 300 * level
        elif lines == 4:
            return 1200 * level
        else:
            return 0

    def draw_board(self):
        """
        Draws the Tetris board to the console.
        """
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        print("Tetris")
        print(f"Score: {self.score}  Level: {self.level}  Lines: {self.lines_cleared}")
        print("Next Piece:")
        for row in self.next_piece:
            print(''.join(['#' if cell else ' ' for cell in row]))

        for i in range(self.HEIGHT):
            row_str = ''
            for j in range(self.WIDTH):
                cell = self.board[i][j]
                # Check if the current cell is occupied by the current piece
                is_piece = False
                if self.current_piece:
                    piece_height = len(self.current_piece)
                    piece_width = len(self.current_piece[0])
                    if (self.current_y <= i < self.current_y + piece_height and
                            self.current_x <= j < self.current_x + piece_width and
                            self.current_piece[i - self.current_y][j - self.current_x]):
                        is_piece = True

                row_str += '#' if cell or is_piece else '.'
            print(row_str)

        print("Controls: A - Left, D - Right, S - Down, W - Rotate, Space - Hard Drop, Q - Quit")

    def run(self):
        """
        Runs the Tetris game loop.
        """
        self.spawn_piece()
        import time
        last_time = time.time()

        while not self.game_over:
            current_time = time.time()
            elapsed_time = (current_time - last_time) * 1000  # Convert to milliseconds

            self.draw_board()

            import select
            if select.select([sys.stdin, ], [], [], self.delay / 1000.0)[0]:
                action = sys.stdin.read(1).upper()  # Read a single character
                if action == 'A':
                    self.move_piece(-1)
                elif action == 'D':
                    self.move_piece(1)
                elif action == 'S':
                    self.drop_piece()
                elif action == 'W':
                    self.rotate_piece()
                elif action == ' ':
                    self.hard_drop()
                elif action == 'Q':
                    self.game_over = True
                    break

            if elapsed_time >= self.delay:
                if not self.drop_piece():
                    self.fix_piece()
                last_time = time.time()
            else:
                time.sleep(0.01) # Small delay to prevent busy-waiting

        self.draw_board()
        print("Game Over! Final Score:", self.score)

if __name__ == "__main__":
    import sys
    import tty
    import termios

    # Store the original terminal settings
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        # Set terminal to raw mode for character-by-character input
        tty.setraw(sys.stdin.fileno())
        game = Tetris()
        game.run()
    finally:
        # Restore the original terminal settings
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)