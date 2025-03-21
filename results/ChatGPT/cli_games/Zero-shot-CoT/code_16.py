import random
import os
import time

class PacMan:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.pacman_position = [0, 0]
        self.ghost_position = [random.randint(0, height-1), random.randint(0, width-1)]
        self.dots = [[random.randint(0, height-1), random.randint(0, width-1)] for _ in range(5)]
        self.score = 0
        self.game_over = False

    def draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(self.height):
            for x in range(self.width):
                if [y, x] == self.pacman_position:
                    print('P', end=' ')
                elif [y, x] == self.ghost_position:
                    print('G', end=' ')
                elif [y, x] in self.dots:
                    print('.', end=' ')
                else:
                    print(' ', end=' ')
            print()
        print(f'Score: {self.score}')

    def move_pacman(self, direction):
        if direction == 'w' and self.pacman_position[0] > 0:
            self.pacman_position[0] -= 1
        elif direction == 's' and self.pacman_position[0] < self.height - 1:
            self.pacman_position[0] += 1
        elif direction == 'a' and self.pacman_position[1] > 0:
            self.pacman_position[1] -= 1
        elif direction == 'd' and self.pacman_position[1] < self.width - 1:
            self.pacman_position[1] += 1

        self.check_collision()

    def check_collision(self):
        if self.pacman_position == self.ghost_position:
            self.game_over = True
            print("Game Over! You were caught by the ghost.")
        elif self.pacman_position in self.dots:
            self.score += 1
            self.dots.remove(self.pacman_position)

    def move_ghost(self):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        move = random.choice(directions)
        new_ghost_position = [self.ghost_position[0] + move[0], self.ghost_position[1] + move[1]]
        if 0 <= new_ghost_position[0] < self.height and 0 <= new_ghost_position[1] < self.width:
            self.ghost_position = new_ghost_position

    def play(self):
        while not self.game_over:
            self.draw()
            direction = input("Move (w/a/s/d): ")
            self.move_pacman(direction)
            self.move_ghost()
            time.sleep(0.5)
        self.draw()

if __name__ == "__main__":
    game = PacMan()
    game.play()