import random

class Snake:
    """
    The class represents a snake game where the snake can move, eat food, reset, and generate a random food position.
    """

    def __init__(self, screen_width, screen_height, block_size):
        """
        Initialize the snake's initial state.
        :param screen_width: int, width of the game screen.
        :param screen_height: int, height of the game screen.
        :param block_size: int, size of moving units.
        """
        self.length = 1
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.block_size = block_size
        self.positions = [(screen_width // 2, screen_height // 2)]
        self.score = 0
        self.food_position = self.random_food_position()

    def move(self, direction):
        """
        Move the snake in the specified direction.
        :param direction: tuple, representing the direction of movement (dx, dy).
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
        Randomly generate a new food position that is not occupied by the snake.
        :return: tuple, representing the position (x, y) of food.
        """
        while True:
            x = random.randint(0, (self.screen_width - self.block_size) // self.block_size) * self.block_size
            y = random.randint(0, (self.screen_height - self.block_size) // self.block_size) * self.block_size
            food_position = (x, y)
            if food_position not in self.positions:
                return food_position

    def reset(self):
        """
        Reset the snake to its initial state.
        """
        self.length = 1
        self.positions = [(self.screen_width // 2, self.screen_height // 2)]
        self.score = 0
        self.food_position = self.random_food_position()

    def eat_food(self):
        """
        Increase the length of the snake and the score by 100, and generate a new food position.
        """
        self.length += 1
        self.score += 100
        self.food_position = self.random_food_position()