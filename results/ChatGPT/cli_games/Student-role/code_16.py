import random
import os
import time
import keyboard

class PacManGame:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.pacman_pos = [1, 1]
        self.food_pos = [random.randint(0, height - 1), random.randint(0, width - 1)]
        self.score = 0
        self.game_over = False
        self.direction = 'RIGHT'
        self.board = self.create_board()

    def create_board(self):
        return [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def update_board(self):
        self.board = self.create_board()
        self.board[self.pacman_pos[0]][self.pacman_pos[1]] = 'P'
        self.board[self.food_pos[0]][self.food_pos[1]] = 'F'

    def display_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.board:
            print('|' + ''.join(row) + '|')
        print(f'Score: {self.score}')

    def move(self):
        if self.direction == 'UP':
            self.pacman_pos[0] -= 1
        elif self.direction == 'DOWN':
            self.pacman_pos[0] += 1
        elif self.direction == 'LEFT':
            self.pacman_pos[1] -= 1
        elif self.direction == 'RIGHT':
            self.pacman_pos[1] += 1

        # Check for boundaries
        self.pacman_pos[0] = max(0, min(self.height - 1, self.pacman_pos[0]))
        self.pacman_pos[1] = max(0, min(self.width - 1, self.pacman_pos[1]))

        # Check for food
        if self.pacman_pos == self.food_pos:
            self.score += 1
            self.food_pos = [random.randint(0, self.height - 1), random.randint(0, self.width - 1)]

    def change_direction(self, new_direction):
        self.direction = new_direction

    def run(self):
        print("Control Pac-Man with WASD (W=Up, A=Left, S=Down, D=Right). Press Q to quit.")
        while not self.game_over:
            self.update_board()
            self.display_board()
            self.move()
            if keyboard.is_pressed('w'):
                self.change_direction('UP')
            elif keyboard.is_pressed('s'):
                self.change_direction('DOWN')
            elif keyboard.is_pressed('a'):
                self.change_direction('LEFT')
            elif keyboard.is_pressed('d'):
                self.change_direction('RIGHT')
            elif keyboard.is_pressed('q'):
                self.game_over = True

            time.sleep(0.1)

if __name__ == "__main__":
    game = PacManGame()
    game.run()