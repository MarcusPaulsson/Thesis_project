import random
import os

class Tetris:
    """
    A command-line Tetris game.
    """

    WIDTH = 10
    HEIGHT = 20
    TETROMINOS = {
        'I': [(0, 0), (0, 1), (0, 2), (0, 3)],
        'O': [(0, 0), (0, 1), (1, 0), (1, 1)],
        'T': [(0, 0), (1, 0), (2, 0), (1, 1)],
        'S': [(0, 1), (1, 1), (1, 0), (2, 0)],
        'Z': [(0, 0), (1, 0), (1, 1), (2, 1)],
        'J': [(0, 0), (1, 0), (2, 0), (2, 1)],
        'L': [(0, 0), (1, 0), (2, 0), (0, 1)],
    }
    COLORS = {
        'I': 'cyan',
        'O': 'yellow',
        'T': 'purple',
        'S': 'green',
        'Z': 'red',
        'J': 'blue',
        'L': 'orange',
    }

    def __init__(self):
        self.board = [[' ' for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]
        self.current_piece = self.new_piece()
        self.current_x = self.WIDTH // 2 - 1
        self.current_y = 0
        self.game_over = False
        self.score = 0
        self.level = 1
        self.lines_cleared = 0

    def new_piece(self):
        """
        Generates a new random Tetromino piece.
        """
        piece_type = random.choice(list(self.TETROMINOS.keys()))
        return {'shape': self.TETROMINOS[piece_type], 'color': self.COLORS[piece_type], 'type': piece_type}

    def rotate_piece(self):
      """Rotates current piece clockwise"""
      original_piece = self.current_piece['shape']
      rotated_piece = []
      for x, y in original_piece:
          rotated_piece.append((y * -1, x))

      # Check boundaries after rotation
      min_x = min(x for x, y in rotated_piece) + self.current_x
      max_x = max(x for x, y in rotated_piece) + self.current_x
      min_y = min(y for x, y in rotated_piece) + self.current_y
      max_y = max(y for x, y in rotated_piece) + self.current_y
      if min_x < 0 or max_x >= self.WIDTH or min_y < 0 or max_y >= self.HEIGHT:
          return  # Don't rotate

      # Check for collisions after rotation
      for x, y in rotated_piece:
          board_x = x + self.current_x
          board_y = y + self.current_y
          if self.board[board_y][board_x] != ' ':
              return  # Don't rotate
      self.current_piece['shape'] = rotated_piece


    def valid_move(self, x_offset, y_offset):
        """
        Checks if moving the current piece by the given offsets is a valid move.
        """
        for x, y in self.current_piece['shape']:
            board_x = x + self.current_x + x_offset
            board_y = y + self.current_y + y_offset

            if board_x < 0 or board_x >= self.WIDTH or board_y >= self.HEIGHT:
                return False

            if board_y >= 0 and self.board[board_y][board_x] != ' ':
                return False

        return True

    def move_piece(self, x_offset, y_offset):
        """
        Moves the current piece by the given offsets if the move is valid.
        """
        if self.valid_move(x_offset, y_offset):
            self.current_x += x_offset
            self.current_y += y_offset
            return True
        else:
            return False

    def place_piece(self):
        """
        Places the current piece on the board.
        """
        for x, y in self.current_piece['shape']:
            board_x = x + self.current_x
            board_y = y + self.current_y
            self.board[board_y][board_x] = self.current_piece['color'][0].upper()  # Use first letter of color

    def clear_lines(self):
        """
        Clears any full lines from the board and updates the score.
        """
        lines_to_clear = []
        for i in range(self.HEIGHT):
            if all(cell != ' ' for cell in self.board[i]):
                lines_to_clear.append(i)

        for line_index in lines_to_clear:
            del self.board[line_index]
            self.board.insert(0, [' ' for _ in range(self.WIDTH)])
            self.score += 100 * self.level  # Increase score based on level
            self.lines_cleared += 1
            if self.lines_cleared % 10 == 0:
                self.level += 1
                print(f"Level Up! Current level: {self.level}")

    def drop_piece(self):
        """
        Drops the current piece down one row. If it can't move down, place it and generate a new piece.
        """
        if not self.move_piece(0, 1):
            self.place_piece()
            self.clear_lines()
            self.current_piece = self.new_piece()
            self.current_x = self.WIDTH // 2 - 1
            self.current_y = 0

            if not self.valid_move(0, 0):
                self.game_over = True

    def draw_board(self):
        """
        Draws the current state of the Tetris board to the console.
        """
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        print(f"Score: {self.score}  Level: {self.level}")
        print("+" + "-" * (self.WIDTH * 2) + "+")  # Top border
        for i in range(self.HEIGHT):
            row_str = "|"
            for j in range(self.WIDTH):
                cell = self.board[i][j]
                row_str += f"{cell} "  # Add space for better readability
            row_str += "|"
            print(row_str)
        print("+" + "-" * (self.WIDTH * 2) + "+")  # Bottom border

        # Draw current piece on the board (but not permanently)
        temp_board = [row[:] for row in self.board]  # Create a copy
        for x, y in self.current_piece['shape']:
            board_x = x + self.current_x
            board_y = y + self.current_y
            if 0 <= board_x < self.WIDTH and 0 <= board_y < self.HEIGHT:  # Check for valid indices
                temp_board[board_y][board_x] = self.current_piece['color'][0].upper()
        print ("\nPreview:")
        print("+" + "-" * (self.WIDTH * 2) + "+")  # Top border
        for i in range(self.HEIGHT):
            row_str = "|"
            for j in range(self.WIDTH):
                cell = temp_board[i][j]
                row_str += f"{cell} "  # Add space for better readability
            row_str += "|"
            print(row_str)
        print("+" + "-" * (self.WIDTH * 2) + "+")  # Bottom border


    def run(self):
        """
        Runs the main game loop.
        """
        while not self.game_over:
            self.draw_board()
            action = input("Enter action (a=left, d=right, s=down, w=rotate, q=quit): ").lower()

            if action == 'a':
                self.move_piece(-1, 0)
            elif action == 'd':
                self.move_piece(1, 0)
            elif action == 's':
                self.drop_piece()
            elif action == 'w':
                self.rotate_piece()
            elif action == 'q':
                break
            else:
                print("Invalid action.")

            self.drop_piece()

        self.draw_board()
        print("Game Over! Final Score:", self.score)


if __name__ == "__main__":
    game = Tetris()
    game.run()