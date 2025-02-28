import curses
import time

# Constants
WINDOW_HEIGHT = 20
WINDOW_WIDTH = 40
PADDLE_HEIGHT = 3
PADDLE_WIDTH = 1
BALL_SIZE = 1

# Ball and paddle positions
ball_x = WINDOW_WIDTH // 2
ball_y = WINDOW_HEIGHT // 2
ball_dx = 1
ball_dy = 1

left_paddle_y = (WINDOW_HEIGHT // 2) - (PADDLE_HEIGHT // 2)
right_paddle_y = (WINDOW_HEIGHT // 2) - (PADDLE_HEIGHT // 2)

def draw(window):
    window.clear()
    
    # Draw paddles
    for i in range(PADDLE_HEIGHT):
        window.addch(left_paddle_y + i, 1, '|')
        window.addch(right_paddle_y + i, WINDOW_WIDTH - 2, '|')
    
    # Draw ball
    window.addch(ball_y, ball_x, 'O')
    
    window.refresh()

def update_ball():
    global ball_x, ball_y, ball_dx, ball_dy

    # Update ball position
    ball_x += ball_dx
    ball_y += ball_dy

    # Bounce off top and bottom walls
    if ball_y <= 0 or ball_y >= WINDOW_HEIGHT - 1:
        ball_dy *= -1

    # Bounce off paddles
    if ball_x == 2 and left_paddle_y <= ball_y < left_paddle_y + PADDLE_HEIGHT:
        ball_dx *= -1
    elif ball_x == WINDOW_WIDTH - 3 and right_paddle_y <= ball_y < right_paddle_y + PADDLE_HEIGHT:
        ball_dx *= -1

    # Reset ball if it goes out of bounds
    if ball_x <= 0 or ball_x >= WINDOW_WIDTH - 1:
        ball_x = WINDOW_WIDTH // 2
        ball_y = WINDOW_HEIGHT // 2
        ball_dx *= -1

def main(stdscr):
    global left_paddle_y, right_paddle_y

    # Set up curses
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    while True:
        draw(stdscr)
        update_ball()

        key = stdscr.getch()

        # Move left paddle
        if key == curses.KEY_UP and left_paddle_y > 0:
            left_paddle_y -= 1
        elif key == curses.KEY_DOWN and left_paddle_y < WINDOW_HEIGHT - PADDLE_HEIGHT:
            left_paddle_y += 1

        # Move right paddle
        if key == ord('w') and right_paddle_y > 0:
            right_paddle_y -= 1
        elif key == ord('s') and right_paddle_y < WINDOW_HEIGHT - PADDLE_HEIGHT:
            right_paddle_y += 1

        time.sleep(0.01)

if __name__ == "__main__":
    curses.wrapper(main)