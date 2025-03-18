import random
import time
import os

class SnakeGame:
    def __init__(self, width=20, height=15, delay=0.1):
        self.width = width
        self.height = height
        self.snake = [(width // 2, height // 2)]
        self.food = self.create_food()
        self.direction = "right"
        self.game_over = False
        self.score = 0
        self.delay = delay

    def create_food(self):
        while True:
            food = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            if food not in self.snake:
                return food

    def move(self):
        head_x, head_y = self.snake[0]

        if self.direction == "right":
            new_head = (head_x + 1, head_y)
        elif self.direction == "left":
            new_head = (head_x - 1, head_y)
        elif self.direction == "up":
            new_head = (head_x, head_y - 1)
        elif self.direction == "down":
            new_head = (head_x, head_y + 1)

        if (
            new_head[0] < 0
            or new_head[0] >= self.width
            or new_head[1] < 0
            or new_head[1] >= self.height
            or new_head in self.snake
        ):
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.food = self.create_food()
        else:
            self.snake.pop()

    def change_direction(self, new_direction):
        if new_direction == "right" and self.direction != "left":
            self.direction = "right"
        elif new_direction == "left" and self.direction != "right":
            self.direction = "left"
        elif new_direction == "up" and self.direction != "down":
            self.direction = "up"
        elif new_direction == "down" and self.direction != "up":
            self.direction = "down"

    def draw(self):
        os.system("cls" if os.name == "nt" else "clear")  # Clear the console

        for y in range(self.height):
            for x in range(self.width):
                if (x, y) == self.food:
                    print("F", end="")
                elif (x, y) in self.snake:
                    if (x,y) == self.snake[0]:
                        print("H", end="")
                    else:
                        print("S", end="")
                else:
                    print(" ", end="")
            print()

        print(f"Score: {self.score}")
        print("Use 'w', 'a', 's', 'd' to move. Press 'q' to quit.")

    def play(self):
        while not self.game_over:
            self.draw()
            time.sleep(self.delay)

            direction = input("Enter move (w/a/s/d/q): ").lower()
            if direction == "q":
                self.game_over = True
                break
            elif direction in ("w", "a", "s", "d"):
                if direction == "w":
                    self.change_direction("up")
                elif direction == "a":
                    self.change_direction("left")
                elif direction == "s":
                    self.change_direction("down")
                elif direction == "d":
                    self.change_direction("right")

            self.move()

        print("Game Over!")
        print(f"Final Score: {self.score}")


if __name__ == "__main__":
    game = SnakeGame()
    game.play()