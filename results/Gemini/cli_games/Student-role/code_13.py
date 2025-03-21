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
        [[0, 1, 1], [1, 1, 0]],  # Z
        [[1, 1, 0], [0, 1, 1]],  # S
        [[1, 0, 0], [1, 1, 1]],  # L
        [[0, 0, 1], [1, 1, 1]],  # J
        [[0, 1, 0], [1, 1, 1]]   # T
    ]
    COLORS = [
        0,  # Empty
        1,  # I - Cyan
        2,  # O - Yellow
        3,  # Z - Red
        4,  # S - Green
        5,  # L - Orange
        6,  # J - Blue
        7   # T - Purple
    ]

    def __init__(self):
        self.board = [[0] * self.WIDTH for _ in range(self.HEIGHT)]
        self.current_piece = None
        self.current_x = 0
        self.current_y = 0
        self.game_over = False
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.next_piece = random.choice(self.PIECES)
        self.new_piece()

    def new_piece(self):
        """
        Generates a new piece at the top of the board.
        """
        self.current_piece = self.next_piece
        self.next_piece = random.choice(self.PIECES)
        self.current_x = self.WIDTH // 2 - len(self.current_piece[0]) // 2
        self.current_y = 0
        if not self.is_valid_position(self.current_piece, self.current_x, self.current_y):
            self.game_over = True

    def rotate(self):
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
            self.freeze()
            self.clear_lines()
            if not self.game_over:
                self.new_piece()

    def hard_drop(self):
        """
        Drops the piece to the lowest possible position.
        """
        while not self.game_over:
            new_y = self.current_y + 1
            if self.is_valid_position(self.current_piece, self.current_x, new_y):
                self.current_y = new_y
            else:
                self.freeze()
                self.clear_lines()
                if not self.game_over:
                    self.new_piece()
                break

    def is_valid_position(self, piece, x, y):
        """
        Checks if a piece can be placed at the given position.
        """
        for i, row in enumerate(piece):
            for j, cell in enumerate(row):
                if cell:
                    board_x = x + j
                    board_y = y + i
                    if board_x < 0 or board_x >= self.WIDTH or board_y >= self.HEIGHT:
                        return False
                    if board_y >= 0 and self.board[board_y][board_x] != 0:
                        return False
        return True

    def freeze(self):
        """
        Places the current piece on the board.
        """
        for i, row in enumerate(self.current_piece):
            for j, cell in enumerate(row):
                if cell:
                    self.board[self.current_y + i][self.current_x + j] = self.COLORS[self.PIECES.index(self.current_piece) + 1] # Assign color based on piece index

    def clear_lines(self):
        """
        Clears any full lines on the board.
        """
        lines_cleared = 0
        new_board = []
        for row in self.board:
            if all(cell != 0 for cell in row):
                lines_cleared += 1
            else:
                new_board.append(row)

        for _ in range(lines_cleared):
            new_board.insert(0, [0] * self.WIDTH)

        self.board = new_board
        self.lines_cleared += lines_cleared
        self.update_score(lines_cleared)
        self.update_level()

    def update_score(self, lines_cleared):
        """
        Updates the score based on the number of lines cleared.
        """
        if lines_cleared == 1:
            self.score += 40 * self.level
        elif lines_cleared == 2:
            self.score += 100 * self.level
        elif lines_cleared == 3:
            self.score += 300 * self.level
        elif lines_cleared == 4:
            self.score += 1200 * self.level

    def update_level(self):
        """
        Updates the level based on the number of lines cleared.
        """
        self.level = (self.lines_cleared // 10) + 1

    def draw(self):
        """
        Draws the current state of the game.
        """
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        print("Tetris")
        print(f"Score: {self.score}  Level: {self.level}  Lines: {self.lines_cleared}")

        # Draw the board
        for i in range(self.HEIGHT):
            row_str = "|"
            for j in range(self.WIDTH):
                cell = self.board[i][j]
                if cell == 0:
                    row_str += "  "
                else:
                    row_str += str(cell) + " "
            row_str += "|"
            print(row_str)

        # Draw the bottom border
        print("-" * (self.WIDTH * 2 + 2))

        # Draw the next piece
        print("\nNext Piece:")
        for row in self.next_piece:
            row_str = ""
            for cell in row:
                if cell == 0:
                    row_str += "  "
                else:
                    row_str += str(self.COLORS[self.PIECES.index(self.next_piece) + 1]) + " "
            print(row_str)

    def run(self):
        """
        Runs the main game loop.
        """
        while not self.game_over:
            self.draw()
            action = input("Action (a=left, d=right, s=down, w=rotate, space=hard drop, q=quit): ").lower()

            if action == 'a':
                self.move(-1)
            elif action == 'd':
                self.move(1)
            elif action == 's':
                self.drop()
            elif action == 'w':
                self.rotate()
            elif action == ' ':
                self.hard_drop()
            elif action == 'q':
                self.game_over = True
            else:
                print("Invalid action.")

            if not self.game_over:
                self.drop()  # Automatically drop the piece

        self.draw()
        print("Game Over! Final Score:", self.score)


if __name__ == '__main__':
    game = Tetris()
    game.run()