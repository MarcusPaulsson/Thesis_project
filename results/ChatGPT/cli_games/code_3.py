import curses
import random

# Set up the window
stdscr = curses.initscr()
curses.curs_set(0)
sh, sw = stdscr.getmaxyx()  # get height and width of window
w = curses.newwin(sh, sw, 0, 0)  # create a new window
w.keypad(1)
w.timeout(100)  # refresh every 100 milliseconds

# Initial snake and food positions
snk_x = sw // 4
snk_y = sh // 2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x - 1],
    [snk_y, snk_x - 2]
]
food = [sh // 2, sw // 2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

# Initial game settings
key = curses.KEY_RIGHT  # initial direction
score = 0

while True:
    next_key = w.getch()  # get user input
    key = key if next_key == -1 else next_key  # use new key if it's pressed

    # Calculate new head position
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    # Insert new head into snake
    snake.insert(0, new_head)

    # Check if snake has eaten the food
    if snake[0] == food:
        score += 1
        food = None
        while food is None:
            nf = [
                random.randint(1, sh - 1),  # y
                random.randint(1, sw - 1)   # x
            ]
            food = nf if nf not in snake else None
        w.addch(int(food[0]), int(food[1]), curses.ACS_PI)
    else:
        # Remove the last segment of the snake
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')

    # Check for collision with borders or self
    if (snake[0][0] in [0, sh] or
        snake[0][1] in [0, sw] or
        snake[0] in snake[1:]):
        curses.endwin()
        print(f"Game Over! Your score was: {score}")
        break

    # Draw the snake
    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)