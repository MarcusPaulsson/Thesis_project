import random
import os
import sys
import time
import msvcrt

class Tetris:
    def __init__(self):
        self.board = [[' ' for _ in range(10)] for _ in range(20)]
        self.shapes = [
            [['#', '#', '#', '#']],  # I
            [['#', '#', '#'], [' ', '#', ' ']],  # T
            [['#', '#'], ['#', '#']],  # O
            [[' ', '#', '#'], ['#', '#', ' ']],  # S
            [['#', '#', ' '], [' ', '#', '#']],  # Z
            [['#', ' '], ['#', ' '], ['#', '#']],  # J
            [[' ', '#'], [' ', '#'], ['#', '#']]   # L
        ]
        self.current_shape = None
        self.current_position = (0, 0)
        self.score = 0
        self.game_over = False

    def new_shape(self):
        self.current_shape = random.choice(self.shapes)
        self.current_position = (0, len(self.board[0]) // 2 - len(self.current_shape[0]) // 2)

    def rotate_shape(self):
        self.current_shape = [list(row) for row in zip(*self.current_shape[::-1])]

    def can_move(self, dx, dy):
        for i, row in enumerate(self.current_shape):
            for j, cell in enumerate(row):
                if cell == '#':
                    x, y = self.current_position[0] + i + dy, self.current_position[1] + j + dx
                    if x < 0 or x >= len(self.board) or y < 0 or y >= len(self.board[0]) or (y < len(self.board[0]) and self.board[x][y] == '#'):
                        return False
        return True

    def merge_shape(self):
        for i, row in enumerate(self.current_shape):
            for j, cell in enumerate(row):
                if cell == '#':
                    self.board[self.current_position[0] + i][self.current_position[1] + j] = '#'

    def clear_lines(self):
        cleared_lines = 0
        for i in range(len(self.board) - 1, -1, -1):
            if all(cell == '#' for cell in self.board[i]):
                cleared_lines += 1
                del self.board[i]
                self.board.insert(0, [' ' for _ in range(10)])
        self.score += cleared_lines

    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.board:
            print('|' + ''.join(row) + '|')
        print(f'Score: {self.score}')
        print('Controls: [A] Left, [D] Right, [S] Down, [W] Rotate, [Q] Quit')

    def drop(self):
        while self.can_move(0, 1):
            self.current_position = (self.current_position[0] + 1, self.current_position[1])
            self.print_board()
            time.sleep(0.5)
        self.merge_shape()
        self.clear_lines()
        self.new_shape()
        if not self.can_move(0, 0):
            self.game_over = True

    def play(self):
        self.new_shape()
        while not self.game_over:
            self.print_board()
            if msvcrt.kbhit():
                key = msvcrt.getch()
                if key == b'a' and self.can_move(-1, 0):
                    self.current_position = (self.current_position[0], self.current_position[1] - 1)
                elif key == b'd' and self.can_move(1, 0):
                    self.current_position = (self.current_position[0], self.current_position[1] + 1)
                elif key == b's' and self.can_move(0, 1):
                    self.current_position = (self.current_position[0] + 1, self.current_position[1])
                elif key == b'w':
                    self.rotate_shape()
                    if not self.can_move(0, 0):
                        self.rotate_shape()  # Undo rotate if not valid
                elif key == b'q':
                    break
            self.drop()
        print("Game Over! Your score was:", self.score)

if __name__ == "__main__":
    game = Tetris()
    game.play()