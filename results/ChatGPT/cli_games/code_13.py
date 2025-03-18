import random
import sys
import os
import time
import threading

# Constants
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
SHAPES = [
    [['.....',
      '.....',
      '..X..',
      '.....',
      '.....'],
     ['.....',
      '.....',
      '..X..',
      '.....',
      '.....']],
    
    [['.....',
      '.....',
      '..X..',
      '..X..',
      '.....'],
     ['.....',
      '.....',
      '..XX.',
      '.....',
      '.....']],
    
    [['.....',
      '.....',
      '.XX..',
      '..X..',
      '.....'],
     ['.....',
      '..X..',
      '..XX.',
      '.....',
      '.....']],

    [['.....',
      '.....',
      'XX...',
      '.....',
      '.....'],
     ['.....',
      '.X...',
      '.XX..',
      '.....',
      '.....']],
    
    [['.....',
      '.....',
      '.X...',
      '.X...',
      '.....'],
     ['.....',
      '..XX.',
      '.....',
      '.....',
      '.....']],
    
    [['.....',
      '.....',
      'X....',
      'X....',
      '.....'],
     ['.....',
      '.....',
      'XXX..',
      '.....',
      '.....']],
    
    [['.....',
      '.....',
      '..X..',
      '..X..',
      '.....'],
     ['.....',
      '.XX..',
      '.....',
      '.....',
      '.....']]
]

class Tetris:
    def __init__(self):
        self.board = [['.' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.current_piece = self.new_piece()
        self.current_x = BOARD_WIDTH // 2 - 1
        self.current_y = 0
        self.game_over = False
        self.score = 0

    def new_piece(self):
        return random.choice(SHAPES)

    def rotate_piece(self):
        self.current_piece = self.current_piece[1:] + self.current_piece[:1]

    def valid_position(self, dx=0, dy=0):
        for y, row in enumerate(self.current_piece[0]):
            for x, cell in enumerate(row):
                if cell == 'X':
                    new_x = self.current_x + x + dx
                    new_y = self.current_y + y + dy
                    if new_x < 0 or new_x >= BOARD_WIDTH or new_y >= BOARD_HEIGHT:
                        return False
                    if new_y >= 0 and self.board[new_y][new_x] == 'X':
                        return False
        return True

    def merge_piece(self):
        for y, row in enumerate(self.current_piece[0]):
            for x, cell in enumerate(row):
                if cell == 'X':
                    self.board[self.current_y + y][self.current_x + x] = 'X'

    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.board) if all(cell == 'X' for cell in row)]
        for i in lines_to_clear:
            self.board.pop(i)
            self.board.insert(0, ['.' for _ in range(BOARD_WIDTH)])
        self.score += len(lines_to_clear)

    def drop_piece(self):
        if self.valid_position(dy=1):
            self.current_y += 1
        else:
            self.merge_piece()
            self.clear_lines()
            self.current_piece = self.new_piece()
            self.current_x = BOARD_WIDTH // 2 - 1
            self.current_y = 0
            if not self.valid_position():
                self.game_over = True

    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Score: {self.score}")
        for row in self.board:
            print(' '.join(row))
        print()

def game_loop(game):
    while not game.game_over:
        game.drop_piece()
        game.print_board()
        time.sleep(0.5)

def main():
    game = Tetris()
    threading.Thread(target=game_loop, args=(game,), daemon=True).start()
    
    while not game.game_over:
        command = input("Enter command (a: left, d: right, s: down, r: rotate, q: quit): ").strip()
        if command == 'a':
            if game.valid_position(dx=-1):
                game.current_x -= 1
        elif command == 'd':
            if game.valid_position(dx=1):
                game.current_x += 1
        elif command == 's':
            game.drop_piece()
        elif command == 'r':
            game.rotate_piece()
            if not game.valid_position():
                game.rotate_piece()
        elif command == 'q':
            game.game_over = True

    print("Game Over! Your score was:", game.score)

if __name__ == '__main__':
    main()