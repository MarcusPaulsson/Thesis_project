import random
import time
import sys
import threading

class DinosaurRunner:
    def __init__(self):
        self.game_over = False
        self.score = 0
        self.dino_pos = 0
        self.obstacles = []
        self.is_jumping = False
        self.jump_height = 3
        self.gravity = 1
        self.jump_count = 0
        self.obstacle_timer = threading.Timer(1, self.spawn_obstacle)

    def spawn_obstacle(self):
        if not self.game_over:
            self.obstacles.append(random.randint(5, 10))  # Random height for the obstacle
            self.obstacle_timer = threading.Timer(1, self.spawn_obstacle)
            self.obstacle_timer.start()

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_count = self.jump_height
            print("Jump!")

    def update(self):
        if self.is_jumping:
            if self.jump_count >= 0:
                print(f"Dino at height: {self.jump_count}")
                self.jump_count -= self.gravity
            else:
                self.is_jumping = False
                print("Dino falls back down.")

        for obstacle in self.obstacles:
            if obstacle <= self.dino_pos:
                print(f"Obstacle at height {obstacle}!")
                if self.is_jumping and self.jump_height > obstacle:
                    print("Jumped over the obstacle!")
                    self.score += 1
                else:
                    self.game_over = True
                    print("Game Over!")
                    self.obstacle_timer.cancel()

    def play(self):
        print("Starting Dinosaur Runner... Press 'j' to jump.")
        self.spawn_obstacle()
        while not self.game_over:
            command = input()
            if command == 'j':
                self.jump()
            self.update()
            time.sleep(0.5)
        print(f"Final Score: {self.score}")

if __name__ == "__main__":
    game = DinosaurRunner()
    game.play()