import random
import time
import os

class SnakeGame:
    """
    A command-line implementation of the classic Snake game.
    """

    def __init__(self, width=20, height=10, initial_length=3):
        """
        Initializes the game.

        Args:
            width (int): The width of the game board.
            height (int): The height of the game board.
            initial_length (int): The initial length of the snake.
        """
        self.width = width
        self.height = height
        self.snake = [(width // 2, height // 2 - i) for i in range(initial_length)]  # Snake starts in the middle
        self.food = self.create_food()
        self.direction = "right"  # Initial direction
        self.game_over = False
        self.score = 0
        self.delay = 0.1 # Initial delay
        self.initial_length = initial_length

    def create_food(self):
        """
        Creates food at a random location on the board, ensuring it's not on the snake.

        Returns:
            tuple: The coordinates (x, y) of the food.
        """
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if (x, y) not in self.snake:
                return (x, y)

    def move(self):
        """
        Moves the snake one step in the current direction.
        """
        head_x, head_y = self.snake[0]

        if self.direction == "up":
            new_head = (head_x, head_y - 1)
        elif self.direction == "down":
            new_head = (head_x, head_y + 1)
        elif self.direction == "left":
            new_head = (head_x - 1, head_y)
        elif self.direction == "right":
            new_head = (head_x + 1, head_y)

        # Check for collision with walls or itself
        if (
            new_head[0] < 0
            or new_head[0] >= self.width
            or new_head[1] < 0
            or new_head[1] >= self.height
            or new_head in self.snake
        ):
            self.game_over = True
            return

        self.snake.insert(0, new_head)  # Add the new head

        # Check if the snake ate the food
        if new_head == self.food:
            self.score += 1
            self.food = self.create_food()
            self.delay *= 0.95  # Increase speed as the snake grows
        else:
            self.snake.pop()  # Remove the tail if it didn't eat

    def change_direction(self, new_direction):
        """
        Changes the direction of the snake, preventing immediate 180-degree turns.

        Args:
            new_direction (str): The new direction ("up", "down", "left", "right").
        """
        if new_direction == "up" and self.direction != "down":
            self.direction = "up"
        elif new_direction == "down" and self.direction != "up":
            self.direction = "down"
        elif new_direction == "left" and self.direction != "right":
            self.direction = "left"
        elif new_direction == "right" and self.direction != "left":
            self.direction = "right"

    def draw(self):
        """
        Draws the game board in the console.
        """
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        print(f"Score: {self.score}")

        for y in range(self.height):
            for x in range(self.width):
                if (x, y) == self.food:
                    print("F", end="")  # Food
                elif (x, y) in self.snake:
                    if (x, y) == self.snake[0]:
                        print("H", end="") # Head
                    else:
                        print("S", end="")  # Snake body
                else:
                    print(".", end="")  # Empty space
            print()  # New line at the end of each row

    def play(self):
        """
        The main game loop.
        """
        while not self.game_over:
            self.draw()
            self.move()
            time.sleep(self.delay)

            # Get user input (non-blocking)
            # This is platform-dependent and requires additional libraries like 'msvcrt' on Windows or 'select' on Linux/macOS
            # For simplicity, we'll use a simple keyboard input method that requires pressing Enter after each move.
            # A better implementation would use non-blocking input.
            direction = input("Enter direction (up, down, left, right, or q to quit): ").lower()
            if direction == 'q':
                self.game_over = True
                break
            if direction in ("up", "down", "left", "right"):
                self.change_direction(direction)

        print("Game Over!")
        print(f"Final Score: {self.score}")

    def reset(self):
        """Resets the game to its initial state."""
        self.snake = [(self.width // 2, self.height // 2 - i) for i in range(self.initial_length)]
        self.food = self.create_food()
        self.direction = "right"
        self.game_over = False
        self.score = 0
        self.delay = 0.1

if __name__ == "__main__":
    game = SnakeGame()
    game.play()