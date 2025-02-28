import random
import time
import os

class DinosaurRunner:
    def __init__(self):
        self.score = 0
        self.is_running = True

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_score(self):
        print(f"Score: {self.score}")

    def jump(self):
        print("Jumping!")
        time.sleep(0.5)

    def game_over(self):
        self.clear_screen()
        print("Game Over!")
        print(f"Final Score: {self.score}")
        self.is_running = False

    def check_obstacle(self):
        # Randomly determine if an obstacle appears
        return random.choice([True, False])

    def play(self):
        while self.is_running:
            self.clear_screen()
            self.display_score()
            print("Press 'j' to jump or 'q' to quit.")
            user_input = input("Your action: ")

            if user_input.lower() == 'j':
                if self.check_obstacle():
                    print("You jumped over an obstacle!")
                    self.score += 1
                else:
                    print("No obstacle to jump over.")
                time.sleep(1)
            elif user_input.lower() == 'q':
                self.is_running = False
            else:
                print("Invalid action! Please press 'j' to jump or 'q' to quit.")
                time.sleep(1)

            if self.check_obstacle() and random.random() < 0.1:  # 10% chance of hitting an obstacle
                self.game_over()

if __name__ == "__main__":
    game = DinosaurRunner()
    game.play()