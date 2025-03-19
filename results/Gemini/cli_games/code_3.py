import random
import time
import os

class SnakeGame:
    """
    A command-line implementation of the classic Snake game.
    """

    def __init__(self, width=20, height=15, initial_length=3):
        """
        Initializes the Snake game.

        Args:
            width (int): The width of the game board.
            height (int): The height of the game board.
            initial_length (int): The initial length of the snake.
        """
        self.width = width
        self.height = height
        self.initial_length = initial_length
        self.snake = []
        self.food = None
        self.direction = "RIGHT"
        self.game_over = False
        self.score = 0
        self.delay = 0.1  # Initial delay between moves
        self.setup_game()

    def setup_game(self):
        """
        Sets up the initial game state.
        """
        self.snake = [(self.width // 2 - i, self.height // 2) for i in range(self.initial_length)]
        self.generate_food()

    def generate_food(self):
        """
        Generates food at a random location that is not occupied by the snake.
        """
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if (x, y) not in self.snake:
                self.food = (x, y)
                break

    def move(self):
        """
        Moves the snake based on the current direction.
        """
        head_x, head_y = self.snake[0]
        if self.direction == "UP":
            new_head = (head_x, (head_y - 1) % self.height) #Wrap around
        elif self.direction == "DOWN":
            new_head = (head_x, (head_y + 1) % self.height) #Wrap around
        elif self.direction == "LEFT":
            new_head = ((head_x - 1) % self.width, head_y) #Wrap around
        elif self.direction == "RIGHT":
            new_head = ((head_x + 1) % self.width, head_y) #Wrap around

        if new_head in self.snake:
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.generate_food()
            self.delay *= 0.95  # Increase speed
        else:
            self.snake.pop()

    def change_direction(self, new_direction):
        """
        Changes the direction of the snake, preventing immediate reversals.
        """
        if new_direction == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        elif new_direction == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
        elif new_direction == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif new_direction == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"

    def draw_board(self):
        """
        Draws the game board in the console.
        """
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        print("Score:", self.score)
        print("-" * (self.width + 2))
        for y in range(self.height):
            print("|", end="")
            for x in range(self.width):
                if (x, y) in self.snake:
                    print("O", end="")
                elif (x, y) == self.food:
                    print("F", end="")
                else:
                    print(" ", end="")
            print("|")
        print("-" * (self.width + 2))

    def play(self):
        """
        Runs the main game loop.
        """
        while not self.game_over:
            self.draw_board()
            self.move()
            time.sleep(self.delay)

            # Get user input (non-blocking)
            # This requires a library like `msvcrt` on Windows or `select` on Linux/macOS
            # For simplicity, we'll just poll for input every frame.  This is not ideal
            #  but works for a basic example.  A proper implementation would use threads or async.
            import sys
            import select

            timeout = 0.001 # Small timeout for non-blocking read
            rlist, _, _ = select.select([sys.stdin], [], [], timeout)
            if rlist:
                key = sys.stdin.readline().strip().upper()  # Read a line
                if key == "W":
                    self.change_direction("UP")
                elif key == "S":
                    self.change_direction("DOWN")
                elif key == "A":
                    self.change_direction("LEFT")
                elif key == "D":
                    self.change_direction("RIGHT")
                elif key == "Q": #Quit
                    self.game_over = True


        self.draw_board()
        print("Game Over! Final Score:", self.score)


if __name__ == "__main__":
    game = SnakeGame()
    game.play()