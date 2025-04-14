import random

class Snake:
    """
    The class is a snake game, with allows snake to move and eat food, and also enables to reset, and generat a random food position.
    """

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, food_position):
        """
        Initialize the length of the snake, screen width, screen height, block size, snake head position, score, and food position.
        :param SCREEN_WIDTH: int
        :param SCREEN_HEIGHT: int
        :param BLOCK_SIZE: int, Size of moving units
        :param food_position: tuple, representing the position(x, y) of food.
        """
        self.length = 1
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.BLOCK_SIZE = BLOCK_SIZE
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.score = 0
        self.food_position = food_position


    def move(self, direction):
        """
        Move the snake in the specified direction. If the new position of the snake's head is equal to the position of the food, then eat the food; If the position of the snake's head is equal to the position of its body, then start over, otherwise its own length plus one.
        :param direction: tuple, representing the direction of movement (x, y).
        :return: None
        """
        x, y = self.positions[0]
        new_head = (x + direction[0], y + direction[1])

        if new_head == self.food_position:
            self.eat_food()
            self.positions.insert(0, new_head)
        elif new_head in self.positions[1:]:
            self.reset()
        else:
            self.positions.insert(0, new_head)
            self.positions.pop()

    def random_food_position(self):
        """
        Randomly generate a new food position, but don't place it on the snake.
        :return: None, Change the food position
        """
        while True:
            x = random.randint(0, self.SCREEN_WIDTH - 1)
            y = random.randint(0, self.SCREEN_HEIGHT - 1)
            if (x, y) not in self.positions:
                self.food_position = (x, y)
                break


    def reset(self):
        """
        Reset the snake to its initial state. Set the length to 1, the snake head position to ((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2)), the score to 0, and randomly generate new food position.
        :return: None
        """
        self.length = 1
        self.positions = [((self.SCREEN_WIDTH // 2), (self.SCREEN_HEIGHT // 2))]
        self.score = 0
        self.random_food_position()


    def eat_food(self):
        """
        Increase the length of the snake by 1 and increase the score by 100. Randomly generate a new food position, but
        don't place it on the snake.
        :return: None
        """
        self.length += 1
        self.score += 100
        self.random_food_position()