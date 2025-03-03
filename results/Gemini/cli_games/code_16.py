import random
import time
import os

class PacManGame:
    def __init__(self, width=20, height=10):
        self.width = width
        self.height = height
        self.pacman_x = width // 2
        self.pacman_y = height // 2
        self.ghost_x = random.randint(1, width - 2)
        self.ghost_y = random.randint(1, height - 2)
        self.food = set()
        for x in range(1, width - 1):
            for y in range(1, height - 1):
                self.food.add((x, y))
        self.food.remove((self.pacman_x, self.pacman_y))
        self.score = 0
        self.game_over = False
        self.last_move = None

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
        grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]

        # Draw walls
        for x in range(self.width):
            grid[0][x] = '#'
            grid[self.height - 1][x] = '#'
        for y in range(self.height):
            grid[y][0] = '#'
            grid[y][self.width - 1] = '#'

        # Draw food
        for x, y in self.food:
            grid[y][x] = '.'

        # Draw Pac-Man
        grid[self.pacman_y][self.pacman_x] = 'P'

        # Draw Ghost
        grid[self.ghost_y][self.ghost_x] = 'G'

        # Print the grid
        for row in grid:
            print(''.join(row))

        print(f"Score: {self.score}")

    def move_pacman(self, direction):
        new_x, new_y = self.pacman_x, self.pacman_y

        if direction == 'w':  # Up
            new_y -= 1
        elif direction == 's':  # Down
            new_y += 1
        elif direction == 'a':  # Left
            new_x -= 1
        elif direction == 'd':  # Right
            new_x += 1
        else:
            return  # Invalid move

        if 0 < new_x < self.width - 1 and 0 < new_y < self.height - 1:
            self.pacman_x = new_x
            self.pacman_y = new_y
            self.last_move = direction

            if (self.pacman_x, self.pacman_y) in self.food:
                self.food.remove((self.pacman_x, self.pacman_y))
                self.score += 10

            if self.pacman_x == self.ghost_x and self.pacman_y == self.ghost_y:
                self.game_over = True


    def move_ghost(self):
        possible_moves = []
        if self.ghost_x > 1 and (self.ghost_x - 1, self.ghost_y) != (self.pacman_x, self.pacman_y):
            possible_moves.append('a')
        if self.ghost_x < self.width - 2 and (self.ghost_x + 1, self.ghost_y) != (self.pacman_x, self.pacman_y):
            possible_moves.append('d')
        if self.ghost_y > 1 and (self.ghost_x, self.ghost_y - 1) != (self.pacman_x, self.pacman_y):
            possible_moves.append('w')
        if self.ghost_y < self.height - 2 and (self.ghost_x, self.ghost_y + 1) != (self.pacman_x, self.pacman_y):
            possible_moves.append('s')

        if possible_moves:
            move = random.choice(possible_moves)

            new_x, new_y = self.ghost_x, self.ghost_y

            if move == 'w':
                new_y -= 1
            elif move == 's':
                new_y += 1
            elif move == 'a':
                new_x -= 1
            elif move == 'd':
                new_x += 1

            self.ghost_x = new_x
            self.ghost_y = new_y
            if self.pacman_x == self.ghost_x and self.pacman_y == self.ghost_y:
                self.game_over = True

    def run(self):
        while not self.game_over and self.food:
            self.display()
            move = input("Enter move (w/a/s/d): ").lower()
            self.move_pacman(move)
            self.move_ghost()
            time.sleep(0.2)

        self.display()
        if self.game_over:
            print("Game Over! Ghost caught you.")
        else:
            print("Congratulations! You ate all the food!")
        print(f"Final Score: {self.score}")

if __name__ == "__main__":
    game = PacManGame()
    game.run()