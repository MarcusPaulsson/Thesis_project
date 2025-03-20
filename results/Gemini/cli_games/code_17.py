import random
import time
import os

class DinosaurRunner:
    """
    A command-line implementation of the Dinosaur Runner game.
    """

    def __init__(self, width=80, initial_speed=1, speed_increment=0.1, obstacle_density=0.05, jump_height=5):
        """
        Initializes the game.

        Args:
            width (int): The width of the game screen.
            initial_speed (float): The initial speed of the game.
            speed_increment (float): The amount the speed increases each frame.
            obstacle_density (float): The probability of an obstacle appearing on a given line.
            jump_height (int): The maximum height of the dinosaur's jump.
        """
        self.width = width
        self.dinosaur_position = 5  # Vertical position of the dinosaur (0 is the ground)
        self.dinosaur_velocity = 0  # Vertical velocity of the dinosaur
        self.gravity = -1  # Simulates gravity
        self.initial_speed = initial_speed
        self.speed = initial_speed
        self.speed_increment = speed_increment
        self.obstacle_density = obstacle_density
        self.jump_height = jump_height
        self.obstacles = []  # List of obstacle positions (x-coordinates)
        self.score = 0
        self.game_over = False
        self.frame_delay = 0.1  # Initial delay between frames

    def clear_screen(self):
      """Clears the terminal screen."""
      os.system('cls' if os.name == 'nt' else 'clear')


    def generate_obstacle(self):
        """
        Generates a new obstacle at the right edge of the screen with a probability
        determined by the obstacle density.
        """
        if random.random() < self.obstacle_density:
            self.obstacles.append(self.width - 1)  # Add obstacle at the right edge

    def update_obstacles(self):
        """
        Updates the position of the obstacles, removing those that have moved off-screen.
        """
        new_obstacles = []
        for obstacle in self.obstacles:
            obstacle -= self.speed  # Move obstacle to the left
            if obstacle >= 0:
                new_obstacles.append(obstacle)
        self.obstacles = new_obstacles

    def update_dinosaur(self):
        """
        Updates the dinosaur's position based on its velocity and gravity.
        """
        self.dinosaur_position += self.dinosaur_velocity
        self.dinosaur_velocity += self.gravity

        # Keep the dinosaur within the ground limits
        if self.dinosaur_position < 0:
            self.dinosaur_position = 0
            self.dinosaur_velocity = 0  # Stop downward movement on the ground

    def check_collision(self):
        """
        Checks for a collision between the dinosaur and any obstacles.
        """
        for obstacle in self.obstacles:
            if (obstacle < 10 and obstacle > 3) and self.dinosaur_position < 2: # Collision detection range
                return True
        return False

    def jump(self):
        """
        Initiates a jump if the dinosaur is on the ground.
        """
        if self.dinosaur_position == 0:  # Only jump if on the ground
            self.dinosaur_velocity = self.jump_height

    def draw_screen(self):
        """
        Draws the current state of the game on the screen.
        """
        self.clear_screen()  # Clear the previous frame
        screen = [" " for _ in range(self.width * 6)] # 6 represents height of the screen

        # Draw the ground
        for i in range(self.width):
            screen[i] = "_"

        # Draw the dinosaur
        dinosaur_height = 2
        dinosaur_width = 3
        dinosaur_start_index = (self.dinosaur_position + 1) * self.width + 3

        if self.dinosaur_position <1: #standing dinosaur
            dino =  """
            O
           /|\\
           / \\
           """
        else:
            dino =  """
            O
           /|\\
           / \\
           """

        dino_lines = dino.splitlines()

        for i, line in enumerate(dino_lines):
          if line:
            for j, char in enumerate(line):
              screen[dinosaur_start_index - (len(dino_lines) -1 -i) * self.width + j] = char



        # Draw the obstacles
        obstacle_height = 2
        obstacle_width = 2
        for obstacle_x in self.obstacles:
            for i in range(obstacle_height):
                for j in range(obstacle_width):
                  if (obstacle_x + j) < self.width:
                    screen[(i) * self.width + int(obstacle_x +j)] = "#"

        # Print the screen
        for i in range(6): #Screen Height
            print("".join(screen[i*self.width:(i+1)*self.width]))

        # Print score
        print(f"Score: {self.score}")

    def update_score(self):
      """Updates the score based on the distance traveled."""
      self.score += self.speed # the faster we go, the faster we score

    def run(self):
        """
        Runs the main game loop.
        """
        while not self.game_over:
            # Get user input
            user_input = input("Press 'j' to jump, or any other key to continue (or 'q' to quit): ").lower()
            if user_input == 'j':
                self.jump()
            elif user_input == 'q':
                break

            # Update game state
            self.generate_obstacle()
            self.update_obstacles()
            self.update_dinosaur()
            self.update_score()

            if self.check_collision():
                self.game_over = True

            self.draw_screen()

            # Increase speed
            self.speed += self.speed_increment
            self.frame_delay = max(0.02, 0.1 - (self.speed * 0.005)) #Adjust frame delay to increase speed smoothly

            time.sleep(self.frame_delay)

        if self.game_over:
            print("Game Over!")
            print(f"Final Score: {self.score}")
        else:
            print("Game quit.")
            print(f"Final Score: {self.score}")

if __name__ == "__main__":
    game = DinosaurRunner()
    game.run()