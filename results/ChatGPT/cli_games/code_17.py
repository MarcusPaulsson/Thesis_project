import random
import time
import sys
import threading

class DinosaurRunner:
    def __init__(self):
        self.dino_pos = 0
        self.obstacles = []
        self.score = 0
        self.game_over = False
        self.obstacle_interval = 2  # seconds
        self.game_speed = 0.1  # seconds (delay between game updates)

    def start(self):
        print("Welcome to Dinosaur Runner!")
        print("Press 'j' to jump and 'q' to quit.")
        threading.Thread(target=self.spawn_obstacles).start()
        self.run_game()

    def spawn_obstacles(self):
        while not self.game_over:
            obstacle_pos = random.randint(1, 10)
            self.obstacles.append(obstacle_pos)
            time.sleep(self.obstacle_interval)

    def run_game(self):
        while not self.game_over:
            self.clear_screen()
            self.display_game()
            self.handle_input()
            self.check_collision()
            self.score += 1
            time.sleep(self.game_speed)

    def display_game(self):
        print(f"Score: {self.score}")
        print(" " * self.dino_pos + "D")
        for i in range(1, 11):
            if i in self.obstacles:
                print(" " * i + "X")
            else:
                print(" " * i + " ")
    
    def handle_input(self):
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            input_char = sys.stdin.read(1)
            if input_char == 'j':
                self.jump()
            elif input_char == 'q':
                self.game_over = True

    def jump(self):
        print("Jumping!")
        time.sleep(0.5)  # simulate jump time

    def check_collision(self):
        if self.dino_pos in self.obstacles:
            self.game_over = True
            print("Game Over! Final Score:", self.score)

    def clear_screen(self):
        print("\033[H\033[J", end="")

if __name__ == "__main__":
    game = DinosaurRunner()
    game.start()