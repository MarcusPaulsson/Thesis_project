import random
import sys
import os
import time
import math

class AsteroidGame:
    def __init__(self, width=40, height=20, num_asteroids=5):
        self.width = width
        self.height = height
        self.player_pos = [width // 2, height // 2]
        self.asteroids = self._create_asteroids(num_asteroids)
        self.score = 0
        self.game_over = False

    def _create_asteroids(self, num_asteroids):
        return [[random.randint(0, self.width - 1), random.randint(0, self.height - 1)] for _ in range(num_asteroids)]

    def _draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(self.height):
            for x in range(self.width):
                if [x, y] == self.player_pos:
                    print("P", end="")
                elif [x, y] in self.asteroids:
                    print("A", end="")
                else:
                    print(" ", end="")
            print()
        print(f"Score: {self.score}")

    def _move_asteroids(self):
        for asteroid in self.asteroids:
            asteroid[1] += 1
            if asteroid[1] >= self.height:
                asteroid[0] = random.randint(0, self.width - 1)
                asteroid[1] = 0
                self.score += 1

    def _check_collision(self):
        if self.player_pos in self.asteroids:
            self.game_over = True

    def _get_input(self):
        if os.name == 'nt':
            import msvcrt
            if msvcrt.kbhit():
                return msvcrt.getch().decode()
        else:
            import select
            import sys
            if select.select([sys.stdin], [], [], 0)[0]:
                return sys.stdin.read(1)
        return None

    def run(self):
        while not self.game_over:
            self._draw()
            self._move_asteroids()
            self._check_collision()
            user_input = self._get_input()
            if user_input:
                if user_input == 'a' and self.player_pos[0] > 0:
                    self.player_pos[0] -= 1
                elif user_input == 'd' and self.player_pos[0] < self.width - 1:
                    self.player_pos[0] += 1
            time.sleep(0.1)

        print("Game Over! Your score was:", self.score)

if __name__ == "__main__":
    game = AsteroidGame()
    game.run()