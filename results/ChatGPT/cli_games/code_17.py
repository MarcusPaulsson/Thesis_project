import random
import os
import time
import sys

class DinosaurRunner:
    def __init__(self):
        self.dino_position = 0
        self.obstacle_position = 50
        self.score = 0
        self.game_over = False

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw_game(self):
        self.clear_screen()
        print("Score:", self.score)
        print(" " * self.dino_position + "D")
        print(" " * self.obstacle_position + "X")
        print("\nPress 'j' to jump, 'q' to quit.")

    def jump(self):
        if self.dino_position == 0:
            self.dino_position = 1
            print("Jumping!")
            time.sleep(0.5)  # Simulate jump duration
            self.dino_position = 0

    def update_game(self):
        self.obstacle_position -= 1
        if self.obstacle_position < 0:
            self.obstacle_position = 50
            self.score += 1
            if random.random() < 0.2:  # 20% chance for a new obstacle
                self.obstacle_position = 50

    def check_collision(self):
        if self.dino_position == 0 and self.obstacle_position == 0:
            self.game_over = True

    def run(self):
        print("Welcome to Dinosaur Runner!")
        print("Avoid the obstacles by jumping!\n")

        while not self.game_over:
            self.draw_game()
            self.update_game()
            self.check_collision()

            if self.game_over:
                break

            user_input = input("Action: ")
            if user_input.lower() == 'j':
                self.jump()
            elif user_input.lower() == 'q':
                print("Quitting the game.")
                break
            else:
                print("Invalid input! Use 'j' to jump or 'q' to quit.")

        print("Game Over! Your score is:", self.score)

if __name__ == "__main__":
    game = DinosaurRunner()
    game.run()