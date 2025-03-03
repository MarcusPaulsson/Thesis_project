import time
import random
import sys
import threading

class DinosaurRunner:
    def __init__(self):
        self.score = 0
        self.is_running = True
        self.obstacles = []
        self.dino_position = 0
        self.game_speed = 1

    def start_game(self):
        print("Welcome to Dinosaur Runner!")
        print("Press 'j' to jump over obstacles, or 'q' to quit.")
        print("Good luck!\n")
        
        # Start obstacle generation in a separate thread
        obstacle_thread = threading.Thread(target=self.generate_obstacles)
        obstacle_thread.start()
        
        # Main game loop
        while self.is_running:
            self.update_score()
            self.display_game_state()
            time.sleep(self.game_speed)
            self.check_collision()

        print("Game Over! Your final score is:", self.score)

    def generate_obstacles(self):
        while self.is_running:
            self.obstacles.append(random.randint(1, 5))  # Random height of obstacles
            time.sleep(random.uniform(1, 3))  # Random interval for obstacles

    def update_score(self):
        self.score += 1

    def display_game_state(self):
        print(f"Score: {self.score}")
        print("Dino " + " " * self.dino_position + "O")
        print("Obstacles: " + " ".join(['#' if h <= 1 else ' ' for h in self.obstacles]))
        
        if self.obstacles:
            self.obstacles = [h - 1 for h in self.obstacles if h - 1 > 0]

    def check_collision(self):
        if self.obstacles and self.obstacles[0] == 0:
            self.is_running = False

    def jump(self):
        print("Jumping!")
        self.dino_position = 1  # Move dino up
        time.sleep(0.5)  # Simulate jump duration
        self.dino_position = 0  # Move dino back down

    def quit_game(self):
        self.is_running = False

def main():
    game = DinosaurRunner()
    threading.Thread(target=game.start_game).start()
    
    while game.is_running:
        user_input = input()
        if user_input == 'j':
            game.jump()
        elif user_input == 'q':
            game.quit_game()

if __name__ == "__main__":
    main()