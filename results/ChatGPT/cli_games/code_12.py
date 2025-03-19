import os
import time
import random
import sys

class Pong:
    def __init__(self, width=40, height=20):
        self.width = width
        self.height = height
        self.paddle_height = 3
        self.ball = [width // 2, height // 2]
        self.ball_dir = [random.choice([-1, 1]), random.choice([-1, 1])]
        self.paddle1 = height // 2 - self.paddle_height // 2
        self.paddle2 = height // 2 - self.paddle_height // 2
        self.score1 = 0
        self.score2 = 0

    def draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(self.height):
            for x in range(self.width):
                if x == 0 and self.paddle1 <= y < self.paddle1 + self.paddle_height:
                    print('|', end='')
                elif x == self.width - 1 and self.paddle2 <= y < self.paddle2 + self.paddle_height:
                    print('|', end='')
                elif [x, y] == self.ball:
                    print('O', end='')
                else:
                    print(' ', end='')
            print()
        print(f'Score: Player 1: {self.score1} | Player 2: {self.score2}')

    def update_ball(self):
        self.ball[0] += self.ball_dir[0]
        self.ball[1] += self.ball_dir[1]

        if self.ball[1] <= 0 or self.ball[1] >= self.height - 1:
            self.ball_dir[1] *= -1

        if self.ball[0] == 0:
            self.score2 += 1
            self.reset_ball()
        elif self.ball[0] == self.width - 1:
            self.score1 += 1
            self.reset_ball()

        if (self.ball[0] == 0 and self.paddle1 <= self.ball[1] < self.paddle1 + self.paddle_height) or \
           (self.ball[0] == self.width - 1 and self.paddle2 <= self.ball[1] < self.paddle2 + self.paddle_height):
            self.ball_dir[0] *= -1

    def reset_ball(self):
        self.ball = [self.width // 2, self.height // 2]
        self.ball_dir = [random.choice([-1, 1]), random.choice([-1, 1])]

    def move_paddle(self, player, direction):
        if player == 1:
            if direction == 'up' and self.paddle1 > 0:
                self.paddle1 -= 1
            elif direction == 'down' and self.paddle1 < self.height - self.paddle_height:
                self.paddle1 += 1
        else:
            if direction == 'up' and self.paddle2 > 0:
                self.paddle2 -= 1
            elif direction == 'down' and self.paddle2 < self.height - self.paddle_height:
                self.paddle2 += 1

    def play(self):
        while True:
            self.draw()
            self.update_ball()
            time.sleep(0.1)

            if self.score1 >= 5 or self.score2 >= 5:
                print("Game Over!")
                break

            # Simple input simulation
            move = random.choice(['up', 'down', None])
            if move:
                self.move_paddle(1, move)
            move = random.choice(['up', 'down', None])
            if move:
                self.move_paddle(2, move)

if __name__ == "__main__":
    game = Pong()
    game.play()