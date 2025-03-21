import random
import os
import sys
import time

class PacMan:
    def __init__(self):
        self.board = [[' ' for _ in range(10)] for _ in range(10)]
        self.pacman_pos = [1, 1]
        self.food_positions = []
        self.score = 0
        self.is_running = True
        self.generate_food(10)

    def generate_food(self, num_food):
        while len(self.food_positions) < num_food:
            pos = [random.randint(0, 9), random.randint(0, 9)]
            if pos != self.pacman_pos and pos not in self.food_positions:
                self.food_positions.append(pos)

    def draw_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in range(10):
            for col in range(10):
                if [row, col] == self.pacman_pos:
                    print('P', end=' ')
                elif [row, col] in self.food_positions:
                    print('.', end=' ')
                else:
                    print(' ', end=' ')
            print()
        print(f"Score: {self.score}")

    def move(self, direction):
        if direction == 'w' and self.pacman_pos[0] > 0:
            self.pacman_pos[0] -= 1
        elif direction == 's' and self.pacman_pos[0] < 9:
            self.pacman_pos[0] += 1
        elif direction == 'a' and self.pacman_pos[1] > 0:
            self.pacman_pos[1] -= 1
        elif direction == 'd' and self.pacman_pos[1] < 9:
            self.pacman_pos[1] += 1

        self.check_food()

    def check_food(self):
        if self.pacman_pos in self.food_positions:
            self.food_positions.remove(self.pacman_pos)
            self.score += 1
            if not self.food_positions:
                self.is_running = False

    def play(self):
        print("Use W (up), A (left), S (down), D (right) to move. Press Q to quit.")
        while self.is_running:
            self.draw_board()
            move = input("Enter move: ").lower()
            if move in ['w', 'a', 's', 'd']:
                self.move(move)
            elif move == 'q':
                self.is_running = False
            else:
                print("Invalid move. Use W, A, S, D or Q to quit.")

        print("Game Over! Final Score: ", self.score)

if __name__ == '__main__':
    game = PacMan()
    game.play()