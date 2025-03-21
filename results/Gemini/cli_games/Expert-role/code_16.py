import random
import sys

class PacMan:
    """
    A command-line Pac-Man game.
    """

    def __init__(self, width=15, height=10, num_ghosts=2, initial_lives=3):
        """
        Initializes the game board and game state.

        Args:
            width (int): The width of the game board.
            height (int): The height of the game board.
            num_ghosts (int): The number of ghosts in the game.
            initial_lives (int): The number of lives Pac-Man starts with.
        """
        self.width = width
        self.height = height
        self.num_ghosts = num_ghosts
        self.initial_lives = initial_lives
        self.board = [['.' for _ in range(width)] for _ in range(height)]
        self.pacman_x = width // 2
        self.pacman_y = height // 2
        self.board[self.pacman_y][self.pacman_x] = 'P'
        self.ghosts = []
        for _ in range(num_ghosts):
            self.add_ghost()
        self.score = 0
        self.lives = initial_lives
        self.game_over = False
        self.total_dots = width * height - num_ghosts - 1 # - Pacman and Ghosts
        self.dots_eaten = 0


    def add_ghost(self):
        """
        Adds a new ghost to the game board at a random available location.
        """
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.board[y][x] == '.':
                self.ghosts.append((x, y))
                self.board[y][x] = 'G'
                break

    def print_board(self):
        """
        Prints the current game board to the console.
        """
        for row in self.board:
            print(''.join(row))
        print(f"Score: {self.score}, Lives: {self.lives}")

    def move_pacman(self, direction):
        """
        Moves Pac-Man in the specified direction.

        Args:
            direction (str): The direction to move ('up', 'down', 'left', 'right').
        """
        new_x = self.pacman_x
        new_y = self.pacman_y

        if direction == 'up':
            new_y -= 1
        elif direction == 'down':
            new_y += 1
        elif direction == 'left':
            new_x -= 1
        elif direction == 'right':
            new_x += 1
        else:
            print("Invalid direction.")
            return

        if 0 <= new_x < self.width and 0 <= new_y < self.height:
            if self.board[new_y][new_x] == '.':
                self.score += 1
                self.dots_eaten += 1
            elif self.board[new_y][new_x] == 'G':
                self.lose_life()
                return


            self.board[self.pacman_y][self.pacman_x] = ' ' # Clear old Pac-Man position
            self.pacman_x = new_x
            self.pacman_y = new_y
            self.board[self.pacman_y][self.pacman_x] = 'P'
            self.move_ghosts()

    def move_ghosts(self):
        """
        Moves each ghost randomly.
        """
        for i in range(len(self.ghosts)):
            old_x, old_y = self.ghosts[i]
            self.board[old_y][old_x] = ' '  # Clear old ghost position

            while True:
                dx = random.choice([-1, 0, 1])
                dy = random.choice([-1, 0, 1])
                if abs(dx) + abs(dy) != 1:
                    continue

                new_x = old_x + dx
                new_y = old_y + dy

                if 0 <= new_x < self.width and 0 <= new_y < self.height and self.board[new_y][new_x] != 'G' and self.board[new_y][new_x] != 'P':
                    break

            self.ghosts[i] = (new_x, new_y)
            if self.board[new_y][new_x] == 'P':
                self.lose_life()
                return


            self.board[new_y][new_x] = 'G'

    def lose_life(self):
        """
        Handles the event when Pac-Man loses a life.
        """
        self.lives -= 1
        if self.lives <= 0:
            self.game_over = True
            print("Game Over!")
        else:
            print("You lost a life!")
            self.reset_pacman_position()
            self.reset_ghost_positions()


    def reset_pacman_position(self):
         """Resets Pac-Man's position to the center of the board."""
         self.board[self.pacman_y][self.pacman_x] = ' '
         self.pacman_x = self.width // 2
         self.pacman_y = self.height // 2
         self.board[self.pacman_y][self.pacman_x] = 'P'

    def reset_ghost_positions(self):
        """Resets the ghost positions, placing them randomly on the board."""
        for x, y in self.ghosts:
            self.board[y][x] = ' '
        self.ghosts = []
        for _ in range(self.num_ghosts):
            self.add_ghost()


    def is_win(self):
        """
        Checks if the player has won the game.
        """
        return self.dots_eaten == self.total_dots

    def play(self):
        """
        Main game loop.
        """
        while not self.game_over:
            self.print_board()
            if self.is_win():
                print("You Win!")
                break


            direction = input("Enter move (up, down, left, right, quit): ").lower()

            if direction == 'quit':
                print("Quitting the game.")
                break

            self.move_pacman(direction)

        if self.game_over:
             self.print_board()
             print("Final Score:", self.score)



if __name__ == "__main__":
    game = PacMan()
    game.play()