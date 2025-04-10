import random

class Snake:
    """
    The class represents a snake in the snake game, allowing movement, food consumption, reset functionality,
    and random food position generation.
    """

    def __init__(self, screen_width, screen_height, block_size, food_position):
        """
        Initialize the snake's properties.
        :param screen_width: int, width of the game screen
        :param screen_height: int, height of the game screen
        :param block_size: int, size of moving units
        :param food_position: tuple, initial position (x, y) of the food
        """
        self.length = 1
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.block_size = block_size
        self.positions = [(screen_width // 2, screen_height // 2)]
        self.score = 0
        self.food_position = food_position

    def move(self, direction):
        """
        Move the snake in the specified direction, handle food consumption and self-collision.
        :param direction: tuple, representing the direction of movement (x, y).
        """
        new_head = (self.positions[0][0] + direction[0] * self.block_size,
                     self.positions[0][1] + direction[1] * self.block_size)

        if new_head == self.food_position:
            self.eat_food()
        elif new_head in self.positions:
            self.reset()
        else:
            self.positions.insert(0, new_head)
            if len(self.positions) > self.length:
                self.positions.pop()

    def random_food_position(self):
        """
        Generate a new food position that is not occupied by the snake.
        """
        while True:
            new_food_position = (
                random.randint(0, (self.screen_width // self.block_size) - 1) * self.block_size,
                random.randint(0, (self.screen_height // self.block_size) - 1) * self.block_size
            )
            if new_food_position not in self.positions:
                self.food_position = new_food_position
                break

    def reset(self):
        """
        Reset the snake to its initial state and generate a new food position.
        """
        self.length = 1
        self.positions = [(self.screen_width // 2, self.screen_height // 2)]
        self.score = 0
        self.random_food_position()

    def eat_food(self):
        """
        Increase the snake's length and score, and generate a new food position.
        """
        self.length += 1
        self.score += 100
        self.random_food_position()