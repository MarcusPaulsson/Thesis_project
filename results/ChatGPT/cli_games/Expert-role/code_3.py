import random
import curses

class SnakeGame:
    def __init__(self):
        self.screen = curses.initscr()
        self.height, self.width = self.screen.getmaxyx()
        self.window = curses.newwin(self.height, self.width, 0, 0)
        self.window.keypad(1)
        self.window.timeout(100)
        
        self.snake = [(self.height // 2, self.width // 4)]
        self.snake_direction = curses.KEY_RIGHT
        self.food = self.place_food()
        self.score = 0

    def place_food(self):
        while True:
            food = (random.randint(1, self.height - 1), random.randint(1, self.width - 1))
            if food not in self.snake:
                return food

    def game_over(self):
        self.window.addstr(self.height // 2, self.width // 2 - 5, "Game Over")
        self.window.refresh()
        self.window.getch()
        curses.endwin()
        exit()

    def run(self):
        while True:
            next_key = self.window.getch()
            self.snake_direction = next_key if next_key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN] else self.snake_direction
            
            head_y, head_x = self.snake[0]
            if self.snake_direction == curses.KEY_DOWN:
                head_y += 1
            elif self.snake_direction == curses.KEY_UP:
                head_y -= 1
            elif self.snake_direction == curses.KEY_LEFT:
                head_x -= 1
            elif self.snake_direction == curses.KEY_RIGHT:
                head_x += 1

            new_head = (head_y, head_x)

            if (new_head in self.snake or
                    head_y in [0, self.height] or
                    head_x in [0, self.width]):
                self.game_over()

            self.snake.insert(0, new_head)
            if new_head == self.food:
                self.score += 1
                self.food = self.place_food()
            else:
                self.snake.pop()

            self.window.clear()
            self.window.border(0)
            self.window.addstr(0, 2, f'Score: {self.score} ')
            self.window.addch(self.food[0], self.food[1], curses.ACS_PI)
            for y, x in self.snake:
                self.window.addch(y, x, curses.ACS_CKBOARD)

if __name__ == "__main__":
    game = SnakeGame()
    try:
        game.run()
    finally:
        curses.endwin()