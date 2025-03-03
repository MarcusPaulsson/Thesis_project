import random
import os
import time

class Game:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.pacman_pos = [1, 1]
        self.food_positions = [[random.randint(0, self.height - 1), random.randint(0, self.width - 1)] for _ in range(5)]
        self.score = 0
        self.game_over = False
        self.directions = {
            'w': [-1, 0],
            's': [1, 0],
            'a': [0, -1],
            'd': [0, 1]
        }

    def draw_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for r in range(self.height):
            for c in range(self.width):
                if [r, c] == self.pacman_pos:
                    print("P", end=" ")
                elif [r, c] in self.food_positions:
                    print("F", end=" ")
                else:
                    print(".", end=" ")
            print()
        print(f"Score: {self.score}")

    def move_pacman(self, direction):
        if direction in self.directions:
            new_pos = [
                self.pacman_pos[0] + self.directions[direction][0],
                self.pacman_pos[1] + self.directions[direction][1]
            ]
            if 0 <= new_pos[0] < self.height and 0 <= new_pos[1] < self.width:
                self.pacman_pos = new_pos
                self.check_food_collision()

    def check_food_collision(self):
        if self.pacman_pos in self.food_positions:
            self.food_positions.remove(self.pacman_pos)
            self.score += 1
            if not self.food_positions:
                self.game_over = True

    def play(self):
        while not self.game_over:
            self.draw_board()
            move = input("Enter move (w/a/s/d): ").strip().lower()
            self.move_pacman(move)
            time.sleep(0.1)
        print("Game Over! Your final score is:", self.score)

if __name__ == "__main__":
    game = Game()
    game.play()