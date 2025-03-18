import time
import random
import os

class Pong:
    def __init__(self, width=60, height=20):
        self.width = width
        self.height = height
        self.ball_x = width // 2
        self.ball_y = height // 2
        self.ball_dx = random.choice([-1, 1])
        self.ball_dy = random.choice([-1, 1])
        self.paddle1_y = height // 2 - 2
        self.paddle2_y = height // 2 - 2
        self.paddle_length = 4
        self.score1 = 0
        self.score2 = 0
        self.running = True
        self.delay = 0.05 # Adjust for game speed

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw(self):
        self.clear_screen()
        # Create the game board
        board = [[' ' for _ in range(self.width)] for _ in range(self.height)]

        # Draw paddles
        for i in range(self.paddle_length):
            board[self.paddle1_y + i][0] = '|'
            board[self.paddle2_y + i][self.width - 1] = '|'

        # Draw ball
        board[self.ball_y][self.ball_x] = 'O'

        # Print the board
        for row in board:
            print(''.join(row))

        # Print the score
        print(f"Player 1: {self.score1}  Player 2: {self.score2}")

    def update(self):
        # Ball movement
        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy

        # Bounce off top and bottom
        if self.ball_y <= 0 or self.ball_y >= self.height - 1:
            self.ball_dy *= -1

        # Paddle collision
        if self.ball_x == 1 and self.paddle1_y <= self.ball_y <= self.paddle1_y + self.paddle_length - 1:
            self.ball_dx *= -1
        elif self.ball_x == self.width - 2 and self.paddle2_y <= self.ball_y <= self.paddle2_y + self.paddle_length - 1:
            self.ball_dx *= -1

        # Score and reset
        if self.ball_x <= 0:
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


    def move_paddle1(self, direction):
        if direction == "up" and self.paddle1_y > 0:
            self.paddle1_y -= 1
        elif direction == "down" and self.paddle1_y < self.height - self.paddle_length:
            self.paddle1_y += 1

    def move_paddle2(self, direction):
        if direction == "up" and self.paddle2_y > 0:
            self.paddle2_y -= 1
        elif direction == "down" and self.paddle2_y < self.height - self.paddle_length:
            self.paddle2_y += 1


    def play(self):
        while self.running:
            self.draw()
            self.update()

            # Get input (non-blocking)
            import select
            import sys
            if select.select([sys.stdin,], [], [], 0.0)[0]: # Check if stdin is ready to read
                action = sys.stdin.readline().strip() # Read input without blocking
                if action == "q":
                    self.running = False
                    break
                elif action == "w":
                    self.move_paddle1("up")
                elif action == "s":
                    self.move_paddle1("down")
                elif action == "o":
                    self.move_paddle2("up")
                elif action == "l":
                    self.move_paddle2("down")

            time.sleep(self.delay)

        print("Game Over!")
        print(f"Final Score: Player 1: {self.score1}  Player 2: {self.score2}")


if __name__ == "__main__":
    game = Pong()
    print("Welcome to Pong!")
    print("Controls:")
    print("Player 1: w (up), s (down)")
    print("Player 2: o (up), l (down)")
    print("Press q to quit")
    game.play()