import random
import time
import os

class PacManGame:
    def __init__(self, width=15, height=10):
        self.width = width
        self.height = height
        self.board = [[' ' for _ in range(width)] for _ in range(height)]
        self.pacman_x = width // 2
        self.pacman_y = height // 2
        self.ghost_x = 1
        self.ghost_y = 1
        self.food_count = 0
        self.game_over = False
        self.score = 0

        # Initialize food
        for y in range(height):
            for x in range(width):
                if random.random() < 0.8 and (x != self.pacman_x or y != self.pacman_y) and (x != self.ghost_x or y != self.ghost_y):
                    self.board[y][x] = '.'
                    self.food_count += 1

        # Place Pac-Man and Ghost
        self.board[self.pacman_y][self.pacman_x] = 'P'
        self.board[self.ghost_y][self.ghost_x] = 'G'

    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        print("-" * (self.width + 2))
        for row in self.board:
            print("|" + "".join(row) + "|")
        print("-" * (self.width + 2))
        print(f"Score: {self.score}, Food Remaining: {self.food_count}")
        

    def move_pacman(self, direction):
        new_x = self.pacman_x
        new_y = self.pacman_y

        if direction == 'w':  # Up
            new_y -= 1
        elif direction == 's':  # Down
            new_y += 1
        elif direction == 'a':  # Left
            new_x -= 1
        elif direction == 'd':  # Right
            new_x += 1
        else:
            print("Invalid direction. Use w, a, s, d.")
            return

        if 0 <= new_x < self.width and 0 <= new_y < self.height:
            if self.board[new_y][new_x] == '.':
                self.score += 10
                self.food_count -= 1
            elif self.board[new_y][new_x] == 'G':
                self.game_over = True
                return

            self.board[self.pacman_y][self.pacman_x] = ' '
            self.pacman_x = new_x
            self.pacman_y = new_y
            self.board[self.pacman_y][self.pacman_x] = 'P'

    def move_ghost(self):
        possible_moves = []
        if self.ghost_x > 0:
            possible_moves.append('a')
        if self.ghost_x < self.width - 1:
            possible_moves.append('d')
        if self.ghost_y > 0:
            possible_moves.append('w')
        if self.ghost_y < self.height - 1:
            possible_moves.append('s')

        if not possible_moves:
            return # Ghost is trapped

        direction = random.choice(possible_moves)
        new_x = self.ghost_x
        new_y = self.ghost_y

        if direction == 'w':
            new_y -= 1
        elif direction == 's':
            new_y += 1
        elif direction == 'a':
            new_x -= 1
        elif direction == 'd':
            new_x += 1

        if self.board[new_y][new_x] == 'P':
            self.game_over = True
            return

        self.board[self.ghost_y][self.ghost_x] = ' '
        self.ghost_x = new_x
        self.ghost_y = new_y
        self.board[self.ghost_y][self.ghost_x] = 'G'


    def play(self):
        while not self.game_over and self.food_count > 0:
            self.print_board()
            direction = input("Enter direction (w/a/s/d): ").lower()
            self.move_pacman(direction)
            if not self.game_over:
                self.move_ghost()
            time.sleep(0.2)  # Add a small delay to make it playable

        self.print_board()
        if self.game_over:
            print("Game Over! Ghost caught Pac-Man.")
        else:
            print("Congratulations! You ate all the food!")
        print(f"Final Score: {self.score}")


if __name__ == "__main__":
    game = PacManGame()
    game.play()