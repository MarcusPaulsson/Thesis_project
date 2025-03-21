import random
import os

class PacManGame:
    def __init__(self, width=10, height=10, num_ghosts=1, num_food=10):
        self.width = width
        self.height = height
        self.num_ghosts = num_ghosts
        self.num_food = num_food
        self.board = [[' ' for _ in range(width)] for _ in range(height)]
        self.pacman_x = width // 2
        self.pacman_y = height // 2
        self.ghosts = []
        self.food_positions = set()
        self.score = 0
        self.game_over = False
        self.won = False

        self.initialize_game()

    def initialize_game(self):
        self.board[self.pacman_y][self.pacman_x] = 'P'

        # Place ghosts
        for _ in range(self.num_ghosts):
            while True:
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                if self.board[y][x] == ' ':
                    self.ghosts.append((x, y))
                    self.board[y][x] = 'G'
                    break

        # Place food
        while len(self.food_positions) < self.num_food:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.board[y][x] == ' ':
                self.food_positions.add((x, y))
                self.board[y][x] = '.'


    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        print("-" * (self.width + 2))
        for row in self.board:
            print("|" + "".join(row) + "|")
        print("-" * (self.width + 2))
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
            print("Invalid direction. Use w, a, s, d.")
            return

        if 0 <= new_x < self.width and 0 <= new_y < self.height:
            # Clear Pac-Man's previous position
            self.board[self.pacman_y][self.pacman_x] = ' '

            self.pacman_x, self.pacman_y = new_x, new_y

            # Check for food
            if (self.pacman_x, self.pacman_y) in self.food_positions:
                self.score += 1
                self.food_positions.remove((self.pacman_x, self.pacman_y))

            # Check for ghost collision
            if self.board[self.pacman_y][self.pacman_x] == 'G':
                self.game_over = True
                return

            # Update Pac-Man's position on the board
            self.board[self.pacman_y][self.pacman_x] = 'P'
        else:
            print("Invalid move: Moving out of bounds.")


    def move_ghosts(self):
        for i, (x, y) in enumerate(self.ghosts):
            self.board[y][x] = ' '  # Clear the ghost's previous position
            possible_moves = []
            if x > 0 and self.board[y][x-1] != 'G':
                possible_moves.append((x-1, y))
            if x < self.width - 1 and self.board[y][x+1] != 'G':
                possible_moves.append((x+1, y))
            if y > 0 and self.board[y-1][x] != 'G':
                possible_moves.append((x, y-1))
            if y < self.height - 1 and self.board[y+1][x] != 'G':
                possible_moves.append((x, y+1))
           
            if possible_moves:
                new_x, new_y = random.choice(possible_moves)


                #Check if the new position is food
                is_food = (new_x, new_y) in self.food_positions
                if is_food:
                    self.food_positions.remove((new_x, new_y))
                    self.food_positions.add((x,y)) #add back to old location

                self.ghosts[i] = (new_x, new_y)
                if self.board[new_y][new_x] == 'P':
                    self.game_over = True
                    return
                self.board[new_y][new_x] = 'G'
            else:
                self.board[y][x] = 'G' #Ghost stays in place

    def check_win_condition(self):
        if not self.food_positions:
            self.won = True
            self.game_over = True



    def play(self):
        while not self.game_over:
            self.print_board()
            direction = input("Enter direction (w/a/s/d): ").lower()
            self.move_pacman(direction)
            if self.game_over:
                break
            self.move_ghosts()
            self.check_win_condition()

        self.print_board()
        if self.won:
            print("Congratulations! You won!")
        else:
            print("Game Over! You were caught by a ghost.")


if __name__ == "__main__":
    game = PacManGame(width=15, height=10, num_ghosts=2, num_food=15)
    game.play()