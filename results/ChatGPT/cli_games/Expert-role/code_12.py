import os
import time
import sys
import random
import keyboard

class Pong:
    def __init__(self):
        self.width = 40
        self.height = 20
        self.ball_x = self.width // 2
        self.ball_y = self.height // 2
        self.ball_dx = random.choice([-1, 1])
        self.ball_dy = random.choice([-1, 1])
        self.paddle1_y = self.height // 2
        self.paddle2_y = self.height // 2
        self.paddle_height = 4
        self.score1 = 0
        self.score2 = 0
        self.running = True

    def draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(self.height):
            for x in range(self.width):
                if x == 0:
                    print('|', end='')
                elif x == self.width - 1:
                    print('|', end='')
                elif (x == self.ball_x and y == self.ball_y):
                    print('O', end='')
                elif (x == 1 and self.paddle1_y <= y < self.paddle1_y + self.paddle_height):
                    print('#', end='')
                elif (x == self.width - 2 and self.paddle2_y <= y < self.paddle2_y + self.paddle_height):
                    print('#', end='')
                else:
                    print(' ', end='')
            print()
        print(f'Score: Player 1: {self.score1} | Player 2: {self.score2}')

    def update(self):
        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy

        if self.ball_y <= 0 or self.ball_y >= self.height - 1:
            self.ball_dy *= -1
        
        if self.ball_x == 1 and self.paddle1_y <= self.ball_y < self.paddle1_y + self.paddle_height:
            self.ball_dx *= -1
        elif self.ball_x == self.width - 2 and self.paddle2_y <= self.ball_y < self.paddle2_y + self.paddle_height:
            self.ball_dx *= -1
        elif self.ball_x <= 0:
            self.score2 += 1
            self.reset_ball()
        elif self.ball_x >= self.width - 1:
            self.score1 += 1
            self.reset_ball()

    def reset_ball(self):
        self.ball_x = self.width // 2
        self.ball_y = self.height // 2
        self.ball_dx = random.choice([-1, 1])
        self.ball_dy = random.choice([-1, 1])

    def move_paddle(self, paddle, direction):
        if paddle == 1 and self.paddle1_y > 0 and direction == 'up':
            self.paddle1_y -= 1
        elif paddle == 1 and self.paddle1_y < self.height - self.paddle_height and direction == 'down':
            self.paddle1_y += 1
        elif paddle == 2 and self.paddle2_y > 0 and direction == 'up':
            self.paddle2_y -= 1
        elif paddle == 2 and self.paddle2_y < self.height - self.paddle_height and direction == 'down':
            self.paddle2_y += 1

    def run(self):
        print("Controls: Player 1 (W/S), Player 2 (I/K)")
        while self.running:
            if keyboard.is_pressed('w'):
                self.move_paddle(1, 'up')
            if keyboard.is_pressed('s'):
                self.move_paddle(1, 'down')
            if keyboard.is_pressed('i'):
                self.move_paddle(2, 'up')
            if keyboard.is_pressed('k'):
                self.move_paddle(2, 'down')

            self.update()
            self.draw()
            time.sleep(0.1)

if __name__ == "__main__":
    pong_game = Pong()
    try:
        pong_game.run()
    except KeyboardInterrupt:
        print("Game exited.")
        sys.exit()