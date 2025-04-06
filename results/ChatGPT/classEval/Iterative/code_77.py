import random

class Snake:
    """
    The class is for a snake game that allows the snake to move, eat food, and reset the game.
    """

    def __init__(self, screen_width, screen_height, block_size):
        """
        Initialize the snake with its properties.
        :param screen_width: int - width of the game screen
        :param screen_height: int - height of the game screen
        :param block_size: int - size of each block the snake moves
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
        :param direction: tuple - (x, y) direction of movement
        """
        new_head = (self.positions[0][0] + direction[0] * self.block_size, 
                     self.positions[0][1] + direction[1] * self.block_size)

        # Check if the snake has eaten food
        if new_head == self.food_position:
            self.eat_food()
        else:
            # Move the snake
            self.positions.insert(0, new_head)
            if len(self.positions) > self.length:
                self.positions.pop()

        # Check for collision with itself
        if new_head in self.positions[1:]:
            self.reset()

    def random_food_position(self):
        """
        Generate a new food position that does not overlap with the snake.
        :return: tuple - new food position (x, y)
        """
        while True:
            x = random.randint(0, (self.screen_width // self.block_size) - 1) * self.block_size
            y = random.randint(0, (self.screen_height // self.block_size) - 1) * self.block_size
            if (x, y) not in self.positions:
                return (x, y)

    def reset(self):
        """
        Reset the game state.
        """
        self.length = 1
        self.positions = [(self.screen_width // 2, self.screen_height // 2)]
        self.score = 0
        self.food_position = self.random_food_position()

    def eat_food(self):
        """
        Handle the logic for eating food.
        """
        self.length += 1
        self.score += 100
        self.food_position = self.random_food_position()