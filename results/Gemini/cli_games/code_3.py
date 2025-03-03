import random
import time
import curses

class SnakeGame:
    def __init__(self, width=20, height=10):
        self.width = width
        self.height = height
        self.snake = [(width // 2, height // 2)]  # Snake starts in the middle
        self.food = self.create_food()
        self.direction = curses.KEY_RIGHT  # Initial direction
        self.score = 0
        self.game_over = False

    def create_food(self):
        """Creates food at a random empty location."""
        while True:
            food = (random.randint(1, self.width - 2), random.randint(1, self.height - 2))
            if food not in self.snake:
                return food

    def move_snake(self):
        """Moves the snake based on the current direction."""
        head_x, head_y = self.snake[0]

        if self.direction == curses.KEY_RIGHT:
            new_head = (head_x + 1, head_y)
        elif self.direction == curses.KEY_LEFT:
            new_head = (head_x - 1, head_y)
        elif self.direction == curses.KEY_UP:
            new_head = (head_x, head_y - 1)
        elif self.direction == curses.KEY_DOWN:
            new_head = (head_x, head_y + 1)
        else:
            return  # Invalid direction

        self.snake.insert(0, new_head)  # Add new head

        # Check if snake ate food
        if new_head == self.food:
            self.score += 1
            self.food = self.create_food()  # Create new food
        else:
            self.snake.pop()  # Remove tail if no food eaten

    def check_collision(self):
        """Checks for collisions with walls or itself."""
        head_x, head_y = self.snake[0]

        if (
            head_x <= 0
            or head_x >= self.width - 1
            or head_y <= 0
            or head_y >= self.height - 1
            or self.snake[0] in self.snake[1:]  # Check self-collision
        ):
            self.game_over = True

    def update(self):
        """Updates the game state."""
        self.move_snake()
        self.check_collision()

    def draw(self, screen):
        """Draws the game on the screen."""
        screen.clear()

        # Draw border
        for i in range(self.width):
            screen.addch(0, i, '#')
            screen.addch(self.height - 1, i, '#')
        for i in range(self.height):
            screen.addch(i, 0, '#')
            screen.addch(i, self.width - 1, '#')


        # Draw snake
        for x, y in self.snake:
            screen.addch(y, x, 'O')

        # Draw food
        screen.addch(self.food[1], self.food[0], '*')

        # Draw score
        screen.addstr(self.height, 0, f"Score: {self.score}")

        screen.refresh()



def main(screen):
    """Main game loop."""
    curses.curs_set(0)  # Hide cursor
    screen.nodelay(1)  # Non-blocking getch
    screen.timeout(100)  # Refresh every 100 ms

    game = SnakeGame(width=40, height=20)

    while not game.game_over:
        game.draw(screen)
        key = screen.getch()

        # Handle input
        if key == curses.KEY_EXIT or key == ord('q'):
            break
        elif key in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN]:
            # Prevent snake from going directly backwards
            if (key == curses.KEY_LEFT and game.direction != curses.KEY_RIGHT) or \
               (key == curses.KEY_RIGHT and game.direction != curses.KEY_LEFT) or \
               (key == curses.KEY_UP and game.direction != curses.KEY_DOWN) or \
               (key == curses.KEY_DOWN and game.direction != curses.KEY_UP):
                game.direction = key

        game.update()

    # Game over message
    screen.clear()
    screen.addstr(game.height // 2, game.width // 2 - 5, "Game Over!")
    screen.addstr(game.height // 2 + 1, game.width // 2 - 7, f"Final Score: {game.score}")
    screen.refresh()
    time.sleep(2)



if __name__ == '__main__':
    curses.wrapper(main)