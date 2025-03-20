import random
import os
import sys
import time
import keyboard

class Tetris:
    WIDTH = 10
    HEIGHT = 20
    SHAPES = [
        [[1, 1, 1, 1]],  # I
        [[1, 1], [1, 1]],  # O
        [[0, 1, 0], [1, 1, 1]],  # T
        [[1, 1, 0], [0, 1, 1]],  # S
        [[0, 1, 1], [1, 1, 0]],  # Z
        [[1, 0, 0], [1, 1, 1]],  # L
        [[0, 0, 1], [1, 1, 1]],  # J
    ]

    def __init__(self):
        self.board = [[0] * self.WIDTH for _ in range(self.HEIGHT)]
        self.current_piece = self.new_piece()
        self.current_position = [0, self.WIDTH // 2 - len(self.current_piece[0]) // 2]
        self.game_over = False

    def new_piece(self):
        return random.choice(self.SHAPES)

    def rotate_piece(self):
        self.current_piece = [list(row) for row in zip(*self.current_piece[::-1])]

    def can_move(self, dx, dy):
        for r, row in enumerate(self.current_piece):
            for c, val in enumerate(row):
                if val:
                    new_r = r + self.current_position[0] + dy
                    new_c = c + self.current_position[1] + dx
                    if (new_r >= self.HEIGHT or new_c < 0 or new_c >= self.WIDTH or
                            (new_r >= 0 and self.board[new_r][new_c])):
                        return False
        return True

    def place_piece(self):
        for r, row in enumerate(self.current_piece):
            for c, val in enumerate(row):
                if val:
                    self.board[r + self.current_position[0]][c + self.current_position[1]] = 1
        self.clear_lines()

    def clear_lines(self):
        new_board = [row for row in self.board if any(val == 0 for val in row)]
        lines_cleared = self.HEIGHT - len(new_board)
        self.board = [[0] * self.WIDTH for _ in range(lines_cleared)] + new_board

    def drop_piece(self):
        if self.can_move(0, 1):
            self.current_position[0] += 1
        else:
            self.place_piece()
            self.current_piece = self.new_piece()
            self.current_position = [0, self.WIDTH // 2 - len(self.current_piece[0]) // 2]
            if not self.can_move(0, 0):
                self.game_over = True

    def draw_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for r in range(self.HEIGHT):
            row = ''.join(['#' if self.board[r][c] else '.' for c in range(self.WIDTH)])
            print(row)
        print("\nControls: [A] Left, [D] Right, [S] Down, [W] Rotate, [Q] Quit")

    def run(self):
        while not self.game_over:
            self.draw_board()
            time.sleep(0.1)
            if keyboard.is_pressed('a') and self.can_move(-1, 0):
                self.current_position[1] -= 1
            if keyboard.is_pressed('d') and self.can_move(1, 0):
                self.current_position[1] += 1
            if keyboard.is_pressed('s'):
                self.drop_piece()
            if keyboard.is_pressed('w'):
                self.rotate_piece()
            self.drop_piece()
        print("Game Over!")

if __name__ == "__main__":
    game = Tetris()
    game.run()