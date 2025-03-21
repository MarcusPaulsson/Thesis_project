import time
import random
import os


class Pong:
    """
    A command-line Pong game implementation.
    """

    def __init__(self, width=60, height=20, paddle_length=3, max_score=10):
        """
        Initializes the Pong game.

        Args:
            width (int): The width of the game board.
            height (int): The height of the game board.
            paddle_length (int): The length of the paddles.
            max_score (int): The maximum score to win the game.
        """

        self.width = width
        self.height = height
        self.paddle_length = paddle_length
        self.max_score = max_score

        # Paddle positions (centered vertically)
        self.paddle_left_y = height // 2 - paddle_length // 2
        self.paddle_right_y = height // 2 - paddle_length // 2

        # Ball position and direction
        self.ball_x = width // 2
        self.ball_y = height // 2
        self.ball_dx = random.choice([-1, 1])  # Initial horizontal direction
        self.ball_dy = random.choice([-1, 1])  # Initial vertical direction

        # Scores
        self.score_left = 0
        self.score_right = 0

        self.running = True
        self.last_update = time.time()
        self.frame_rate = 0.1  # seconds between frames (adjust for speed)

    def _clear_screen(self):
        """Clears the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def _draw_board(self):
        """Draws the game board with paddles, ball, and scores."""
        board = [[' ' for _ in range(self.width)] for _ in range(self.height)]

        # Draw paddles
        for i in range(self.paddle_length):
            board[self.paddle_left_y + i][0] = '|'
            board[self.paddle_right_y + i][self.width - 1] = '|'

        # Draw ball
        board[self.ball_y][self.ball_x] = 'O'

        # Prepare the output string
        output = ""

        # Draw top border
        output += "+" + ("-" * (self.width - 2)) + "+\n"

        # Draw the board content
        for row in board:
            output += "|" + "".join(row[1:-1]) + "|\n"

        # Draw bottom border
        output += "+" + ("-" * (self.width - 2)) + "+\n"

        # Draw scores
        output += f"Score: Left {self.score_left} - Right {self.score_right}\n"
        return output

    def _update_ball(self):
        """Updates the ball's position and handles collisions."""
        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy

        # Bounce off top and bottom walls
        if self.ball_y <= 0 or self.ball_y >= self.height - 1:
            self.ball_dy *= -1

        # Bounce off paddles
        if self.ball_x <= 1 and self.paddle_left_y <= self.ball_y <= self.paddle_left_y + self.paddle_length - 1:
            self.ball_dx *= -1
        elif self.ball_x >= self.width - 2 and self.paddle_right_y <= self.ball_y <= self.paddle_right_y + self.paddle_length - 1:
            self.ball_dx *= -1

        # Handle scoring and reset ball position
        if self.ball_x <= 0:
            self.score_right += 1
            self._reset_ball()
        elif self.ball_x >= self.width - 1:
            self.score_left += 1
            self._reset_ball()

    def _reset_ball(self):
        """Resets the ball to the center with a random direction."""
        self.ball_x = self.width // 2
        self.ball_y = self.height // 2
        self.ball_dx = random.choice([-1, 1])
        self.ball_dy = random.choice([-1, 1])

    def _move_paddle_left(self, direction):
        """Moves the left paddle up or down."""
        if direction == "up":
            if self.paddle_left_y > 0:
                self.paddle_left_y -= 1
        elif direction == "down":
            if self.paddle_left_y + self.paddle_length < self.height:
                self.paddle_left_y += 1

    def _move_paddle_right(self, direction):
        """Moves the right paddle up or down."""
        if direction == "up":
            if self.paddle_right_y > 0:
                self.paddle_right_y -= 1
        elif direction == "down":
            if self.paddle_right_y + self.paddle_length < self.height:
                self.paddle_right_y += 1

    def _get_input(self):
        """
        Gets player input for paddle movement.
        Non-blocking input is tricky in a cross-platform way in the terminal.
        This implementation uses simple polling with a timeout.  It is not ideal,
        but it avoids the need for external libraries.

        Returns:
            str: A string representing the player input ("q", "a", "z", "k", "m", or None).
        """
        import select
        import sys
        import tty
        import termios

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setraw(sys.stdin.fileno())
            [rlist, _, _] = select.select([sys.stdin], [], [], 0.01) # Non-blocking read with timeout
            if rlist:
                key = sys.stdin.read(1)
                return key
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return None

    def run(self):
        """Runs the main game loop."""
        print("Welcome to Pong!")
        print("Left paddle: 'a' (up), 'z' (down)")
        print("Right paddle: 'k' (up), 'm' (down)")
        print("Press 'q' to quit.")

        while self.running:
            current_time = time.time()
            if current_time - self.last_update >= self.frame_rate:
                self._clear_screen()
                board_str = self._draw_board()
                print(board_str)

                self._update_ball()

                # Handle player input
                user_input = self._get_input()
                if user_input == 'q':
                    self.running = False
                elif user_input == 'a':
                    self._move_paddle_left("up")
                elif user_input == 'z':
                    self._move_paddle_left("down")
                elif user_input == 'k':
                    self._move_paddle_right("up")
                elif user_input == 'm':
                    self._move_paddle_right("down")

                self.last_update = current_time

                # Check for a winner
                if self.score_left >= self.max_score:
                    print("Left player wins!")
                    self.running = False
                elif self.score_right >= self.max_score:
                    print("Right player wins!")
                    self.running = False
        print("Game Over.")


if __name__ == "__main__":
    game = Pong()
    game.run()