import random
import curses

class SnakeGame:
    def __init__(self, height=20, width=60):
        self.height = height
        self.width = width
        self.window = curses.initscr()
        self.window.keypad(1)
        self.window.timeout(100)
        self.snake = [[height // 2, width // 4]]
        self.snake_direction = curses.KEY_RIGHT
        self.food = self.place_food()
        self.score = 0

    def place_food(self):
        while True:
            food = [random.randint(1, self.height - 1), random.randint(1, self.width - 1)]
            if food not in self.snake:
                return food

    def run(self):
        while True:
            next_key = self.window.getch()
            self.snake_direction = next_key if next_key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN] else self.snake_direction

            new_head = self.snake[0][:]
            if self.snake_direction == curses.KEY_DOWN:
                new_head[0] += 1
            elif self.snake_direction == curses.KEY_UP:
                new_head[0] -= 1
            elif self.snake_direction == curses.KEY_LEFT:
                new_head[1] -= 1
            elif self.snake_direction == curses.KEY_RIGHT:
                new_head[1] += 1

            if new_head in self.snake or new_head[0] in [0, self.height] or new_head[1] in [0, self.width]:
                curses.endwin()
                print("Game Over! Your score is: {}".format(self.score))
                break

            self.snake.insert(0, new_head)

            if self.snake[0] == self.food:
                self.score += 1
                self.food = self.place_food()
            else:
                self.snake.pop()

            self.window.clear()
            self.window.border(0)
            self.window.addstr(0, 2, 'Score: {}'.format(self.score))
            self.window.addch(int(self.food[0]), int(self.food[1]), curses.ACS_PI)
            for segment in self.snake:
                self.window.addch(int(segment[0]), int(segment[1]), curses.ACS_CKBOARD)
            self.window.refresh()

if __name__ == "__main__":
    curses.wrapper(SnakeGame().run)