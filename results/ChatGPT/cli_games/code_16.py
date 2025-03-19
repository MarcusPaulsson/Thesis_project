import random
import os
import time

class PacMan:
    def __init__(self, width=10, height=10, num_ghosts=2):
        self.width = width
        self.height = height
        self.num_ghosts = num_ghosts
        self.pacman_pos = [0, 0]
        self.ghosts = []
        self.score = 0
        self.map = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        self.food_count = 0
        self.game_over = False

        self.initialize_game()

    def initialize_game(self):
        for _ in range(self.num_ghosts):
            ghost_pos = self.random_position()
            while ghost_pos == self.pacman_pos:
                ghost_pos = self.random_position()
            self.ghosts.append(ghost_pos)

        for _ in range(self.width * self.height // 3):
            food_pos = self.random_position()
            while food_pos == self.pacman_pos or food_pos in self.ghosts:
                food_pos = self.random_position()
            self.map[food_pos[0]][food_pos[1]] = '.'
            self.food_count += 1

    def random_position(self):
        return [random.randint(0, self.height - 1), random.randint(0, self.width - 1)]

    def display_map(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for r in range(self.height):
            for c in range(self.width):
                if [r, c] == self.pacman_pos:
                    print('P', end=' ')
                elif [r, c] in self.ghosts:
                    print('G', end=' ')
                else:
                    print(self.map[r][c], end=' ')
            print()
        print(f"Score: {self.score}")

    def move_pacman(self, direction):
        if direction == 'w' and self.pacman_pos[0] > 0:
            self.pacman_pos[0] -= 1
        elif direction == 's' and self.pacman_pos[0] < self.height - 1:
            self.pacman_pos[0] += 1
        elif direction == 'a' and self.pacman_pos[1] > 0:
            self.pacman_pos[1] -= 1
        elif direction == 'd' and self.pacman_pos[1] < self.width - 1:
            self.pacman_pos[1] += 1

        self.check_collision()

    def check_collision(self):
        if self.map[self.pacman_pos[0]][self.pacman_pos[1]] == '.':
            self.score += 1
            self.map[self.pacman_pos[0]][self.pacman_pos[1]] = ' '
            self.food_count -= 1

        if self.pacman_pos in self.ghosts:
            self.game_over = True

    def move_ghosts(self):
        for i in range(len(self.ghosts)):
            move = random.choice([[0, 1], [0, -1], [1, 0], [-1, 0]])
            new_pos = [self.ghosts[i][0] + move[0], self.ghosts[i][1] + move[1]]
            if 0 <= new_pos[0] < self.height and 0 <= new_pos[1] < self.width:
                self.ghosts[i] = new_pos

    def play(self):
        while not self.game_over and self.food_count > 0:
            self.display_map()
            direction = input("Move (w/a/s/d): ").strip().lower()
            self.move_pacman(direction)
            self.move_ghosts()
            time.sleep(0.5)

        if self.game_over:
            print("Game Over! Final Score:", self.score)
        else:
            print("You ate all the food! Final Score:", self.score)

if __name__ == "__main__":
    game = PacMan()
    game.play()