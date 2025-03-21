import random
import os
import time

class Tetris:
    """
    A command-line Tetris game implementation.
    """

    WIDTH = 10
    HEIGHT = 20
    PIECES = {
        'I': [[(0, 0), (0, 1), (0, 2), (0, 3)], [(0, 0), (1, 0), (2, 0), (3, 0)]],
        'O': [[(0, 0), (0, 1), (1, 0), (1, 1)]],
        'T': [[(0, 0), (1, 0), (2, 0), (1, 1)], [(1, 0), (1, 1), (1, 2), (0, 1)],
              [(0, 1), (1, 1), (2, 1), (1, 0)], [(0, 1), (0, 0), (0, 2), (1, 1)]],
        'L': [[(0, 0), (0, 1), (0, 2), (1, 2)], [(0, 0), (1, 0), (2, 0), (0, 1)],
              [(0, 0), (1, 0), (1, 1), (1, 2)], [(2, 0), (0, 1), (1, 1), (2, 1)]],
        'J': [[(1, 0), (1, 1), (1, 2), (0, 2)], [(0, 0), (0, 1), (1, 1), (2, 1)],
              [(0, 0), (0, 1), (0, 2), (1, 0)], [(0, 0), (1, 0), (2, 0), (2, 1)]],
        'S': [[(1, 0), (2, 0), (0, 1), (1, 1)], [(0, 0), (0, 1), (1, 1), (1, 2)]],
        'Z': [[(0, 0), (1, 0), (1, 1), (2, 1)], [(1, 0), (0, 1), (1, 1), (0, 2)]]
    }
    COLORS = {
        'I': 'cyan',
        'O': 'yellow',
        'T': 'purple',
        'L': 'orange',
        'J': 'blue',
        'S': 'green',
        'Z': 'red'
    }
    CLEAR_LINE_SCORE = 100
    TETRIS_SCORE = 800
    
    def __init__(self, width=WIDTH, height=HEIGHT):
        """
        Initializes the Tetris game.
        """
        self.width = width
        self.height = height
        self.board = [[' ' for _ in range(width)] for _ in range(height)]
        self.current_piece = None
        self.current_x = 0
        self.current_y = 0
        self.current_rotation = 0
        self.next_piece = None
        self.game_over = False
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.delay = 0.5  # Initial delay in seconds
        self.piece_bag = self.create_piece_bag()

    def create_piece_bag(self):
        """Creates a bag containing all piece types."""
        bag = list(self.PIECES.keys())
        random.shuffle(bag)
        return bag
    
    def get_next_piece_from_bag(self):
        """Gets the next piece from the bag, refilling if empty."""
        if not self.piece_bag:
            self.piece_bag = self.create_piece_bag()
        return self.piece_bag.pop()

    def new_piece(self):
        """
        Generates a new piece at the top of the board.
        """
        if self.next_piece:
            self.current_piece = self.next_piece
        else:
            self.current_piece = self.get_next_piece_from_bag()

        self.next_piece = self.get_next_piece_from_bag()
        self.current_rotation = 0
        self.current_x = self.width // 2 - 2 if self.current_piece == 'I' else self.width // 2 - 1
        self.current_y = 0

        if not self.is_valid_position():
            self.game_over = True
            return

    def rotate_piece(self):
        """
        Rotates the current piece clockwise.
        """
        original_rotation = self.current_rotation
        self.current_rotation = (self.current_rotation + 1) % len(self.PIECES[self.current_piece])
        if not self.is_valid_position():
            self.current_rotation = original_rotation

    def move(self, dx):
        """
        Moves the current piece horizontally.
        """
        self.current_x += dx
        if not self.is_valid_position():
            self.current_x -= dx

    def drop(self):
        """
        Moves the current piece down one row.
        """
        self.current_y += 1
        if not self.is_valid_position():
            self.current_y -= 1
            self.lock_piece()

    def hard_drop(self):
        """
        Drops the piece to the lowest possible position.
        """
        while not self.game_over:
            self.current_y += 1
            if not self.is_valid_position():
                self.current_y -= 1
                self.lock_piece()
                return

    def is_valid_position(self):
        """
        Checks if the current piece's position is valid.
        """
        piece_shape = self.PIECES[self.current_piece][self.current_rotation]
        for x, y in piece_shape:
            board_x = self.current_x + x
            board_y = self.current_y + y

            if board_x < 0 or board_x >= self.width or board_y >= self.height:
                return False
            if board_y >= 0 and self.board[board_y][board_x] != ' ':
                return False
        return True

    def lock_piece(self):
        """
        Locks the current piece into the board and checks for cleared lines.
        """
        piece_shape = self.PIECES[self.current_piece][self.current_rotation]
        for x, y in piece_shape:
            self.board[self.current_y + y][self.current_x + x] = self.current_piece

        self.clear_lines()
        self.new_piece()

    def clear_lines(self):
        """
        Clears any full lines from the board and updates the score.
        """
        lines_to_clear = []
        for i in range(self.height):
            if all(self.board[i][j] != ' ' for j in range(self.width)):
                lines_to_clear.append(i)

        num_lines_cleared = len(lines_to_clear)
        if num_lines_cleared > 0:
            for line_index in lines_to_clear:
                del self.board[line_index]
                self.board.insert(0, [' ' for _ in range(self.width)])

            if num_lines_cleared == 4:
                self.score += self.TETRIS_SCORE * self.level
            else:
                self.score += self.CLEAR_LINE_SCORE * num_lines_cleared * self.level

            self.lines_cleared += num_lines_cleared
            self.level = self.lines_cleared // 10 + 1
            self.delay = max(0.1, 0.5 - (self.level - 1) * 0.05)

    def draw_board(self):
        """
        Draws the current game board and score.
        """
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console

        # Print score and level information
        print(f"Score: {self.score}, Level: {self.level}, Lines: {self.lines_cleared}")

        # Print next piece
        print("Next Piece:")
        next_piece_shape = self.PIECES[self.next_piece][0]
        next_piece_grid = [[' ' for _ in range(4)] for _ in range(4)]
        for x, y in next_piece_shape:
            next_piece_grid[y][x] = self.next_piece
        for row in next_piece_grid:
            print(''.join(row))

        # Print the board
        for i in range(self.height):
            row_str = '|' + ''.join([self.board[i][j] if self.board[i][j] != ' ' else '.' for j in range(self.width)]) + '|'
            print(row_str)
        print("-" * (self.width + 2))

    def update(self):
        """
        Updates the game state.
        """
        self.drop()

    def run(self):
        """
        Runs the main game loop.
        """
        self.new_piece()
        self.next_piece = self.get_next_piece_from_bag()

        while not self.game_over:
            self.draw_board()
            start_time = time.time()
            
            # Get user input (non-blocking)
            user_input = self.get_user_input(self.delay)

            if user_input == 'q':
                break

            if user_input == 'a':
                self.move(-1)
            elif user_input == 'd':
                self.move(1)
            elif user_input == 's':
                self.drop()
            elif user_input == 'w':
                self.rotate_piece()
            elif user_input == ' ':
                self.hard_drop()

            time_elapsed = time.time() - start_time
            sleep_time = max(0, self.delay - time_elapsed)
            time.sleep(sleep_time)  # Control game speed
            self.update()

        self.draw_board()
        print("Game Over!")
        print(f"Final Score: {self.score}")

    def get_user_input(self, timeout):
        """
        Gets user input with a timeout.
        """
        import select, sys

        rlist, _, _ = select.select([sys.stdin], [], [], timeout)
        if rlist:
            return sys.stdin.readline().strip().lower()
        else:
            return ''

    def place_piece_on_board(self):
        """Places the current piece on the board for rendering."""
        piece_shape = self.PIECES[self.current_piece][self.current_rotation]
        temp_board = [row[:] for row in self.board]  # Create a copy of the board

        for x, y in piece_shape:
            board_x = self.current_x + x
            board_y = self.current_y + y

            if 0 <= board_x < self.width and 0 <= board_y < self.height:
                temp_board[board_y][board_x] = self.current_piece
        return temp_board


if __name__ == '__main__':
    game = Tetris()
    game.run()