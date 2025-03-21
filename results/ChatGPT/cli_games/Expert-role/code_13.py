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
            [['#', '#'], ['#', '#']],  # O
            [[' ', ' ', '#'], ['#', '#', '#']],  # L
            [['#', ' ', ' '], ['#', '#', '#']],  # J
            [['#', '#', ' '], [' ', '#', '#']],  # S
            [[' ', '#', '#'], ['#', '#', ' ']]   # Z
        ]
        self.current_shape = None
        self.current_position = (0, 0)
        self.game_over = False

    def new_shape(self):
        self.current_shape = random.choice(self.shapes)
        self.current_position = (0, self.width // 2 - len(self.current_shape[0]) // 2)

    def rotate_shape(self):
        self.current_shape = [list(row) for row in zip(*self.current_shape[::-1])]

    def can_move(self, offset_x, offset_y):
        for r, row in enumerate(self.current_shape):
            for c, cell in enumerate(row):
                if cell == '#':
                    x = self.current_position[0] + r + offset_y
                    y = self.current_position[1] + c + offset_x
                    if x < 0 or x >= self.height or y < 0 or y >= self.width or self.board[x][y] == '#':
                        return False
        return True

    def merge_shape(self):
        for r, row in enumerate(self.current_shape):
            for c, cell in enumerate(row):
                if cell == '#':
                    self.board[self.current_position[0] + r][self.current_position[1] + c] = '#'

    def clear_lines(self):
        self.board = [row for row in self.board if any(cell == ' ' for cell in row)]
        while len(self.board) < self.height:
            self.board.insert(0, [' ' for _ in range(self.width)])

    def draw_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.board:
            print('|' + ''.join(row) + '|')
        print('+' + '-' * self.width + '+')

    def drop_shape(self):
        if self.can_move(0, 1):
            self.current_position = (self.current_position[0] + 1, self.current_position[1])
        else:
            self.merge_shape()
            self.clear_lines()
            if self.current_position[0] == 0:
                self.game_over = True
            self.new_shape()

    def move_shape(self, direction):
        if self.can_move(direction, 0):
            self.current_position = (self.current_position[0], self.current_position[1] + direction)

    def play(self):
        self.new_shape()
        while not self.game_over:
            self.draw_board()
            time.sleep(0.5)
            self.drop_shape()
            if keyboard.is_pressed('left'):
                self.move_shape(-1)
            if keyboard.is_pressed('right'):
                self.move_shape(1)
            if keyboard.is_pressed('down'):
                self.drop_shape()
            if keyboard.is_pressed('up'):
                self.rotate_shape()

        print("Game Over")

if __name__ == "__main__":
    game = Tetris()
    game.play()