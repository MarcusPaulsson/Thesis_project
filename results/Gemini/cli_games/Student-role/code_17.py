import random
import time
import os

class DinosaurRunner:
    """
    A command-line Dinosaur Runner game.
    """

    def __init__(self, width=80, initial_speed=1):
        """
        Initializes the game.

        Args:
            width (int): The width of the game screen.
            initial_speed (float): The initial speed of the game (obstacles moving towards the dinosaur).
        """
        self.width = width
        self.dinosaur_position = 5  # Fixed position of the dinosaur from the left
        self.obstacle_position = width - 5  # Starting position of the obstacle from the right
        self.obstacle_height = random.choice([1, 2])  # 1 for low, 2 for high
        self.score = 0
        self.game_over = False
        self.speed = initial_speed
        self.ground = "_" * width
        self.dinosaur = "D"
        self.space = " "
        self.obstacle_char = "X"
        self.jump_height = 3
        self.is_jumping = False
        self.jump_counter = 0
        self.clear_screen = lambda: os.system('cls' if os.name == 'nt' else 'clear')

    def update(self):
        """
        Updates the game state.
        """
        if self.game_over:
            return

        # Move the obstacle
        self.obstacle_position -= self.speed
        if self.obstacle_position < 0:
            self.obstacle_position = self.width - 1
            self.obstacle_height = random.choice([1, 2])
            self.score += 1
            self.speed += 0.01  # Increase speed gradually


        # Handle jumping
        if self.is_jumping:
            self.jump_counter += 1
            if self.jump_counter > self.jump_height:
                self.is_jumping = False
                self.jump_counter = 0

        # Check for collision
        if self.obstacle_position <= self.dinosaur_position + 1 and self.obstacle_position >= self.dinosaur_position -1:
            if not self.is_jumping and self.obstacle_height == 2:
                self.game_over = True
            if self.is_jumping and self.obstacle_height == 1:
                self.game_over = True


    def render(self):
        """
        Renders the game screen.
        """
        self.clear_screen()
        screen = list(self.ground)

        # Draw the dinosaur
        dinosaur_height = self.jump_counter if self.is_jumping else 0
        dinosaur_row = len(self.ground.splitlines()) - 1 - dinosaur_height
        screen[self.dinosaur_position] = self.dinosaur

        # Draw the obstacle
        obstacle_row = len(self.ground.splitlines()) - 1
        if self.obstacle_height == 2:  # High obstacle, need to skip a row
            obstacle_row -= 1
        screen[int(self.obstacle_position)] = self.obstacle_char

        # Print the screen
        print("".join(screen))
        print(f"Score: {self.score}")

        if self.game_over:
            print("Game Over!")

    def jump(self):
        """
        Initiates a jump if the dinosaur is not already jumping.
        """
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_counter = 0

    def play(self):
        """
        Starts the game loop.
        """
        while not self.game_over:
            start_time = time.time()
            self.update()
            self.render()

            # Control the game speed (frame rate)
            elapsed_time = time.time() - start_time
            sleep_time = max(0, 0.1 - elapsed_time)  # Target frame rate: 10 FPS
            time.sleep(sleep_time)

        input("Press Enter to exit.") # Keep the game over screen until Enter is pressed


if __name__ == '__main__':
    game = DinosaurRunner()

    # Simple input handling for jumping (press 'j' to jump)
    import threading
    import sys

    def input_thread(game):
        while not game.game_over:
            user_input = input()
            if user_input.lower() == 'j':
                game.jump()
            elif user_input.lower() == 'q':
                game.game_over = True # Quit the game
                break

    input_thread = threading.Thread(target=input_thread, args=(game,), daemon=True) # Daemonize to exit with main thread
    input_thread.start()

    game.play()