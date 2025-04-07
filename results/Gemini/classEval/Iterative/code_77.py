import random

class Snake:
    """
    The class is a snake game, with allows snake to move and eat food, and also enables to reset and generate a random food position.
    """

    def __init__(self, screen_width, screen_height, block_size):
        """
        Initialize the snake.

        :param screen_width: int, The width of the game screen.
        :param screen_height: int, The height of the game screen.
        :param block_size: int, Size of moving units.
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.block_size = block_size
        self.reset()  # Initialize snake's position, length, score, and food

    def reset(self):
        """
        Reset the snake to its initial state.
        """
        self.length = 1
        self.positions = [((self.screen_width // 2), (self.screen_height // 2))]
        self.score = 0
        self.direction = (0, 0)  # Initial direction: stationary
        self.random_food_position()

    def move(self):
        """
        Move the snake in the current direction.
        """
        if self.direction == (0, 0):
            return  # Snake is stationary, don't move

        cur = self.positions[0]
        x, y = self.direction
        new = (((cur[0] + (x * self.block_size)) % self.screen_width),
               (cur[1] + (y * self.block_size)) % self.screen_height)

        if new in self.positions[1:]:
            self.reset()  # Collision with self, game over
        else:
            self.positions.insert(0, new)  # Add new head position
            if new == self.food_position:
                self.eat_food()
            else:
                self.positions.pop()  # Remove tail if no food eaten

    def set_direction(self, direction):
        """
        Set the direction of the snake's movement.

        :param direction: tuple, representing the direction of movement (x, y).  Must be one of (0,1), (0,-1), (1,0), (-1,0)
        """

        # Prevent snake from reversing direction immediately
        if (direction[0] * -1, direction[1] * -1) == self.direction and self.length > 1:
            return
        self.direction = direction

    def random_food_position(self):
        """
        Randomly generate a new food position, but not on the snake's body.
        """
        while True:
            x = random.randint(0, (self.screen_width // self.block_size) - 1) * self.block_size
            y = random.randint(0, (self.screen_height // self.block_size) - 1) * self.block_size
            if (x, y) not in self.positions:
                self.food_position = (x, y)
                return

    def eat_food(self):
        """
        Increase the length of the snake and the score. Generate new food.
        """
        self.length += 1
        self.score += 10
        self.random_food_position()


if __name__ == '__main__':
    # Example Usage
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 480
    BLOCK_SIZE = 20

    snake = Snake(SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE)
    print(f"Initial snake positions: {snake.positions}")
    print(f"Initial snake length: {snake.length}")
    print(f"Initial snake score: {snake.score}")
    print(f"Initial food position: {snake.food_position}")

    snake.set_direction((1, 0))  # Move right
    snake.move()
    print(f"Snake positions after moving right: {snake.positions}")

    initial_score = snake.score
    # Simulate eating food by placing food next to the snake's head
    snake.food_position = (snake.positions[0][0] + BLOCK_SIZE, snake.positions[0][1])
    snake.move()  # Move again to 'eat' the food
    print(f"Snake length after eating food: {snake.length}")
    print(f"Snake score after eating food: {snake.score}")
    print(f"New food position after eating: {snake.food_position}")

    snake.reset()
    print(f"Snake positions after reset: {snake.positions}")
    print(f"Snake length after reset: {snake.length}")
    print(f"Snake score after reset: {snake.score}")
    print(f"New food position after reset: {snake.food_position}")