import random
import curses

class SnakeGame:
    def __init__(self, height=20, width=60):
        self.height = height
        self.width = width
        self.window = curses.initscr()
        curses.curs_set(0)
        self.window.timeout(100)
        self.window.keypad(1)
        self.snake = [(height // 2, width // 2)]
        self.snake_direction = curses.KEY_RIGHT
        self.food = self.place_food()
        self.score = 0

    def place_food(self):
        while True:
            food = (random.randint(1, self.height - 1), random.randint(1, self.width - 1))
            if food not in self.snake:
                return food

    def run(self):
        while True:
            next_key = self.window.getch()
            self.snake_direction = next_key if next_key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN] else self.snake_direction
            self.move_snake()
            self.draw()
            if self.is_game_over():
                break

        self.window.addstr(self.height // 2, self.width // 2 - len("Game Over!") // 2, "Game Over!")
        self.window.addstr(self.height // 2 + 1, self.width // 2 - len(f"Score: {self.score}") // 2, f"Score: {self.score}")
        self.window.refresh()
        self.window.getch()
        curses.endwin()

    def move_snake(self):
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
        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.food = self.place_food()
        else:
            self.snake.pop()

    def draw(self):
        self.window.clear()
        self.window.border(0)
        self.window.addstr(0, 2, f'Score: {self.score}')    
        self.window.addch(self.food[0], self.food[1], curses.ACS_PI)
        for segment in self.snake:
            self.window.addch(segment[0], segment[1], curses.ACS_CKBOARD)
        self.window.refresh()

    def is_game_over(self):
        head = self.snake[0]
        return (
            head[0] in [0, self.height] or
            head[1] in [0, self.width] or
            head in self.snake[1:]
        )

if __name__ == "__main__":
    game = SnakeGame()
    game.run()