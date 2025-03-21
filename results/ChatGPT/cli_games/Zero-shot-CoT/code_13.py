import random
import os
import sys
import time
import threading

class Tetris:
    # Define shapes of the Tetriminos
    shapes = [
        [['.....',
          '.....',
          '..00.',
          '..00.',
          '.....'],
         'O'],
        
        [['.....',
          '.....',
          '..0..',
          '..000',
          '.....'],
         'T'],
        
        [['.....',
          '.....',
          '.0...',
          '.000.',
          '.....'],
         'L'],
        
        [['.....',
          '.....',
          '...0.',
          '.000.',
          '.....'],
         'J'],
        
        [['.....',
          '.....',
          '..0..',
          '.00..',
          '.0...'],
         'S'],
        
        [['.....',
          '.....',
          '.0...',
          '..00.',
          '..0..'],
         'Z'],
        
        [['.....',
          '.....',
          '..0..',
          '..0..',
          '..00.'],
         'I']
    ]

    def __init__(self):
        self.board = [['.' for _ in range(10)] for _ in range(20)]
        self.current_piece = None
        self.current_x = 0
        self.current_y = 0
        self.score = 0
        self.game_over = False
        self.game_thread = threading.Thread(target=self.run)
        self.game_thread.start()

    def new_piece(self):
        self.current_piece = random.choice(self.shapes)
        self.current_x = 3
        self.current_y = 0

    def rotate_piece(self):
        self.current_piece[0] = [''.join(row) for row in zip(*self.current_piece[0][::-1])]

    def valid_move(self, dx, dy):
        for y, row in enumerate(self.current_piece[0]):
            for x, cell in enumerate(row):
                if cell == '0':
                    new_x = self.current_x + x + dx
                    new_y = self.current_y + y + dy
                    if new_x < 0 or new_x >= len(self.board[0]) or new_y >= len(self.board):
                        return False
                    if new_y >= 0 and self.board[new_y][new_x] != '.':
                        return False
        return True

    def lock_piece(self):
        for y, row in enumerate(self.current_piece[0]):
            for x, cell in enumerate(row):
                if cell == '0':
                    self.board[self.current_y + y][self.current_x + x] = '0'
        self.clear_lines()
        self.new_piece()
        if not self.valid_move(0, 0):
            self.game_over = True

    def clear_lines(self):
        new_board = [row for row in self.board if any(cell == '.' for cell in row)]
        cleared_lines = len(self.board) - len(new_board)
        self.score += cleared_lines
        self.board = [['.' for _ in range(10)] for _ in range(cleared_lines)] + new_board

    def drop(self):
        if self.valid_move(0, 1):
            self.current_y += 1
        else:
            self.lock_piece()

    def run(self):
        self.new_piece()
        while not self.game_over:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.draw_board()
            self.drop()
            time.sleep(0.5)

    def draw_board(self):
        for y in range(len(self.board)):
            line = ''
            for x in range(len(self.board[y])):
                if self.current_y <= y < self.current_y + len(self.current_piece[0]) and \
                        self.current_x <= x < self.current_x + len(self.current_piece[0][0]) and \
                        self.current_piece[0][y - self.current_y][x - self.current_x] == '0':
                    line += '0'
                else:
                    line += self.board[y][x]
            print(line)
        print(f'Score: {self.score}')
        if self.game_over:
            print("Game Over!")

    def move_left(self):
        if self.valid_move(-1, 0):
            self.current_x -= 1

    def move_right(self):
        if self.valid_move(1, 0):
            self.current_x += 1

    def move_down(self):
        self.drop()

    def rotate(self):
        self.rotate_piece()
        if not self.valid_move(0, 0):
            self.rotate_piece()  # Rotate back if not valid

def main():
    game = Tetris()
    
    while not game.game_over:
        command = input("Enter command (l=left, r=right, d=down, t=rotate, q=quit): ")
        if command == 'l':
            game.move_left()
        elif command == 'r':
            game.move_right()
        elif command == 'd':
            game.move_down()
        elif command == 't':
            game.rotate()
        elif command == 'q':
            game.game_over = True

if __name__ == "__main__":
    main()