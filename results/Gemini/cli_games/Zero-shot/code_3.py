import random
import time
import sys
import os


class SnakeGame:
    """
    A command-line Snake game implementation.
    """

    def __init__(self, width=20, height=10, delay=0.1):
        """
        Initializes the Snake game.

        Args:
            width (int): Width of the game board.
            height (int): Height of the game board.
            delay (float): Delay between game updates in seconds.
        """

        self.width = width
        self.height = height
        self.delay = delay
        self.snake = [(width // 2, height // 2)]  # Snake starts in the middle
        self.direction = "right"
        self.food = self.create_food()
        self.score = 0
        self.game_over = False

    def create_food(self):
        """
        Creates food at a random location that is not occupied by the snake.

        Returns:
            tuple: Coordinates (x, y) of the food.
        """
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if (x, y) not in self.snake:
                return (x, y)

    def move(self):
        """
        Moves the snake in the current direction.
        """

        head_x, head_y = self.snake[0]

        if self.direction == "right":
            new_head = (head_x + 1, head_y)
        elif self.direction == "left":
            new_head = (head_x - 1, head_y)
        elif self.direction == "up":
            new_head = (head_x, head_y - 1)
        elif self.direction == "down":
            new_head = (head_x, head_y + 1)
        else:
            new_head = (head_x, head_y) # Invalid direction, don't move.

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

        self.snake.insert(0, new_head)  # Add new head

        if new_head == self.food:
            self.score += 1
            self.food = self.create_food()
        else:
            self.snake.pop()  # Remove tail if no food eaten

    def change_direction(self, new_direction):
        """
        Changes the direction of the snake, preventing immediate reversals.

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

    def draw(self):
        """
        Draws the game board in the console.
        """
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen

        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in self.snake:
                    print("O", end="")  # Snake body
                elif (x, y) == self.food:
                    print("X", end="")  # Food
                else:
                    print(" ", end="")  # Empty space
            print()
        print(f"Score: {self.score}")
        print("Use 'w', 'a', 's', 'd' to move. 'q' to quit.")

    def run(self):
        """
        Runs the main game loop.
        """
        while not self.game_over:
            self.draw()
            self.move()
            time.sleep(self.delay)

            # Get input (non-blocking)
            user_input = None
            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]: #Check if input is available immediately
                user_input = sys.stdin.readline().strip().lower()


            if user_input == "w":
                self.change_direction("up")
            elif user_input == "s":
                self.change_direction("down")
            elif user_input == "a":
                self.change_direction("left")
            elif user_input == "d":
                self.change_direction("right")
            elif user_input == "q":
                self.game_over = True

        print("Game Over! Final Score:", self.score)


if __name__ == "__main__":
    import select
    game = SnakeGame()
    game.run()