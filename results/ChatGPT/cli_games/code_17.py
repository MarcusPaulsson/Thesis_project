import random
import time
import os
import sys

class DinosaurRunner:
    def __init__(self):
        self.score = 0
        self.game_over = False
        self.obstacles = ['-', '!', 'O']  # Different obstacles
        self.player_pos = 0

    def print_game_state(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Dinosaur Runner")
        print("Score:", self.score)
        print("Press 'x' to jump, 'q' to quit.")
        print(" " * self.player_pos + "D")
        print("\n" + self.generate_obstacles())

    def generate_obstacles(self):
        return ''.join(random.choice(self.obstacles) for _ in range(20))

    def jump(self):
        if not self.game_over:
            self.score += 1
            print("Jumped over an obstacle!")
            time.sleep(0.5)

    def check_collision(self, obstacles):
        if obstacles[self.player_pos] in self.obstacles:
            self.game_over = True
            print("Game Over! You hit an obstacle.")

    def play(self):
        while not self.game_over:
            self.print_game_state()
            obstacles = self.generate_obstacles()
            self.check_collision(obstacles)
            if self.game_over:
                break
            action = input("Action: ")
            if action == 'x':
                self.jump()
            elif action == 'q':
                print("Thanks for playing!")
                sys.exit()
            else:
                print("Invalid action. Press 'x' to jump or 'q' to quit.")

        print("Final Score:", self.score)

if __name__ == "__main__":
    game = DinosaurRunner()
    game.play()