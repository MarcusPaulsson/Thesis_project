import curses
import random
import math

# Constants
WIDTH = 80
HEIGHT = 24
ASTEROID_COUNT = 5
ASTEROID_SYMBOL = '*'
SHIP_SYMBOL = 'A'

class Asteroid:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 1)
        self.y = random.randint(0, HEIGHT - 1)
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x <= 0 or self.x >= WIDTH - 1:
            self.dx *= -1
        if self.y <= 0 or self.y >= HEIGHT - 1:
            self.dy *= -1

class Ship:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.angle = 0

    def turn_left(self):
        self.angle -= 5

    def turn_right(self):
        self.angle += 5

    def move(self):
        rad = math.radians(self.angle)
        self.x += int(math.cos(rad))
        self.y += int(math.sin(rad))
        self.x %= WIDTH
        self.y %= HEIGHT

def draw_window(stdscr, ship, asteroids):
    stdscr.clear()
    stdscr.addstr(ship.y, ship.x, SHIP_SYMBOL)
    for asteroid in asteroids:
        stdscr.addstr(asteroid.y, asteroid.x, ASTEROID_SYMBOL)
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    ship = Ship()
    asteroids = [Asteroid() for _ in range(ASTEROID_COUNT)]

    while True:
        draw_window(stdscr, ship, asteroids)

        key = stdscr.getch()
        if key == curses.KEY_LEFT:
            ship.turn_left()
        elif key == curses.KEY_RIGHT:
            ship.turn_right()
        elif key == ord('w'):
            ship.move()
        elif key == ord('q'):
            break

        for asteroid in asteroids:
            asteroid.move()

curses.wrapper(main)