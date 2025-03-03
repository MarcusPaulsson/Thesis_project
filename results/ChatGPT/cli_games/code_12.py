import os
import time
import random
import sys
import threading

# Constants
WIDTH = 40
HEIGHT = 20
PADDLE_SIZE = 3
BALL_CHAR = 'O'
PADDLE_CHAR = '|'
EMPTY_CHAR = ' '

# Game state
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = 1
ball_dy = 1
left_paddle_y = HEIGHT // 2 - PADDLE_SIZE // 2
right_paddle_y = HEIGHT // 2 - PADDLE_SIZE // 2
running = True

def draw():
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if x == 0 and left_paddle_y <= y < left_paddle_y + PADDLE_SIZE:
                print(PADDLE_CHAR, end="")
            elif x == WIDTH - 1 and right_paddle_y <= y < right_paddle_y + PADDLE_SIZE:
                print(PADDLE_CHAR, end="")
            elif x == ball_x and y == ball_y:
                print(BALL_CHAR, end="")
            else:
                print(EMPTY_CHAR, end="")
        print()

def update_ball():
    global ball_x, ball_y, ball_dx, ball_dy, left_paddle_y, right_paddle_y

    while running:
        time.sleep(0.1)
        ball_x += ball_dx
        ball_y += ball_dy

        # Ball collision with top and bottom walls
        if ball_y <= 0 or ball_y >= HEIGHT - 1:
            ball_dy *= -1

        # Ball collision with paddles
        if ball_x == 0 and left_paddle_y <= ball_y < left_paddle_y + PADDLE_SIZE:
            ball_dx *= -1
        elif ball_x == WIDTH - 1 and right_paddle_y <= ball_y < right_paddle_y + PADDLE_SIZE:
            ball_dx *= -1

        # Ball out of bounds
        if ball_x < 0 or ball_x >= WIDTH:
            ball_x = WIDTH // 2
            ball_y = HEIGHT // 2
            ball_dx = random.choice([-1, 1])
            ball_dy = random.choice([-1, 1])

def move_paddle(paddle, direction):
    global left_paddle_y, right_paddle_y
    if paddle == 'left':
        if direction == 'up' and left_paddle_y > 0:
            left_paddle_y -= 1
        elif direction == 'down' and left_paddle_y < HEIGHT - PADDLE_SIZE:
            left_paddle_y += 1
    elif paddle == 'right':
        if direction == 'up' and right_paddle_y > 0:
            right_paddle_y -= 1
        elif direction == 'down' and right_paddle_y < HEIGHT - PADDLE_SIZE:
            right_paddle_y += 1

def input_listener():
    global running
    while running:
        command = input()
        if command == 'w':
            move_paddle('left', 'up')
        elif command == 's':
            move_paddle('left', 'down')
        elif command == 'i':
            move_paddle('right', 'up')
        elif command == 'k':
            move_paddle('right', 'down')
        elif command == 'q':
            running = False

if __name__ == "__main__":
    # Start the ball update thread
    ball_thread = threading.Thread(target=update_ball)
    ball_thread.start()

    # Start the input listener
    input_listener()

    # Wait for the ball thread to finish
    ball_thread.join()
    print("Game Over!")