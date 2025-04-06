import random

class Snake:
    """
    The class is a snake game, with allows snake to move and eat food, and also enables to reset, and generat a random food position.
    """

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE):
        """
        Initialize the length of the snake, screen width, screen height, block size, snake head position, score, and food position.
        :param SCREEN_WIDTH: int
        :param SCREEN_HEIGHT: int
        :param BLOCK_SIZE: int, Size of moving units
        """
        self.length = 1
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.BLOCK_SIZE = BLOCK_SIZE
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.score = 0
        self.food_position = self.random_food_position() # Initialize food position

    def move(self, direction):
        """
        Move the snake in the specified direction. If the new position of the snake's head is equal to the position of the food, then eat the food; If the position of the snake's head is equal to the position of its body, then start over, otherwise its own length plus one.
        :param direction: tuple, representing the direction of movement (x, y).
        :return: None
        """
        x, y = self.positions[0]
        new_head = (x + direction[0] * self.BLOCK_SIZE, y + direction[1] * self.BLOCK_SIZE)
        self.positions.insert(0, new_head)

        if new_head == self.food_position:
            self.eat_food()
        else:
            self.positions.pop()

        # Check for self-collision
        if len(self.positions) != len(set(self.positions)):
            self.reset()

        # Check for out-of-bounds
        if not (0 <= new_head[0] < self.SCREEN_WIDTH and 0 <= new_head[1] < self.SCREEN_HEIGHT):
            self.reset()


    def random_food_position(self):
        """
        Randomly generate a new food position, but don't place it on the snake.
        :return: tuple, representing the new food position
        """
        while True:
            x = random.randrange(0, self.SCREEN_WIDTH // self.BLOCK_SIZE) * self.BLOCK_SIZE
            y = random.randrange(0, self.SCREEN_HEIGHT // self.BLOCK_SIZE) * self.BLOCK_SIZE
            food_position = (x, y)
            if food_position not in self.positions:
                return food_position


    def reset(self):
        """
        Reset the snake to its initial state. Set the length to 1, the snake head position to ((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2)), the score to 0, and randomly generate new food position.
        :return: None
        """
        self.length = 1
        self.positions = [((self.SCREEN_WIDTH // 2), (self.SCREEN_HEIGHT // 2))]
        self.score = 0
        self.food_position = self.random_food_position()


    def eat_food(self):
        """
        Increase the length of the snake by 1 and increase the score by 10. Randomly generate a new food position, but
        don't place it on the snake.
        :return: None
        """
        self.length += 1
        self.score += 10
        self.food_position = self.random_food_position()