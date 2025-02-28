import curses
from random import randint

# Setting up the window
stdscr = curses.initscr()
curses.curs_set(0)
sh, sw = stdscr.getmaxyx()  # height and width of window
w = curses.newwin(sh, sw, 0, 0)  # create a new window
w.keypad(1)  # enable keypad input
w.timeout(100)  # refresh every 100 milliseconds

# Initializing the snake and food
snk_x = sw // 4  # starting x coordinate
snk_y = sh // 2  # starting y coordinate
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x - 1],
    [snk_y, snk_x - 2]
]
food = [sh // 2, sw // 2]  # food position
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)  # place food on the window

key = curses.KEY_RIGHT  # initial direction

while True:
    next_key = w.getch()  # get user input
    key = key if next_key == -1 else next_key  # update direction if input is available

    # Calculate new head of the snake
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    # Insert new head
    snake.insert(0, new_head)

    # Check if snake has eaten the food
    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                randint(1, sh - 1),
                randint(1, sw - 1)
            ]
            food = nf if nf not in snake else None
        w.addch(int(food[0]), int(food[1]), curses.ACS_PI)  # place new food
    else:
        # Remove the last segment of snake
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')  # clear the tail

    # Game Over conditions
    if (snake[0][0] in [0, sh]) or (snake[0][1] in [0, sw]) or (snake[0] in snake[1:]):
        curses.endwin()
        quit()

    # Drawing the snake
    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)  # draw the head