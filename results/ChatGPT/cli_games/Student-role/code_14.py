import random
import os
import sys
import time
import threading

class AsteroidGame:
    def __init__(self, width=40, height=20, num_asteroids=5):
        self.width = width
        self.height = height
        self.num_asteroids = num_asteroids
        self.player_pos = [self.width // 2, self.height - 1]
        self.asteroids = self.generate_asteroids()
        self.score = 0
        self.game_over = False

    def generate_asteroids(self):
        return [[random.randint(0, self.width - 1), 0] for _ in range(self.num_asteroids)]

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(self.height):
            for x in range(self.width):
                if [x, y] == self.player_pos:
                    print('^', end='')
                elif [x, y] in self.asteroids:
                    print('O', end='')
                else:
                    print(' ', end='')
            print()
        print(f'Score: {self.score}')

    def move_player(self, direction):
        if direction == 'left' and self.player_pos[0] > 0:
            self.player_pos[0] -= 1
        elif direction == 'right' and self.player_pos[0] < self.width - 1:
            self.player_pos[0] += 1

    def update_asteroids(self):
        new_asteroids = []
        for asteroid in self.asteroids:
            asteroid[1] += 1
            if asteroid[1] < self.height:
                new_asteroids.append(asteroid)
            else:
                self.score += 1  # Player dodged an asteroid
        self.asteroids = new_asteroids
        if any(asteroid == self.player_pos for asteroid in self.asteroids):
            self.game_over = True

    def run(self):
        def input_thread():
            while not self.game_over:
                command = input()
                if command == 'a':
                    self.move_player('left')
                elif command == 'd':
                    self.move_player('right')

        threading.Thread(target=input_thread, daemon=True).start()

        while not self.game_over:
            self.display()
            self.update_asteroids()
            time.sleep(0.2)

        print("Game Over! Your score was:", self.score)

if __name__ == "__main__":
    game = AsteroidGame()
    game.run()