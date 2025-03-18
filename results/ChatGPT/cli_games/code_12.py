import os
import sys
import time
import keyboard

# Constants
WIDTH = 40
HEIGHT = 20
PADDLE_HEIGHT = 4
BALL_CHAR = 'O'
PADDLE_CHAR = '|'
EMPTY_CHAR = ' '

# Game state
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = 1
ball_dy = 1
paddle_left_y = (HEIGHT // 2) - (PADDLE_HEIGHT // 2)
paddle_right_y = (HEIGHT // 2) - (PADDLE_HEIGHT // 2)

def draw():
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if x == 0 and paddle_left_y <= y < paddle_left_y + PADDLE_HEIGHT:
                print(PADDLE_CHAR, end='')
            elif x == WIDTH - 1 and paddle_right_y <= y < paddle_right_y + PADDLE_HEIGHT:
                print(PADDLE_CHAR, end='')
            elif x == ball_x and y == ball_y:
                print(BALL_CHAR, end='')
            else:
                print(EMPTY_CHAR, end='')
        print()
    print("Use 'w' and 's' to move left paddle, 'i' and 'k' to move right paddle. Press 'q' to quit.")

def update():
    global ball_x, ball_y, ball_dx, ball_dy, paddle_left_y, paddle_right_y
    
    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with top and bottom walls
    if ball_y <= 0 or ball_y >= HEIGHT - 1:
        ball_dy *= -1

    # Ball collision with paddles
    if ball_x == 0 and paddle_left_y <= ball_y < paddle_left_y + PADDLE_HEIGHT:
        ball_dx *= -1
    elif ball_x == WIDTH - 1 and paddle_right_y <= ball_y < paddle_right_y + PADDLE_HEIGHT:
        ball_dx *= -1

    # Reset ball if it goes out of bounds
    if ball_x < 0 or ball_x >= WIDTH:
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_dx = 1 if ball_dx > 0 else -1
        ball_dy = 1 if ball_dy > 0 else -1

def handle_input():
    global paddle_left_y, paddle_right_y
    if keyboard.is_pressed('w') and paddle_left_y > 0:
        paddle_left_y -= 1
    if keyboard.is_pressed('s') and paddle_left_y < HEIGHT - PADDLE_HEIGHT:
        paddle_left_y += 1
    if keyboard.is_pressed('i') and paddle_right_y > 0:
        paddle_right_y -= 1
    if keyboard.is_pressed('k') and paddle_right_y < HEIGHT - PADDLE_HEIGHT:
        paddle_right_y += 1
    if keyboard.is_pressed('q'):
        sys.exit()

def main():
    while True:
        handle_input()
        update()
        draw()
        time.sleep(0.1)

if __name__ == "__main__":
    main()