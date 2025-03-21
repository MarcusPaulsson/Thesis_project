import random
import time
import os

class DinosaurRunner:
    """
    Implementation of the Dinosaur Runner game in a command line interface.
    """

    def __init__(self, width=80, height=10):
        """
        Initializes the game.

        Args:
            width (int): The width of the game screen.
            height (int): The height of the game screen.
        """
        self.width = width
        self.height = height
        self.dino_position = self.height - 2  # Dino starts near the bottom
        self.obstacle_position = self.width - 5 # Obstacle starts far right
        self.obstacle_height = 1 # Obstacle height
        self.score = 0
        self.game_over = False
        self.ground = ["="] * self.width
        self.dino = ["^", "|", "\\", "|"] # Dino representation (simplified)
        self.obstacle = ["#"]  # Obstacle representation (simplified)
        self.obstacle_speed = 1 # Obstacle speed
        self.jump_height = 3 # Height of the dino jump
        self.is_jumping = False # Flag to indicate if the Dino is jumping
        self.jump_counter = 0  # Counter for the jump duration
        self.difficulty = 1  # Game difficulty multiplier
        self.high_score = 0 # Store the current high score

        self.load_high_score()

    def load_high_score(self):
        """Loads the high score from a file."""
        try:
            with open("highscore.txt", "r") as f:
                self.high_score = int(f.read())
        except FileNotFoundError:
            self.high_score = 0
        except ValueError:
            self.high_score = 0 # Handle cases where the file is corrupted

    def save_high_score(self):
        """Saves the high score to a file."""
        with open("highscore.txt", "w") as f:
            f.write(str(self.high_score))

    def clear_screen(self):
        """Clears the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def generate_obstacle(self):
        """Generates a new obstacle."""
        self.obstacle_position = self.width - 5
        self.obstacle_height = random.randint(1, 2) # Vary obstacle height

    def update(self):
        """Updates the game state."""
        if self.game_over:
            return

        # Update obstacle position
        self.obstacle_position -= self.obstacle_speed * self.difficulty

        # Generate new obstacle if it goes off screen
        if self.obstacle_position < 0:
            self.generate_obstacle()
            self.score += 1

        # Update jump
        if self.is_jumping:
            self.jump_counter += 1
            if self.jump_counter <= self.jump_height:  # Ascending
                self.dino_position -= 1
            else:  # Descending
                self.dino_position += 1
            if self.dino_position >= self.height - 2:  # Back on the ground
                self.dino_position = self.height - 2
                self.is_jumping = False
                self.jump_counter = 0

        # Collision detection (simplified)
        if (self.obstacle_position < 4 and self.obstacle_position > 0 and
            self.dino_position >= self.height - 1 - self.obstacle_height):
            self.game_over = True
            if self.score > self.high_score:
                self.high_score = self.score
                self.save_high_score()

        # Increase difficulty over time
        if self.score > 0 and self.score % 10 == 0:
            self.difficulty += 0.1

    def draw(self):
        """Draws the game on the screen."""
        self.clear_screen()

        screen = [[" "] * self.width for _ in range(self.height)]

        # Draw ground
        for i in range(self.width):
            screen[self.height - 1][i] = "="

        # Draw Dino
        for i, part in enumerate(self.dino):
            if self.dino_position + i < self.height: # Avoid drawing outside screen
                screen[self.dino_position + i][2] = part

        # Draw obstacle
        for i in range(self.obstacle_height):
             screen[self.height - 1 - i][self.obstacle_position] = "#"

        # Print the screen
        for row in screen:
            print("".join(row))

        # Print score and instructions
        print(f"Score: {self.score:.0f}  High Score: {self.high_score}")
        print("Press 'space' to jump. Press 'q' to quit.")


    def handle_input(self, key):
        """Handles user input."""
        if key == " ":
            if not self.is_jumping:
                self.is_jumping = True
        elif key == "q":
            self.game_over = True

    def play(self):
        """Runs the main game loop."""
        self.generate_obstacle()

        while not self.game_over:
            start_time = time.time()
            self.draw()
            time.sleep(0.05)

            # Get user input (non-blocking)
            key = None
            try:
                import termios, sys, tty
                fd = sys.stdin.fileno()
                old_settings = termios.tcgetattr(fd)
                try:
                    tty.setcbreak(sys.stdin.fileno())
                    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:  # Check if input is available
                        key = sys.stdin.read(1)
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            except ImportError:
                # Fallback for Windows (requires installation of 'msvcrt')
                import msvcrt
                if msvcrt.kbhit():
                    key = msvcrt.getch().decode("utf-8")
            except Exception as e:
                print(f"Error getting input: {e}")
                key = None

            if key:
                self.handle_input(key)

            self.update()

            elapsed_time = time.time() - start_time
            delay = max(0.01, 0.05 - elapsed_time) # Adjust delay to maintain consistent speed
            time.sleep(delay)

        self.draw() # Final draw before game over
        print("Game Over!")
        print(f"Final Score: {self.score:.0f}")



if __name__ == "__main__":
    import select

    game = DinosaurRunner()
    game.play()