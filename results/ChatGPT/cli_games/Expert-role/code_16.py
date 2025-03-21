import random
import os
import time

class PacManGame:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.pacman_pos = [1, 1]
        self.food_positions = self.generate_food(5)
        self.score = 0
        self.is_running = True
        self.directions = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}

    def generate_food(self, count):
        food_positions = []
        while len(food_positions) < count:
            pos = [random.randint(0, self.height - 1), random.randint(0, self.width - 1)]
            if pos not in food_positions and pos != self.pacman_pos:
                food_positions.append(pos)
        return food_positions

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(self.height):
            for j in range(self.width):
                if [i, j] == self.pacman_pos:
                    print("P", end=' ')
                elif [i, j] in self.food_positions:
                    print("F", end=' ')
                else:
                    print(".", end=' ')
            print()
        print(f"Score: {self.score}")

    def move(self, direction):
        if direction in self.directions:
            new_pos = [
                self.pacman_pos[0] + self.directions[direction][0],
                self.pacman_pos[1] + self.directions[direction][1]
            ]
            if 0 <= new_pos[0] < self.height and 0 <= new_pos[1] < self.width:
                self.pacman_pos = new_pos
                self.check_food()

    def check_food(self):
        if self.pacman_pos in self.food_positions:
            self.food_positions.remove(self.pacman_pos)
            self.score += 1           

    def run(self):
        while self.is_running:
            self.display()
            move = input("Move (w/a/s/d) or 'q' to quit: ")
            if move == 'q':
                self.is_running = False
            else:
                self.move(move)

if __name__ == "__main__":
    game = PacManGame()
    game.run()