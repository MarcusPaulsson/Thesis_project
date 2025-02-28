import curses
import time

# Constants
WIN_HEIGHT = 20
WIN_WIDTH = 40
PADDLE_HEIGHT = 3
BALL_SYMBOL = 'O'
PADDLE_SYMBOL = '|'

def main(stdscr):
    # Clear and refresh the screen
    stdscr.clear()
    curses.curs_set(0)

    # Create a window
    win = curses.newwin(WIN_HEIGHT, WIN_WIDTH, 0, 0)
    win.keypad(1)
    win.timeout(100)

    # Initial positions
    left_paddle = (WIN_HEIGHT // 2) - 1
    right_paddle = (WIN_HEIGHT // 2) - 1
    ball_x = WIN_WIDTH // 2
    ball_y = WIN_HEIGHT // 2
    ball_dx = 1
    ball_dy = 1

    while True:
        win.clear()

        # Draw paddles
        for i in range(PADDLE_HEIGHT):
            win.addch(left_paddle + i, 1, PADDLE_SYMBOL)
            win.addch(right_paddle + i, WIN_WIDTH - 2, PADDLE_SYMBOL)

        # Draw ball
        win.addch(ball_y, ball_x, BALL_SYMBOL)

        # Refresh the window
        win.refresh()

        # Ball movement
        ball_x += ball_dx
        ball_y += ball_dy

        # Ball collision with top and bottom
        if ball_y <= 0 or ball_y >= WIN_HEIGHT - 1:
            ball_dy *= -1

        # Ball collision with paddles
        if ball_x == 2 and left_paddle <= ball_y < left_paddle + PADDLE_HEIGHT:
            ball_dx *= -1
        if ball_x == WIN_WIDTH - 3 and right_paddle <= ball_y < right_paddle + PADDLE_HEIGHT:
            ball_dx *= -1

        # Ball out of bounds
        if ball_x <= 0 or ball_x >= WIN_WIDTH - 1:
            ball_x, ball_y = WIN_WIDTH // 2, WIN_HEIGHT // 2  # Reset ball position

        # Paddle movement
        key = win.getch()
        if key == curses.KEY_UP and right_paddle > 0:
            right_paddle -= 1
        elif key == curses.KEY_DOWN and right_paddle < WIN_HEIGHT - PADDLE_HEIGHT:
            right_paddle += 1
        elif key == ord('w') and left_paddle > 0:
            left_paddle -= 1
        elif key == ord('s') and left_paddle < WIN_HEIGHT - PADDLE_HEIGHT:
            left_paddle += 1

        time.sleep(0.05)

if __name__ == "__main__":
    curses.wrapper(main)