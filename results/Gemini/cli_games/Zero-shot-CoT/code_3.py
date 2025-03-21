import random
import time
import os

class SnakeGame:
    def __init__(self, width=20, height=15):
        self.width = width
        self.height = height
        self.snake = [(width // 2, height // 2)]  # Snake starts in the middle
        self.food = self.create_food()
        self.direction = 'right'  # Initial direction
        self.game_over = False
        self.score = 0

    def create_food(self):
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if (x, y) not in self.snake:
                return (x, y)

    def move(self):
        head_x, head_y = self.snake[0]

        if self.direction == 'up':
            new_head = (head_x, (head_y - 1) % self.height)
        elif self.direction == 'down':
            new_head = (head_x, (head_y + 1) % self.height)
        elif self.direction == 'left':
            new_head = ((head_x - 1) % self.width, head_y)
        elif self.direction == 'right':
            new_head = ((head_x + 1) % self.width, head_y)

        if new_head in self.snake:
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.food = self.create_food()
        else:
            self.snake.pop()

    def change_direction(self, new_direction):
        if new_direction == 'up' and self.direction != 'down':
            self.direction = 'up'
        elif new_direction == 'down' and self.direction != 'up':
            self.direction = 'down'
        elif new_direction == 'left' and self.direction != 'right':
            self.direction = 'left'
        elif new_direction == 'right' and self.direction != 'left':
            self.direction = 'right'

    def draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        print(f"Score: {self.score}")

        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in self.snake:
                    print("O", end="")
                elif (x, y) == self.food:
                    print("F", end="")
                else:
                    print(".", end="")
            print()  # Newline at the end of each row

    def play(self):
        while not self.game_over:
            self.draw()
            self.move()

            if self.game_over:
                break

            time.sleep(0.1)  # Adjust speed here

            # Get input from the user (non-blocking)
            import select, sys
            timeout = 0.001 #Small timeout for non-blocking input
            rlist, _, _ = select.select([sys.stdin], [], [], timeout)

            if rlist: #If there's input
                key = sys.stdin.readline().strip().lower()

                if key == 'w':
                    self.change_direction('up')
                elif key == 's':
                    self.change_direction('down')
                elif key == 'a':
                    self.change_direction('left')
                elif key == 'd':
                    self.change_direction('right')
                elif key == 'q':
                    self.game_over = True #Quit

        print("Game Over!")
        print(f"Final Score: {self.score}")

if __name__ == '__main__':
    game = SnakeGame()
    game.play()