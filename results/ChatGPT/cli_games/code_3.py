import random
import curses

class SnakeGame:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.window_height = 20
        self.window_width = 60
        self.snake = [(self.window_height // 2, self.window_width // 4)]
        self.snake_direction = (0, 1)  # Initially moving to the right
        self.food = None
        self.score = 0
        self.game_over = False
        self.setup()

    def setup(self):
        curses.curs_set(0)
        self.stdscr.clear()
        self.stdscr.nodelay(1)
        self.stdscr.timeout(100)
        self.place_food()
        self.draw()

    def place_food(self):
        while True:
            food = (random.randint(1, self.window_height - 2), random.randint(1, self.window_width - 2))
            if food not in self.snake:
                self.food = food
                break

    def draw(self):
        self.stdscr.clear()
        for y, x in self.snake:
            self.stdscr.addch(y, x, curses.ACS_CKBOARD)
        self.stdscr.addch(self.food[0], self.food[1], curses.ACS_PI)
        self.stdscr.addstr(0, 2, f'Score: {self.score}')
        self.stdscr.refresh()

    def change_direction(self, key):
        if key == curses.KEY_UP and self.snake_direction != (1, 0):
            self.snake_direction = (-1, 0)
        elif key == curses.KEY_DOWN and self.snake_direction != (-1, 0):
            self.snake_direction = (1, 0)
        elif key == curses.KEY_LEFT and self.snake_direction != (0, 1):
            self.snake_direction = (0, -1)
        elif key == curses.KEY_RIGHT and self.snake_direction != (0, -1):
            self.snake_direction = (0, 1)

    def move_snake(self):
        head_y, head_x = self.snake[0]
        new_head = (head_y + self.snake_direction[0], head_x + self.snake_direction[1])
        
        if (new_head[0] in [0, self.window_height] or
                new_head[1] in [0, self.window_width] or
                new_head in self.snake):
            self.game_over = True
            return
        
        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.place_food()
        else:
            self.snake.pop()

    def play(self):
        while not self.game_over:
            key = self.stdscr.getch()
            self.change_direction(key)
            self.move_snake()
            self.draw()

        self.stdscr.addstr(self.window_height // 2, self.window_width // 2 - 5, "Game Over!")
        self.stdscr.addstr(self.window_height // 2 + 1, self.window_width // 2 - 5, f'Final Score: {self.score}')
        self.stdscr.refresh()
        self.stdscr.getch()

def main():
    curses.wrapper(SnakeGame)

if __name__ == "__main__":
    main()