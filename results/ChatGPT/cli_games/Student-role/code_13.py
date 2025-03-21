import random
import os
import sys
import time
import keyboard

class Tetris:
    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height
        self.board = [[' ' for _ in range(width)] for _ in range(height)]
        self.shapes = [
            [['#', '#', '#', '#']],  # I
            [['#', '#', '#'], [' ', '#', ' ']],  # T
            [['#', '#', ' '], [' ', '#', '#']],  # Z
            [[' ', '#', '#'], ['#', '#', ' ']],  # S
            [['#', '#'], ['#', '#']],  # O
            [['#', '#', '#'], ['#', ' ', ' ']],  # L
            [['#', '#', '#'], [' ', ' ', '#']],  # J
        ]
        self.current_shape = None
        self.current_position = (0, 0)
        self.score = 0
        self.game_over = False

    def new_shape(self):
        self.current_shape = random.choice(self.shapes)
        self.current_position = (0, self.width // 2 - len(self.current_shape[0]) // 2)

    def rotate_shape(self):
        self.current_shape = [list(row) for row in zip(*self.current_shape[::-1])]

    def check_collision(self, offset_x=0, offset_y=0):
        for i, row in enumerate(self.current_shape):
            for j, cell in enumerate(row):
                if cell != ' ':
                    x = self.current_position[0] + i + offset_x
                    y = self.current_position[1] + j + offset_y
                    if x < 0 or x >= self.height or y < 0 or y >= self.width or (x >= 0 and self.board[x][y] != ' '):
                        return True
        return False

    def place_shape(self):
        for i, row in enumerate(self.current_shape):
            for j, cell in enumerate(row):
                if cell != ' ':
                    x = self.current_position[0] + i
                    y = self.current_position[1] + j
                    if x >= 0:
                        self.board[x][y] = '#'
        self.clear_lines()

    def clear_lines(self):
        new_board = [row for row in self.board if any(cell == ' ' for cell in row)]
        cleared_lines = self.height - len(new_board)
        self.score += cleared_lines
        new_board = [[' ' for _ in range(self.width)] for _ in range(cleared_lines)] + new_board
        self.board = new_board

    def drop_shape(self):
        if not self.check_collision(offset_x=1):
            self.current_position = (self.current_position[0] + 1, self.current_position[1])
        else:
            self.place_shape()
            if self.current_position[0] < 0:
                self.game_over = True
            self.new_shape()

    def move_shape(self, dx):
        if not self.check_collision(offset_y=dx):
            self.current_position = (self.current_position[0], self.current_position[1] + dx)

    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.board:
            print('|' + ''.join(row) + '|')
        print('-' * (self.width + 2))
        print(f'Score: {self.score}')

    def play(self):
        self.new_shape()
        while not self.game_over:
            self.print_board()
            self.drop_shape()
            time.sleep(0.5)
            if keyboard.is_pressed('left'):
                self.move_shape(-1)
            elif keyboard.is_pressed('right'):
                self.move_shape(1)
            elif keyboard.is_pressed('down'):
                self.drop_shape()
            elif keyboard.is_pressed('up'):
                self.rotate_shape()

        print("Game Over! Final Score:", self.score)

if __name__ == "__main__":
    game = Tetris()
    game.play()