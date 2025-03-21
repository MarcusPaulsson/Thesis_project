import random
import time
import os

class DinosaurRunner:
    """
    A command-line Dinosaur Runner game.
    """

    def __init__(self, width=60, initial_speed=1, speed_increment=0.2, obstacle_density=0.1):
        """
        Initializes the game.

        Args:
            width (int): The width of the game screen.
            initial_speed (float): The initial speed of the game.
            speed_increment (float): The amount the speed increases each round.
            obstacle_density (float): The probability of an obstacle appearing in a column.
        """
        self.width = width
        self.dinosaur_position = 5  # Fixed dinosaur position
        self.obstacles = []
        self.score = 0
        self.speed = initial_speed
        self.initial_speed = initial_speed
        self.speed_increment = speed_increment
        self.obstacle_density = obstacle_density
        self.game_over = False

    def reset(self):
        """Resets the game to the initial state."""
        self.obstacles = []
        self.score = 0
        self.speed = self.initial_speed
        self.game_over = False

    def generate_obstacle(self):
        """Generates a new obstacle at the right edge of the screen."""
        if random.random() < self.obstacle_density:
            self.obstacles.append(self.width - 1)  # Obstacle starts at the right edge

    def move_obstacles(self):
        """Moves existing obstacles one step to the left."""
        self.obstacles = [obstacle - 1 for obstacle in self.obstacles if obstacle > 0]

    def check_collision(self):
        """Checks if the dinosaur has collided with an obstacle."""
        for obstacle in self.obstacles:
            if obstacle == self.dinosaur_position:
                return True
        return False

    def update_game(self):
        """Updates the game state."""
        self.generate_obstacle()
        self.move_obstacles()
        if self.check_collision():
            self.game_over = True
        else:
            self.score += 1
            self.speed += self.speed_increment

    def render(self):
        """Renders the game screen."""
        screen = [' '] * self.width
        screen[self.dinosaur_position] = 'D'  # Dinosaur

        for obstacle in self.obstacles:
            screen[obstacle] = '#'  # Obstacle

        print(''.join(screen))
        print(f"Score: {self.score}")

    def play(self):
        """Plays the game."""
        while not self.game_over:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
            self.render()
            self.update_game()
            time.sleep(0.1 / self.speed)

        print("Game Over!")
        print(f"Final Score: {self.score}")

def main():
    """Main function to start the game."""
    game = DinosaurRunner()
    while True:
        game.play()
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != 'y':
            break
        game.reset()

if __name__ == "__main__":
    main()