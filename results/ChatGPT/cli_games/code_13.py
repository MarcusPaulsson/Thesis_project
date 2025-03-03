import random
import os
import sys
import time
import keyboard

# Constants
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
TICK_RATE = 0.5  # Seconds per tick

# Tetrimino shapes
SHAPES = [
    [['.....',
      '.....',
      '..X..',
      '..X..',
      '..X..'],
     ['.....',
      '.....',
      'XXXXX',
      '.....',
      '.....']],
    
    [['.....',
      '.....',
      '..X..',
      '..XX.',
      '.....'],
     ['.....',
      '.....',
      '..X..',
      '..XX.',
      '.....'],
     ['.....',
      '.....',
      'XXXXX',
      '.....',
      '.....']],
    
    [['.....',
      '.....',
      '..X..',
      '.XX..',
      '.....'],
     ['.....',
      '.....',
      '..XX.',
      '..X..',
      '.....'],
     ['.....',
      '.....',
      'XXXXX',
      '.....',
      '.....']],
    
    [['.....',
      '.....',
      '..X..',
      '..XXX',
      '.....'],
     ['.....',
      '.....',
      'XXXXX',
      '.....',
      '.....']],
    
    [['.....',
      '.....',
      '..X..',
      '.X...',
      '.X...'],
     ['.....',
      '.....',
      'XXXXX',
      '.....',
      '.....']],
    
    [['.....',
      '.....',
      '..XX.',
      '..X..',
      '.....'],
     ['.....',
      '.....',
      'XXXXX',
      '.....',
      '.....']],
    
    [['.....',
      '.....',
      '..XX.',
      '.X...',
      '.....'],
     ['.....',
      '.....',
      'XXXXX',
      '.....',
      '.....']],
]

class Tetris:
    def __init__(self):
        self.board = [[' ' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.current_tetrimino = self.new_tetrimino()
        self.current_x = BOARD_WIDTH // 2 - 1
        self.current_y = 0
        self.score = 0

    def new_tetrimino(self):
        shape = random.choice(SHAPES)
        return [list(row) for row in shape]

    def rotate_tetrimino(self):
        self.current_tetrimino = self.current_tetrimino[1:] + self.current_tetrimino[:1]

    def draw_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.board:
            print('|' + ''.join(row) + '|')
        print('-' * (BOARD_WIDTH + 2))
        print(f'Score: {self.score}')

    def check_collision(self, dx=0, dy=0):
        for y, row in enumerate(self.current_tetrimino[0]):
            for x, cell in enumerate(row):
                if cell != '.' and (y + self.current_y + dy >= BOARD_HEIGHT or
                                    x + self.current_x + dx < 0 or
                                    x + self.current_x + dx >= BOARD_WIDTH or
                                    self.board[y + self.current_y + dy][x + self.current_x + dx] != ' '):
                    return True
        return False

    def merge_tetrimino(self):
        for y, row in enumerate(self.current_tetrimino[0]):
            for x, cell in enumerate(row):
                if cell != '.':
                    self.board[y + self.current_y][x + self.current_x] = cell

    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.board) if all(cell != ' ' for cell in row)]
        for i in lines_to_clear:
            self.board.pop(i)
            self.board.insert(0, [' ' for _ in range(BOARD_WIDTH)])
            self.score += 1

    def drop_tetrimino(self):
        if not self.check_collision(dy=1):
            self.current_y += 1
        else:
            self.merge_tetrimino()
            self.clear_lines()
            self.current_tetrimino = self.new_tetrimino()
            self.current_x = BOARD_WIDTH // 2 - 1
            self.current_y = 0
            if self.check_collision():
                print("Game Over!")
                sys.exit()

    def move_left(self):
        if not self.check_collision(dx=-1):
            self.current_x -= 1

    def move_right(self):
        if not self.check_collision(dx=1):
            self.current_x += 1

    def main_loop(self):
        while True:
            self.draw_board()
            self.drop_tetrimino()
            time.sleep(TICK_RATE)

            if keyboard.is_pressed('left'):
                self.move_left()
            if keyboard.is_pressed('right'):
                self.move_right()
            if keyboard.is_pressed('up'):
                self.rotate_tetrimino()


if __name__ == '__main__':
    game = Tetris()
    game.main_loop()