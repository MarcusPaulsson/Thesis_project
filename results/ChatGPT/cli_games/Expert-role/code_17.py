import random
import time
import threading
import os
import sys

class DinosaurRunner:
    def __init__(self):
        self.score = 0
        self.is_running = True
        self.dino_pos = 5
        self.obstacle_pos = 20
        self.obstacle_char = 'O'
        self.dino_char = 'D'
        self.width = 30
        self.height = 10

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw_game(self):
        self.clear_screen()
        for i in range(self.height):
            if i == self.height - 1:
                print('Score: {}'.format(self.score))
            else:
                line = [' '] * self.width
                if self.obstacle_pos < self.width:
                    line[self.obstacle_pos] = self.obstacle_char
                line[self.dino_pos] = self.dino_char
                print(''.join(line))

    def move_obstacle(self):
        while self.is_running:
            time.sleep(0.1)
            self.obstacle_pos -= 1
            if self.obstacle_pos < 0:
                self.obstacle_pos = self.width - 1
                self.score += 1

    def jump(self):
        original_pos = self.dino_pos
        self.dino_pos -= 1
        self.draw_game()
        time.sleep(0.3)
        self.dino_pos = original_pos

    def check_collision(self):
        return self.dino_pos == self.obstacle_pos

    def run(self):
        threading.Thread(target=self.move_obstacle, daemon=True).start()
        while self.is_running:
            self.draw_game()
            action = input("Press 'j' to jump: ")
            if action.lower() == 'j':
                self.jump()
            if self.check_collision():
                self.is_running = False
                print("Game Over! Final Score: {}".format(self.score))

if __name__ == "__main__":
    game = DinosaurRunner()
    game.run()