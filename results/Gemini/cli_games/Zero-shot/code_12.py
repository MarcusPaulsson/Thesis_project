import time
import random
import os


class Pong:
    """
    A simple command-line Pong game.
    """

    def __init__(self, width=60, height=20, paddle_length=4):
        """
        Initializes the Pong game.

        Args:
            width (int): Width of the game board.
            height (int): Height of the game board.
            paddle_length (int): Length of the paddles.
        """
        self.width = width
        self.height = height
        self.paddle_length = paddle_length
        self.ball_x = width // 2
        self.ball_y = height // 2
        self.ball_dx = random.choice([-1, 1])  # Ball direction in x-axis
        self.ball_dy = random.choice([-1, 1])  # Ball direction in y-axis
        self.paddle1_y = height // 2 - paddle_length // 2
        self.paddle2_y = height // 2 - paddle_length // 2
        self.score1 = 0
        self.score2 = 0
        self.max_score = 5  # Game ends when a player reaches this score
        self.game_over = False

    def _clear_screen(self):
        """Clears the terminal screen."""
        os.system("cls" if os.name == "nt" else "clear")

    def _draw_board(self):
        """Draws the game board in the console."""
        board = []
        for i in range(self.height):
            board.append([" "] * self.width)

        # Draw paddles
        for i in range(self.paddle_length):
            board[self.paddle1_y + i][1] = "|"  # Paddle 1
            board[self.paddle2_y + i][self.width - 2] = "|"  # Paddle 2

        # Draw ball
        board[self.ball_y][self.ball_x] = "O"

        # Print the board
        self._clear_screen()
        print("-" * self.width)
        for row in board:
            print("".join(row))
        print("-" * self.width)
        print(f"Player 1: {self.score1}  |  Player 2: {self.score2}")

    def _move_ball(self):
        """Moves the ball and handles collisions."""
        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy

        # Bounce off top and bottom walls
        if self.ball_y <= 0 or self.ball_y >= self.height - 1:
            self.ball_dy *= -1

        # Bounce off paddles
        if self.ball_x <= 2 and self.paddle1_y <= self.ball_y <= self.paddle1_y + self.paddle_length - 1:
            self.ball_dx *= -1
            # Add some randomness to the vertical direction
            self.ball_dy += random.choice([-1, 0, 1])
            self.ball_dy = max(min(self.ball_dy, 1), -1)  # Limit dy to -1,0,1

        if self.ball_x >= self.width - 3 and self.paddle2_y <= self.ball_y <= self.paddle2_y + self.paddle_length - 1:
            self.ball_dx *= -1
            # Add some randomness to the vertical direction
            self.ball_dy += random.choice([-1, 0, 1])
            self.ball_dy = max(min(self.ball_dy, 1), -1)  # Limit dy to -1,0,1
        # Score and reset if ball goes out of bounds
        if self.ball_x <= 0:
            self.score2 += 1
            self._reset_ball()
        elif self.ball_x >= self.width - 1:
            self.score1 += 1
            self._reset_ball()

        # Check for game over
        if self.score1 >= self.max_score or self.score2 >= self.max_score:
            self.game_over = True

    def _reset_ball(self):
        """Resets the ball to the center after a score."""
        self.ball_x = self.width // 2
        self.ball_y = self.height // 2
        self.ball_dx = random.choice([-1, 1])
        self.ball_dy = random.choice([-1, 1])

    def _move_paddle1(self, direction):
        """Moves paddle 1 up or down."""
        if direction == "up":
            if self.paddle1_y > 0:
                self.paddle1_y -= 1
        elif direction == "down":
            if self.paddle1_y + self.paddle_length < self.height:
                self.paddle1_y += 1

    def _move_paddle2(self, direction):
        """Moves paddle 2 up or down."""
        if direction == "up":
            if self.paddle2_y > 0:
                self.paddle2_y -= 1
        elif direction == "down":
            if self.paddle2_y + self.paddle_length < self.height:
                self.paddle2_y += 1

    def play(self):
        """Starts the Pong game loop."""
        while not self.game_over:
            self._draw_board()
            # Get input for paddle movements
            p1_move = input("Player 1 (w/s): ").lower()
            p2_move = input("Player 2 (up/down): ").lower()

            # Process paddle movements
            if "w" in p1_move:
                self._move_paddle1("up")
            if "s" in p1_move:
                self._move_paddle1("down")
            if "up" in p2_move:
                self._move_paddle2("up")
            if "down" in p2_move:
                self._move_paddle2("down")

            self._move_ball()
            time.sleep(0.1)  # Control game speed

        # Game over message
        self._draw_board()
        if self.score1 > self.score2:
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")


if __name__ == "__main__":
    game = Pong()
    game.play()