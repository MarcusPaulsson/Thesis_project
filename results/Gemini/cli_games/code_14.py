import random
import os
import sys
import time
import threading
import keyboard

# Game constants
WIDTH = 40
HEIGHT = 20
NUM_ASTEROIDS = 5
SHIP_ICON = '>'
ASTEROID_ICON = '*'
BULLET_ICON = '|'
SHIP_START_X = WIDTH // 2
SHIP_START_Y = HEIGHT - 1

class Game:
    def __init__(self):
        self.ship_x = SHIP_START_X
        self.ship_y = SHIP_START_Y
        self.asteroids = self.create_asteroids()
        self.bullets = []
        self.score = 0
        self.game_over = False

    def create_asteroids(self):
        return [(random.randint(0, WIDTH-1), random.randint(0, HEIGHT-5)) for _ in range(NUM_ASTEROIDS)]

    def draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if (x, y) == (self.ship_x, self.ship_y):
                    print(SHIP_ICON, end='')
                elif (x, y) in self.asteroids:
                    print(ASTEROID_ICON, end='')
                elif (x, y) in self.bullets:
                    print(BULLET_ICON, end='')
                else:
                    print(' ', end='')
            print()
        print(f'Score: {self.score}')

    def move_ship(self, dx):
        self.ship_x = max(0, min(WIDTH - 1, self.ship_x + dx))

    def shoot(self):
        self.bullets.append((self.ship_x, self.ship_y - 1))

    def update_bullets(self):
        new_bullets = []
        for bullet in self.bullets:
            if bullet[1] > 0:
                new_bullets.append((bullet[0], bullet[1] - 1))
        self.bullets = new_bullets

    def check_collisions(self):
        for bullet in self.bullets:
            if bullet in self.asteroids:
                self.asteroids.remove(bullet)
                self.score += 1

    def run(self):
        while not self.game_over:
            self.draw()
            self.update_bullets()
            self.check_collisions()
            if not self.asteroids:
                print("You destroyed all the asteroids! You win!")
                self.game_over = True
            time.sleep(0.1)

def control_thread(game):
    while not game.game_over:
        if keyboard.is_pressed('a'):
            game.move_ship(-1)
        elif keyboard.is_pressed('d'):
            game.move_ship(1)
        elif keyboard.is_pressed('space'):
            game.shoot()
        time.sleep(0.1)

if __name__ == '__main__':
    game = Game()
    threading.Thread(target=control_thread, args=(game,), daemon=True).start()
    game.run()