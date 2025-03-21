import os
import sys
import time
import random
import threading

class Pong:
    def __init__(self, width=40, height=20):
        self.width = width
        self.height = height
        self.ball_x = width // 2
        self.ball_y = height // 2
        self.ball_dx = random.choice([-1, 1])
        self.ball_dy = random.choice([-1, 1])
        self.paddle_left_y = height // 2
        self.paddle_right_y = height // 2
        self.score_left = 0
        self.score_right = 0
        self.running = True

    def draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(self.height):
            for x in range(self.width):
                if x == 0 and y in range(self.paddle_left_y - 1, self.paddle_left_y + 2):
                    print('|', end='')
                elif x == self.width - 1 and y in range(self.paddle_right_y - 1, self.paddle_right_y + 2):
                    print('|', end='')
                elif x == self.ball_x and y == self.ball_y:
                    print('O', end='')
                else:
                    print(' ', end='')
            print()
        print(f'Score: Left {self.score_left} - Right {self.score_right}')

    def update_ball(self):
        if self.ball_x <= 1:
            self.score_right += 1
            self.reset_ball()
        elif self.ball_x >= self.width - 2:
            self.score_left += 1
            self.reset_ball()
        elif self.ball_y <= 0 or self.ball_y >= self.height - 1:
            self.ball_dy *= -1

        if self.ball_x == 1 and self.paddle_left_y - 1 <= self.ball_y <= self.paddle_left_y + 1:
            self.ball_dx *= -1
        elif self.ball_x == self.width - 2 and self.paddle_right_y - 1 <= self.ball_y <= self.paddle_right_y + 1:
            self.ball_dx *= -1

        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy

    def reset_ball(self):
        self.ball_x = self.width // 2
        self.ball_y = self.height // 2
        self.ball_dx = random.choice([-1, 1])
        self.ball_dy = random.choice([-1, 1])

    def move_paddle(self, direction, side):
        if side == 'left':
            if direction == 'up' and self.paddle_left_y > 1:
                self.paddle_left_y -= 1
            elif direction == 'down' and self.paddle_left_y < self.height - 2:
                self.paddle_left_y += 1
        elif side == 'right':
            if direction == 'up' and self.paddle_right_y > 1:
                self.paddle_right_y -= 1
            elif direction == 'down' and self.paddle_right_y < self.height - 2:
                self.paddle_right_y += 1

    def play(self):
        def input_thread():
            while self.running:
                command = input()
                if command == 'w':
                    self.move_paddle('up', 'left')
                elif command == 's':
                    self.move_paddle('down', 'left')
                elif command == 'i':
                    self.move_paddle('up', 'right')
                elif command == 'k':
                    self.move_paddle('down', 'right')

        threading.Thread(target=input_thread, daemon=True).start()

        while self.running:
            self.update_ball()
            self.draw()
            time.sleep(0.1)

if __name__ == "__main__":
    game = Pong()
    game.play()