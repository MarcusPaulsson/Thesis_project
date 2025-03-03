import random
import time
import sys
import threading

class DinosaurRunner:
    def __init__(self):
        self.score = 0
        self.is_running = True
        self.obstacle_position = 50  # Starting position of the obstacle
        self.dino_position = 0  # Starting position of the Dino

    def jump(self):
        print("Dino jumped!")
        time.sleep(0.5)  # Simulating the jump duration
        print("Dino landed.")
    
    def generate_obstacle(self):
        # Randomly decide if an obstacle should appear
        if random.choice([True, False]):
            self.obstacle_position = 50
            print("An obstacle has appeared!")
        else:
            self.obstacle_position = -1  # No obstacle

    def move_dino(self):
        while self.is_running:
            if self.obstacle_position != -1:
                if self.dino_position >= self.obstacle_position:
                    print("Game Over! You hit an obstacle.")
                    self.is_running = False
                    break
            time.sleep(1)
            self.score += 1
            print(f"Score: {self.score}")

    def game_loop(self):
        while self.is_running:
            self.generate_obstacle()
            time.sleep(2)  # Generate new obstacles every 2 seconds

    def start_game(self):
        print("Starting Dinosaur Runner Game!")
        threading.Thread(target=self.move_dino).start()
        self.game_loop()

        while self.is_running:
            command = input("Press 'j' to jump or 'q' to quit: ").strip().lower()
            if command == 'j':
                self.jump()
            elif command == 'q':
                print("Quitting the game.")
                self.is_running = False
            else:
                print("Invalid command. Please press 'j' to jump or 'q' to quit.")
        
        print(f"Final Score: {self.score}")

if __name__ == "__main__":
    game = DinosaurRunner()
    game.start_game()