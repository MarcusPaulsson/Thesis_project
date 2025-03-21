import random
import time
import os

class PacMan:
    def __init__(self, width=15, height=10, num_ghosts=2):
        self.width = width
        self.height = height
        self.num_ghosts = num_ghosts
        self.grid = [['.' for _ in range(width)] for _ in range(height)]
        self.pacman_x = width // 2
        self.pacman_y = height // 2
        self.grid[self.pacman_y][self.pacman_x] = 'P'
        self.ghosts = []
        self.food = width * height - 1 # Initial food count (excluding Pac-Man's starting position)
        self.score = 0
        self.game_over = False
        self.won = False
        self.ghost_chars = ['G', 'H', 'I', 'J'] # Allow for up to 4 ghosts, expand if needed

        # Initial ghost placement (avoiding Pac-Man)
        for i in range(num_ghosts):
            while True:
                x = random.randint(0, width - 1)
                y = random.randint(0, height - 1)
                if (x, y) != (self.pacman_x, self.pacman_y):
                    self.ghosts.append({'x': x, 'y': y, 'char': self.ghost_chars[i % len(self.ghost_chars)]})
                    self.grid[y][x] = self.ghosts[-1]['char']
                    break
        self.display_delay = 0.2  # Delay between moves for better viewing

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen
        print("-" * (self.width + 2)) # Top border
        for row in self.grid:
            print("|" + "".join(row) + "|") # Side borders
        print("-" * (self.width + 2)) # Bottom border
        print(f"Score: {self.score}, Food remaining: {self.food}")


    def move_pacman(self, direction):
        new_x = self.pacman_x
        new_y = self.pacman_y

        if direction == 'w':
            new_y -= 1
        elif direction == 's':
            new_y += 1
        elif direction == 'a':
            new_x -= 1
        elif direction == 'd':
            new_x += 1
        else:
            return  # Invalid move

        if 0 <= new_x < self.width and 0 <= new_y < self.height:
            # Clear Pac-Man's old position
            self.grid[self.pacman_y][self.pacman_x] = '.'

            # Check for collision with a ghost
            for ghost in self.ghosts:
                if new_x == ghost['x'] and new_y == ghost['y']:
                    self.game_over = True
                    return

            # Update Pac-Man's position
            self.pacman_x = new_x
            self.pacman_y = new_y

            # Check if Pac-Man eats food
            if self.grid[self.pacman_y][self.pacman_x] == '.':
                self.score += 10
                self.food -= 1

            # Place Pac-Man in the new position
            self.grid[self.pacman_y][self.pacman_x] = 'P'

            if self.food == 0:
                self.won = True
                self.game_over = True

    def move_ghosts(self):
        for ghost in self.ghosts:
            old_x = ghost['x']
            old_y = ghost['y']
            self.grid[old_y][old_x] = '.'

            possible_moves = []
            if old_x > 0:
                possible_moves.append(('a', old_x - 1, old_y))
            if old_x < self.width - 1:
                possible_moves.append(('d', old_x + 1, old_y))
            if old_y > 0:
                possible_moves.append(('w', old_x, old_y - 1))
            if old_y < self.height - 1:
                possible_moves.append(('s', old_x, old_y + 1))

            # Prioritize moving towards Pac-Man
            best_move = None
            min_distance = float('inf')
            for move, new_x, new_y in possible_moves:
                distance = abs(new_x - self.pacman_x) + abs(new_y - self.pacman_y)
                if distance < min_distance:
                    min_distance = distance
                    best_move = (move, new_x, new_y)

            if best_move:
                _, new_x, new_y = best_move
            else: #If no valid moves, stay put
                new_x = old_x
                new_y = old_y

            # Check for collision with Pac-Man
            if new_x == self.pacman_x and new_y == self.pacman_y:
                self.game_over = True
                return

            # Check for collision with other ghosts
            for other_ghost in self.ghosts:
                if ghost != other_ghost and new_x == other_ghost['x'] and new_y == other_ghost['y']:
                    new_x = old_x  # Stay put if collision with other ghost
                    new_y = old_y
                    break

            ghost['x'] = new_x
            ghost['y'] = new_y
            self.grid[new_y][new_x] = ghost['char']


    def play(self):
        while not self.game_over:
            self.display()
            direction = input("Enter move (w/a/s/d): ").lower()
            self.move_pacman(direction)
            if self.game_over:
                break  # Exit loop immediately if Pac-Man dies during move_pacman
            self.move_ghosts()
            time.sleep(self.display_delay)



        self.display() # Display final state
        if self.won:
            print("You win!")
        else:
            print("Game over!")
        print(f"Final Score: {self.score}")


if __name__ == '__main__':
    game = PacMan()
    game.play()