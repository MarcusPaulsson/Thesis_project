import random
import time
import os

class SnakeGame:
    """
    A command-line Snake game implementation.
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
        self.snake = [(width // 2, height // 2 - i) for i in range(initial_length)]  # Start in the middle, going up
        self.food = self.create_food()
        self.direction = "down"  # Initial direction
        self.game_over = False
        self.score = 0
        self.delay = 0.2 # Delay between moves (seconds)

    def create_food(self):
        """
        Creates food at a random location that is not occupied by the snake.

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
        else:
            raise ValueError("Invalid direction")

        # Check for game over conditions (collision with wall or self)
        if (
            new_head[0] < 0
            or new_head[0] >= self.width
            or new_head[1] < 0
            or new_head[1] >= self.height
            or new_head in self.snake
        ):
            self.game_over = True
            return

        self.snake.insert(0, new_head)  # Add new head

        # Check if food was eaten
        if new_head == self.food:
            self.score += 1
            self.food = self.create_food()
            self.delay *= 0.95 # Speed up slightly
        else:
            self.snake.pop()  # Remove tail if no food eaten

    def change_direction(self, new_direction):
        """
        Changes the direction of the snake, preventing immediate reversal.

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

    def draw_board(self):
        """
        Draws the game board in the console.
        """

        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        print(f"Score: {self.score}")

        for y in range(self.height):
            for x in range(self.width):
                if (x, y) == self.food:
                    print("F", end="")
                elif (x, y) in self.snake:
                    if (x,y) == self.snake[0]:
                        print("H", end="") # Head
                    else:
                        print("S", end="")
                else:
                    print(" ", end="")
            print()  # Newline at the end of each row

    def play(self):
        """
        Plays the game.
        """

        while not self.game_over:
            self.draw_board()
            self.move()
            time.sleep(self.delay)

            # Get user input (non-blocking)
            import select
            import sys

            if select.select([sys.stdin], [], [], 0)[0]:
                key = sys.stdin.read(1)

                if key == "w":
                    self.change_direction("up")
                elif key == "s":
                    self.change_direction("down")
                elif key == "a":
                    self.change_direction("left")
                elif key == "d":
                    self.change_direction("right")
                elif key == "q":
                    self.game_over = True # Quit

        print("Game Over!")
        print(f"Final Score: {self.score}")


if __name__ == "__main__":
    game = SnakeGame()
    game.play()