import random
import curses

class SnakeGame:
    def __init__(self, height=20, width=60):
        self.height = height
        self.width = width
        self.window = curses.initscr()
        self.window.keypad(1)
        curses.noecho()
        curses.cbreak()
        self.window.border(0)
        self.window.timeout(100)
        self.snake = [(height // 2, width // 4)]
        self.snake_dir = (0, 1)  # Start moving right
        self.food = self.place_food()
        self.score = 0

    def place_food(self):
        while True:
            food = (random.randint(1, self.height - 2), random.randint(1, self.width - 2))
            if food not in self.snake:
                return food

    def change_direction(self, key):
        if key == curses.KEY_UP and self.snake_dir != (1, 0):
            self.snake_dir = (-1, 0)
        elif key == curses.KEY_DOWN and self.snake_dir != (-1, 0):
            self.snake_dir = (1, 0)
        elif key == curses.KEY_LEFT and self.snake_dir != (0, 1):
            self.snake_dir = (0, -1)
        elif key == curses.KEY_RIGHT and self.snake_dir != (0, -1):
            self.snake_dir = (0, 1)

    def update(self):
        head_y, head_x = self.snake[0]
        new_head = (head_y + self.snake_dir[0], head_x + self.snake_dir[1])

        if (new_head[0] in [0, self.height - 1] or
                new_head[1] in [0, self.width - 1] or
                new_head in self.snake):
            return False  # Game over

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.food = self.place_food()
        else:
            self.snake.pop()

        return True

    def draw(self):
        self.window.clear()
        self.window.border(0)
        self.window.addstr(0, 2, f'Score: {self.score} ')
        self.window.addstr(self.food[0], self.food[1], '🍏')
        for y, x in self.snake:
            self.window.addstr(y, x, '🐍')
        self.window.refresh()

    def run(self):
        while True:
            self.draw()
            key = self.window.getch()
            self.change_direction(key)
            if not self.update():
                break
        curses.endwin()
        print(f'Game Over! Your score was {self.score}.')

if __name__ == '__main__':
    game = SnakeGame()
    game.run()