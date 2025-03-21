import random
import time
import os
import sys

class DinosaurRunner:
    def __init__(self):
        self.score = 0
        self.is_running = True
        self.obstacle_distance = 50
        self.obstacles = ['Cactus', 'Bird']
        self.obstacle = None

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def generate_obstacle(self):
        self.obstacle = random.choice(self.obstacles)
        self.obstacle_distance = 50

    def jump(self):
        if self.obstacle_distance <= 10:
            if self.obstacle == 'Cactus':
                print("Jumped over the Cactus!")
                self.score += 1
            elif self.obstacle == 'Bird':
                print("Jumped over the Bird!")
                self.score += 1
            self.obstacle = None
            self.obstacle_distance = 50

    def run(self):
        print("Welcome to Dinosaur Runner!")
        print("Press 'j' to jump. Type 'exit' to quit.")
        while self.is_running:
            if self.obstacle is None:
                self.generate_obstacle()
            self.obstacle_distance -= 1
            print(f"Obstacle: {self.obstacle} | Distance: {self.obstacle_distance} | Score: {self.score}")
            user_input = input("Your action: ").strip().lower()

            if user_input == 'exit':
                self.is_running = False
                print("Thanks for playing! Your final score is:", self.score)
                break
            elif user_input == 'j':
                self.jump()
            else:
                print("Invalid input. Press 'j' to jump or 'exit' to quit.")

            if self.obstacle_distance <= 0:
                print(f"Game Over! You hit the {self.obstacle}. Final score: {self.score}")
                self.is_running = False

            time.sleep(1)
            self.clear_screen()

if __name__ == "__main__":
    game = DinosaurRunner()
    game.run()