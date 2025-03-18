import random
import os
import time

# Constants
WALL = '#'
SPACE = ' '
PACMAN = 'P'
DOT = '.'
GHOST = 'G'
WIDTH = 10
HEIGHT = 10
NUM_GHOSTS = 2
NUM_DOTS = 10

class Game:
    def __init__(self):
        self.board = self.create_board()
        self.pacman_position = (0, 0)
        self.score = 0
        self.ghosts = self.place_ghosts()
        self.game_over = False

    def create_board(self):
        board = [[SPACE for _ in range(WIDTH)] for _ in range(HEIGHT)]
        # Place walls
        for i in range(WIDTH):
            board[0][i] = WALL
            board[HEIGHT - 1][i] = WALL
        for i in range(HEIGHT):
            board[i][0] = WALL
            board[i][WIDTH - 1] = WALL
        # Place dots
        for _ in range(NUM_DOTS):
            while True:
                x, y = random.randint(1, HEIGHT - 2), random.randint(1, WIDTH - 2)
                if board[x][y] == SPACE:
                    board[x][y] = DOT
                    break
        return board

    def place_ghosts(self):
        ghosts = []
        for _ in range(NUM_GHOSTS):
            while True:
                x, y = random.randint(1, HEIGHT - 2), random.randint(1, WIDTH - 2)
                if (x, y) != self.pacman_position and self.board[x][y] == SPACE:
                    ghosts.append((x, y))
                    self.board[x][y] = GHOST
                    break
        return ghosts

    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if (y, x) == self.pacman_position:
                    print(PACMAN, end='')
                else:
                    print(self.board[y][x], end='')
            print()
        print(f'Score: {self.score}')

    def move_pacman(self, direction):
        x, y = self.pacman_position
        if direction == 'w' and x > 0:
            x -= 1
        elif direction == 's' and x < HEIGHT - 1:
            x += 1
        elif direction == 'a' and y > 0:
            y -= 1
        elif direction == 'd' and y < WIDTH - 1:
            y += 1
        if self.board[x][y] != WALL:
            self.pacman_position = (x, y)
            if self.board[x][y] == DOT:
                self.score += 1
                self.board[x][y] = SPACE
            self.check_game_over()

    def check_game_over(self):
        for ghost in self.ghosts:
            if ghost == self.pacman_position:
                self.game_over = True

    def move_ghosts(self):
        for i in range(len(self.ghosts)):
            x, y = self.ghosts[i]
            move = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])  # random move
            new_x, new_y = x + move[0], y + move[1]
            if self.board[new_x][new_y] == SPACE:
                self.board[x][y] = SPACE
                self.ghosts[i] = (new_x, new_y)
                self.board[new_x][new_y] = GHOST

    def play(self):
        while not self.game_over:
            self.print_board()
            direction = input("Move (w/a/s/d): ")
            self.move_pacman(direction)
            self.move_ghosts()
        self.print_board()
        print("Game Over! Your score was:", self.score)

if __name__ == "__main__":
    game = Game()
    game.play()