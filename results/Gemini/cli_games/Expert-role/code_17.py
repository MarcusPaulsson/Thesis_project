import random
import time
import os

class DinosaurRunner:
    """
    A command-line implementation of the Dinosaur Runner game.
    """

    def __init__(self, width=60, initial_speed=1):
        """
        Initializes the game.

        Args:
            width (int): The width of the game screen.
            initial_speed (float): The initial speed of the game.
        """
        self.width = width
        self.initial_speed = initial_speed
        self.speed = initial_speed
        self.dino_position = 5
        self.obstacle_position = width - 5
        self.obstacle_height = 1
        self.score = 0
        self.game_over = False
        self.last_obstacle_time = time.time()
        self.obstacle_interval = 2  # Initial obstacle generation interval (seconds)
        self.level = 1

    def clear_screen(self):
        """
        Clears the console screen. Works cross-platform.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def generate_obstacle(self):
        """
        Generates a new obstacle.  Obstacle height is randomly 1 or 2.
        """
        self.obstacle_position = self.width - 5
        self.obstacle_height = random.choice([1, 2])  # Introduce varying obstacle height
        self.last_obstacle_time = time.time()

    def update(self):
        """
        Updates the game state.
        """
        if self.game_over:
            return

        # Move the obstacle
        self.obstacle_position -= self.speed
        if self.obstacle_position < 0:
            self.generate_obstacle()
            self.score += 1
            self.obstacle_interval = max(0.5, self.obstacle_interval - 0.01) #difficulty increase

        # Check for collision
        if self.dino_position < self.obstacle_position < self.dino_position + 3:
            if self.obstacle_height == 2 and self.dino_position < 3:
                self.game_over = True
            elif self.obstacle_height == 1:
                self.game_over = True

        # Increase speed gradually
        self.speed = self.initial_speed + (self.score / 20)
        # Update level
        self.level = int(self.score / 5) + 1

    def render(self):
        """
        Renders the game screen.
        """
        screen = [' '] * self.width
        # Draw dinosaur
        screen[self.dino_position] = 'D'
        screen[self.dino_position + 1] = 'i'
        screen[self.dino_position + 2] = 'n'

        # Draw obstacle
        if self.obstacle_position < self.width:
            if self.obstacle_height == 1:
                screen[int(self.obstacle_position)] = '#'
            else:  # obstacle_height == 2
                screen[int(self.obstacle_position)] = 'H'
                if int(self.obstacle_position) + 1 < self.width:
                    screen[int(self.obstacle_position) + 1] = 'H'

        # Display score and level
        score_display = f"Score: {self.score}  Level: {self.level}"
        screen_str = ''.join(screen)
        print(f"{score_display:^{self.width}}")  # Center-align score
        print("-" * self.width)
        print(screen_str)
        print("-" * self.width)

        if self.game_over:
            print("Game Over!")


    def jump(self):
        """
        Makes the dinosaur jump (moves it up).
        """
        if self.dino_position == 5:
            self.dino_position = 2

    def duck(self):
        """
        Makes the dinosaur duck (moves it down).
        """
        if self.dino_position == 2:
            self.dino_position = 5

    def run(self):
        """
        Runs the main game loop.
        """
        while not self.game_over:
            start_time = time.time()

            # Get user input (non-blocking)
            # This part is difficult in pure command-line Python without external libraries.
            # For simplicity, we'll skip real-time input and rely on a fixed update rate.

            self.update()
            self.clear_screen()
            self.render()

            # Control game speed
            elapsed_time = time.time() - start_time
            sleep_time = max(0, 0.1 - elapsed_time)  # Target update rate: 10 FPS
            time.sleep(sleep_time)

        print("Final Score:", self.score)


if __name__ == "__main__":
    game = DinosaurRunner()

    # Simple input handling (replace with proper input if possible)
    print("Dinosaur Runner - Command Line Edition")
    print("Press Enter to jump, any other key to duck.  Ctrl+C to quit.")

    import threading

    def input_thread(game_instance):
        """Handles user input in a separate thread."""
        while not game_instance.game_over:
            try:
                user_input = input()  # This blocks, hence the thread
                if user_input == "":
                    game_instance.jump()
                    time.sleep(0.2)
                    game_instance.duck() #duck after jump
                else:
                    game_instance.duck()
                    time.sleep(0.2)
                    game_instance.jump()#jump after duck
            except EOFError:  # Handle Ctrl+C gracefully
                game_instance.game_over = True
                break
            except KeyboardInterrupt:
                game_instance.game_over = True
                break


    input_thread_obj = threading.Thread(target=input_thread, args=(game,))
    input_thread_obj.daemon = True  # Allow the main thread to exit
    input_thread_obj.start()

    game.run()