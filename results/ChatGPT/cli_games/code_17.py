import time
import random

class DinosaurRunner:
    def __init__(self):
        self.score = 0
        self.is_running = True

    def start_game(self):
        print("Welcome to Dinosaur Runner!")
        print("Press 'J' to jump over obstacles!")
        print("Press 'Q' to quit the game.")
        
        while self.is_running:
            time.sleep(1)  # Simulate time between obstacles
            obstacle_distance = random.randint(1, 5)
            print("\nAn obstacle is approaching! Distance:", obstacle_distance)
            
            user_input = input("Your move (J to jump, Q to quit): ").strip().upper()
            
            if user_input == 'J':
                if obstacle_distance <= 3:
                    print("You jumped and avoided the obstacle!")
                    self.score += 1
                else:
                    print("You jumped too early and hit the obstacle! Game Over.")
                    self.is_running = False
            elif user_input == 'Q':
                print("You quit the game. Final Score:", self.score)
                self.is_running = False
            else:
                print("Invalid input. Please press 'J' to jump or 'Q' to quit.")

        print("Game Over! Your final score is:", self.score)

if __name__ == "__main__":
    game = DinosaurRunner()
    game.start_game()