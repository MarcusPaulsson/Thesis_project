import random
import time
import os

class DinosaurRunner:
    def __init__(self, width=80, height=15):
        self.width = width
        self.height = height
        self.dino = 2  # Dino's vertical position
        self.cactus_position = self.width - 5  # Cactus initial position
        self.score = 0
        self.game_over = False
        self.cactus_speed = 1  # Cactus movement speed
        self.jump_height = 4
        self.is_jumping = False
        self.jump_peak = 0
        self.jump_direction = 1 # 1 for up, -1 for down

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw_screen(self):
        """Draws the game screen in the console."""
        screen = [[' ' for _ in range(self.width)] for _ in range(self.height)]

        # Draw ground
        for i in range(self.width):
            screen[self.height - 1][i] = '_'

        # Draw dino
        if self.is_jumping:
            dino_height = self.dino - (self.jump_peak - abs(self.jump_peak - self.jump_height))
            screen[int(dino_height)][2] = 'D'
        else:
            screen[self.dino][2] = 'D'

        # Draw cactus
        screen[self.height - 2][self.cactus_position] = '#'
        screen[self.height - 3][self.cactus_position] = '#'

        # Print the screen
        self.clear_screen()
        for row in screen:
            print(''.join(row))

        print(f"Score: {self.score}")

    def update_game(self):
        """Updates the game state - moves cactus, checks for collisions, etc."""

        # Move cactus
        self.cactus_position -= self.cactus_speed
        if self.cactus_position < 0:
            self.cactus_position = self.width - 1
            self.score += 1
            self.cactus_speed = min(1 + self.score // 10, 5)  # Increase speed

        # Jumping logic
        if self.is_jumping:
            self.jump_peak += self.jump_direction
            if self.jump_peak == self.jump_height :
                self.jump_direction = -1
            elif self.jump_peak == 0:
                self.is_jumping = False
                self.jump_direction = 1

        # Collision detection (simplified)
        if 1 <= self.cactus_position <= 3:
            if not self.is_jumping:
                self.game_over = True
                print("Game Over!")

    def handle_input(self, input_char):
        """Handles user input.  'j' for jump."""
        if input_char == 'j' and not self.is_jumping:
            self.is_jumping = True
            self.jump_peak = 0
            self.jump_direction = 1 # Start going up

    def play(self):
        """Main game loop."""
        while not self.game_over:
            self.draw_screen()
            self.update_game()

            # Get input (non-blocking)
            input_char = None
            try:
                import termios, sys, tty
                def getch():
                    fd = sys.stdin.fileno()
                    old_settings = termios.tcgetattr(fd)
                    try:
                        tty.setraw(sys.stdin.fileno())
                        ch = sys.stdin.read(1)
                    finally:
                        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                    return ch
                input_char = getch()
            except ImportError: # For Windows (no termios)
                import msvcrt
                if msvcrt.kbhit():
                    input_char = msvcrt.getch().decode('utf-8')

            if input_char:
                self.handle_input(input_char)

            time.sleep(0.1)  # Adjust for desired game speed

        print(f"Final Score: {self.score}")
        input("Press Enter to exit.")


if __name__ == '__main__':
    game = DinosaurRunner()
    game.play()