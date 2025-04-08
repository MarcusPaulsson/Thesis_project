import random

class Snake:
    """
    A snake game class that allows the snake to move, eat food, reset, and generate random food positions.
    """

    def __init__(self, screen_width, screen_height, block_size, initial_food_position):
        """
        Initializes the snake's attributes.

        :param screen_width: The width of the game screen in blocks.
        :param screen_height: The height of the game screen in blocks.
        :param block_size: The size of each block in pixels.
        :param initial_food_position: The initial position of the food (x, y) in blocks.
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.block_size = block_size
        self.length = 1
        self.positions = [(screen_width // 2, screen_height // 2)]  # Initial position is the center of the screen
        self.score = 0
        self.food_position = initial_food_position
    
    def move(self, direction):
        """
        Moves the snake in the given direction.

        :param direction: A tuple representing the direction of movement (dx, dy), where dx and dy are integers.
        """
        head_x, head_y = self.positions[0]
        new_head = (head_x + direction[0], head_y + direction[1])

        if new_head == self.food_position:
            self._eat_food()
            self.positions.insert(0, new_head)
            self.length += 1
            self.score += 100
        elif (
            new_head[0] < 0
            or new_head[0] >= self.screen_width
            or new_head[1] < 0
            or new_head[1] >= self.screen_height
            or new_head in self.positions[1:]
        ):
            self.reset()
        else:
            self.positions.insert(0, new_head)
            self.positions.pop()

    def _eat_food(self):
        """
        Handles the logic when the snake eats food: generates new food, increases length and score. Internal method.
        """
        self.length += 1
        self.score += 100
        self.random_food_position()

    def random_food_position(self):
        """
        Generates a random food position that is not on the snake's body.
        """
        while True:
            x = random.randint(0, self.screen_width - 1)
            y = random.randint(0, self.screen_height - 1)
            food_position = (x, y)
            if food_position not in self.positions:
                self.food_position = food_position
                break

    def reset(self):
        """
        Resets the snake to its initial state.
        """
        self.length = 1
        self.positions = [(self.screen_width // 2, self.screen_height // 2)]
        self.score = 0
        self.random_food_position()