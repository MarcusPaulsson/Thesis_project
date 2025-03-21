import os
import time
import random
import sys
import threading

class PongGame:
    def __init__(self, width=40, height=20):
        self.width = width
        self.height = height
        self.paddle_height = 3
        self.ball_x = width // 2
        self.ball_y = height // 2
        self.ball_dx = random.choice([-1, 1])
        self.ball_dy = random.choice([-1, 1])
        self.paddle1_y = height // 2 - self.paddle_height // 2
        self.paddle2_y = height // 2 - self.paddle_height // 2
        self.score1 = 0
        self.score2 = 0
        self.running = True

    def draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(self.height):
            for x in range(self.width):
                if x == 0 and self.paddle1_y <= y < self.paddle1_y + self.paddle_height:
                    print('|', end='')
                elif x == self.width - 1 and self.paddle2_y <= y < self.paddle2_y + self.paddle_height:
                    print('|', end='')
                elif x == self.ball_x and y == self.ball_y:
                    print('O', end='')
                else:
                    print(' ', end='')
            print()
        print(f'Score - Player 1: {self.score1} | Player 2: {self.score2}')

    def update_ball(self):
        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy

        if self.ball_y <= 0 or self.ball_y >= self.height - 1:
            self.ball_dy *= -1

        if self.ball_x == 0:
            if self.paddle1_y <= self.ball_y < self.paddle1_y + self.paddle_height:
                self.ball_dx *= -1
            else:
                self.score2 += 1
                self.reset_ball()

        if self.ball_x == self.width - 1:
            if self.paddle2_y <= self.ball_y < self.paddle2_y + self.paddle_height:
                self.ball_dx *= -1
            else:
                self.score1 += 1
                self.reset_ball()

    def reset_ball(self):
        self.ball_x = self.width // 2
        self.ball_y = self.height // 2
        self.ball_dx = random.choice([-1, 1])
        self.ball_dy = random.choice([-1, 1])

    def move_paddle(self, paddle, direction):
        if paddle == 1:
            if direction == 'up' and self.paddle1_y > 0:
                self.paddle1_y -= 1
            elif direction == 'down' and self.paddle1_y < self.height - self.paddle_height:
                self.paddle1_y += 1
        elif paddle == 2:
            if direction == 'up' and self.paddle2_y > 0:
                self.paddle2_y -= 1
            elif direction == 'down' and self.paddle2_y < self.height - self.paddle_height:
                self.paddle2_y += 1

    def game_loop(self):
        while self.running:
            self.update_ball()
            self.draw()
            time.sleep(0.1)

    def input_thread(self):
        while self.running:
            command = input()
            if command == 'w':
                self.move_paddle(1, 'up')
            elif command == 's':
                self.move_paddle(1, 'down')
            elif command == 'i':
                self.move_paddle(2, 'up')
            elif command == 'k':
                self.move_paddle(2, 'down')
            elif command == 'exit':
                self.running = False
                break

    def start(self):
        threading.Thread(target=self.input_thread, daemon=True).start()
        self.game_loop()

if __name__ == '__main__':
    game = PongGame()
    game.start()