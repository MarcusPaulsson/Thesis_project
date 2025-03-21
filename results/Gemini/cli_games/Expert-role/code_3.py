import random
import time
import os

class SnakeGame:
    """
    A command-line implementation of the Snake game.
    """

    def __init__(self, width=20, height=10, initial_length=3, initial_speed=0.3):
        """
        Initializes the game.

        Args:
            width (int): The width of the game board.
            height (int): The height of the game board.
            initial_length (int): The initial length of the snake.
            initial_speed (float): The initial speed of the game (seconds between moves).
        """
        self.width = width
        self.height = height
        self.snake = [(width // 2, height // 2 - i) for i in range(initial_length)]
        self.food = self.create_food()
        self.direction = "right"
        self.game_over = False
        self.score = 0
        self.speed = initial_speed
        self.paused = False
        self.last_move_time = time.time()

    def create_food(self):
        """
        Creates a new food item at a random location on the board, ensuring it's not on the snake.

        Returns:
            tuple: The coordinates (x, y) of the new food item.
        """
        while True:
            food = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            if food not in self.snake:
                return food

    def move(self):
        """
        Moves the snake one step in the current direction.
        """
        if self.paused:
            return

        current_time = time.time()
        if current_time - self.last_move_time < self.speed:
            return  # Don't move if it's too soon

        self.last_move_time = current_time

        head_x, head_y = self.snake[0]
        if self.direction == "right":
            new_head = (head_x + 1, head_y)
        elif self.direction == "left":
            new_head = (head_x - 1, head_y)
        elif self.direction == "up":
            new_head = (head_x, head_y - 1)
        elif self.direction == "down":
            new_head = (head_x, head_y + 1)

        # Check for game over conditions
        if (
            new_head[0] < 0
            or new_head[0] >= self.width
            or new_head[1] < 0
            or new_head[1] >= self.height
            or new_head in self.snake
        ):
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        # Check if the snake ate the food
        if new_head == self.food:
            self.score += 1
            self.food = self.create_food()
            self.speed *= 0.95  # Increase speed slightly
        else:
            self.snake.pop()  # Remove the tail

    def change_direction(self, new_direction):
        """
        Changes the direction of the snake, preventing immediate 180-degree turns.

        Args:
            new_direction (str): The new direction ("up", "down", "left", "right").
        """
        if new_direction == "right" and self.direction != "left":
            self.direction = "right"
        elif new_direction == "left" and self.direction != "right":
            self.direction = "left"
        elif new_direction == "up" and self.direction != "down":
            self.direction = "up"
        elif new_direction == "down" and self.direction != "up":
            self.direction = "down"

    def draw_board(self):
        """
        Draws the game board in the console.
        """
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        print(f"Score: {self.score}")
        print("-" * (self.width + 2))  # Top border

        for y in range(self.height):
            row = "|"  # Left border
            for x in range(self.width):
                if (x, y) in self.snake:
                    row += "O"  # Snake body
                elif (x, y) == self.food:
                    row += "X"  # Food
                else:
                    row += " "  # Empty space
            row += "|"  # Right border
            print(row)

        print("-" * (self.width + 2))  # Bottom border
        print("Controls: Use arrow keys to move. 'p' to pause/unpause. 'q' to quit.")

    def run(self):
        """
        Runs the main game loop.
        """
        import sys
        import select
        import tty
        import termios

        def is_data():
            return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

        old_settings = termios.tcgetattr(sys.stdin)
        try:
            tty.setcbreak(sys.stdin.fileno())
            while not self.game_over:
                self.draw_board()
                self.move()

                if is_data():
                    c = sys.stdin.read(1)
                    if c == '\x1b[A':  # Up arrow
                        self.change_direction("up")
                    elif c == '\x1b[B':  # Down arrow
                        self.change_direction("down")
                    elif c == '\x1b[C':  # Right arrow
                        self.change_direction("right")
                    elif c == '\x1b[D':  # Left arrow
                        self.change_direction("left")
                    elif c == 'p':
                        self.paused = not self.paused
                    elif c == 'q':
                        self.game_over = True
                else:
                    time.sleep(0.01) # Reduce CPU usage

            self.draw_board()
            print("Game Over! Final Score:", self.score)

        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)



if __name__ == "__main__":
    game = SnakeGame()
    game.run()