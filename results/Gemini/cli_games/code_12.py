import time
import random
import os

class Pong:
    """
    A command-line Pong game.
    """

    def __init__(self, width=60, height=20, paddle_length=4, ball_speed=1, ai_speed=1):
        """
        Initializes the Pong game.

        Args:
            width (int): Width of the game board.
            height (int): Height of the game board.
            paddle_length (int): Length of the paddles.
            ball_speed (int): Initial speed of the ball.
            ai_speed (int): Initial speed of the AI paddle.
        """
        self.width = width
        self.height = height
        self.paddle_length = paddle_length
        self.ball_speed = ball_speed
        self.ai_speed = ai_speed

        self.player_paddle_x = 1
        self.player_paddle_y = height // 2 - paddle_length // 2
        self.ai_paddle_x = width - 2
        self.ai_paddle_y = height // 2 - paddle_length // 2

        self.ball_x = width // 2
        self.ball_y = height // 2
        self.ball_dx = random.choice([-1, 1]) * ball_speed
        self.ball_dy = random.choice([-1, 1]) * ball_speed

        self.player_score = 0
        self.ai_score = 0
        self.game_over = False

    def _clear_screen(self):
        """Clears the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def _draw_board(self):
        """Draws the game board with paddles and ball."""

        board = [[' ' for _ in range(self.width)] for _ in range(self.height)]

        # Draw paddles
        for i in range(self.paddle_length):
            if 0 <= self.player_paddle_y + i < self.height:
                board[self.player_paddle_y + i][self.player_paddle_x] = '|'
            if 0 <= self.ai_paddle_y + i < self.height:
                board[self.ai_paddle_y + i][self.ai_paddle_x] = '|'

        # Draw ball
        if 0 <= self.ball_y < self.height and 0 <= self.ball_x < self.width:
            board[self.ball_y][self.ball_x] = 'O'

        # Draw score
        score_str = f"Player: {self.player_score}  AI: {self.ai_score}"
        score_x = (self.width - len(score_str)) // 2
        for i, char in enumerate(score_str):
            if 0 <= score_x + i < self.width:
                board[0][score_x + i] = char


        self._clear_screen()
        for row in board:
            print("".join(row))
        print(f"Controls: W (Up), S (Down), Q (Quit)  - Ball Speed: {abs(self.ball_dx)}, AI Speed: {self.ai_speed}") #Added speed info


    def _update_ball(self):
        """Updates the ball's position and handles collisions."""
        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy

        # Bounce off top and bottom walls
        if self.ball_y <= 0 or self.ball_y >= self.height - 1:
            self.ball_dy *= -1

        # Bounce off paddles
        if (self.ball_x <= self.player_paddle_x + 1 and
            self.player_paddle_y <= self.ball_y < self.player_paddle_y + self.paddle_length):
            self.ball_dx *= -1
            self.ball_dx = max(self.ball_dx * 1.1, -5) if self.ball_dx < 0 else min(self.ball_dx * 1.1, 5) # Increase ball speed after paddle hit.

        if (self.ball_x >= self.ai_paddle_x - 1 and
            self.ai_paddle_y <= self.ball_y < self.ai_paddle_y + self.paddle_length):
            self.ball_dx *= -1
            self.ball_dx = max(self.ball_dx * 1.1, -5) if self.ball_dx < 0 else min(self.ball_dx * 1.1, 5) # Increase ball speed after paddle hit.
        # Score
        if self.ball_x <= 0:
            self.ai_score += 1
            self._reset_ball()
        elif self.ball_x >= self.width - 1:
            self.player_score += 1
            self._reset_ball()

        #Check for Game Over
        if self.player_score >= 10 or self.ai_score >= 10:
            self.game_over = True

    def _reset_ball(self):
        """Resets the ball to the center of the board with random direction."""
        self.ball_x = self.width // 2
        self.ball_y = self.height // 2
        self.ball_dx = random.choice([-1, 1]) * self.ball_speed
        self.ball_dy = random.choice([-1, 1]) * self.ball_speed

    def _update_ai(self):
        """Updates the AI paddle's position."""
        if self.ai_paddle_y + self.paddle_length // 2 < self.ball_y and self.ai_paddle_y < self.height - self.paddle_length:
            self.ai_paddle_y += self.ai_speed
        elif self.ai_paddle_y + self.paddle_length // 2 > self.ball_y and self.ai_paddle_y > 0:
            self.ai_paddle_y -= self.ai_speed


    def _handle_input(self, key):
        """Handles player input."""
        if key.lower() == 'w':
            self.player_paddle_y = max(0, self.player_paddle_y - 1)
        elif key.lower() == 's':
            self.player_paddle_y = min(self.height - self.paddle_length, self.player_paddle_y + 1)
        elif key.lower() == 'q':
            self.game_over = True
        elif key.lower() == 'a': #Increase AI speed
            self.ai_speed = min(self.ai_speed + 1, 5) #Limit to 5
        elif key.lower() == 'd': #Decrease AI speed
            self.ai_speed = max(self.ai_speed - 1, 1) #Limit to 1



    def play(self):
        """Starts the Pong game loop."""
        while not self.game_over:
            self._draw_board()
            self._update_ball()
            self._update_ai()

            key = input()  # Get player input
            self._handle_input(key)

            time.sleep(0.05)  # Adjust for game speed

        self._draw_board() #Final Draw
        if self.player_score > self.ai_score:
            print("Player wins!")
        else:
            print("AI wins!")


if __name__ == "__main__":
    game = Pong(width=70, height=25, paddle_length=5, ball_speed=1, ai_speed=2)
    game.play()