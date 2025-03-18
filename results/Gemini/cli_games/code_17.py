import time
import random
import os

class DinosaurRunner:
    def __init__(self):
        self.dino_position = 0
        self.obstacle_position = 20
        self.score = 0
        self.game_over = False
        self.obstacle_type = self.choose_obstacle() # 0: cactus, 1: bird
        self.jump_height = 3

    def choose_obstacle(self):
        return random.randint(0, 1)

    def generate_obstacle(self):
       if self.obstacle_type == 0:
            return "🌵"
       else:
            return "🐦"

    def print_screen(self):
        """Prints the game screen."""
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        screen = ""

        # Ground
        ground = "_" * 40 + "\n"
        screen += ground

        # Dino
        dino = "🦖"
        dino_position_str = " " * self.dino_position + dino

        # Obstacle
        obstacle = self.generate_obstacle()
        obstacle_position_str = " " * self.obstacle_position + obstacle

        # Combine dino and obstacle, handling potential overlap
        if self.dino_position < self.obstacle_position:
          screen += dino_position_str + obstacle_position_str[len(dino_position_str):] + "\n"
        else:
          screen += obstacle_position_str + dino_position_str[len(obstacle_position_str):] + "\n"


        screen += ground
        screen += f"Score: {self.score}\n"
        print(screen)


    def update(self, action):
        """Updates the game state based on the player's action."""

        # Handle jumping
        if action == "jump":
            self.dino_position = self.jump_height  # Dino jumps
        else:
            self.dino_position = 0 # Dino on the ground


        # Move the obstacle
        self.obstacle_position -= 1

        # Check for collision
        if self.dino_position == 0 and self.obstacle_position <= 1:
            self.game_over = True
            return

        # Generate new obstacle
        if self.obstacle_position < 0:
            self.obstacle_position = 39
            self.score += 1
            self.obstacle_type = self.choose_obstacle()

    def play(self):
        """Main game loop."""
        while not self.game_over:
            self.print_screen()
            action = input("Type 'jump' to jump, or press Enter to continue: ").lower()
            self.update(action)
            time.sleep(0.1)

        print("Game Over!")
        print(f"Final Score: {self.score}")


if __name__ == "__main__":
    game = DinosaurRunner()
    game.play()