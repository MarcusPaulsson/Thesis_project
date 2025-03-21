import time
import random
import os

class Pong:
    """
    A simple Pong game implemented in the command line.
    """

    def __init__(self, width=60, height=20, paddle_length=3, ball_speed_x=1, ball_speed_y=1):
        """
        Initializes the Pong game.

        Args:
            width (int): The width of the game board.
            height (int): The height of the game board.
            paddle_length (int): The length of the paddles.
        """
        self.width = width
        self.height = height
        self.paddle_length = paddle_length
        self.ball_speed_x = ball_speed_x
        self.ball_speed_y = ball_speed_y

        self.paddle1_pos = height // 2 - paddle_length // 2
        self.paddle2_pos = height // 2 - paddle_length // 2
        self.ball_x = width // 2
        self.ball_y = height // 2
        self.ball_dx = self.ball_speed_x * random.choice([-1, 1])  # Ball direction x (+1 or -1)
        self.ball_dy = self.ball_speed_y * random.choice([-1, 1])  # Ball direction y (+1 or -1)

        self.score1 = 0
        self.score2 = 0
        self.game_over = False

    def _clear_screen(self):
        """Clears the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def _draw_board(self):
        """
        Draws the game board in the console.
        """
        self._clear_screen()
        board = []
        for i in range(self.height):
            board.append([' '] * self.width)

        # Draw paddles
        for i in range(self.paddle_length):
            board[self.paddle1_pos + i][1] = '|'
            board[self.paddle2_pos + i][self.width - 2] = '|'

        # Draw ball
        board[self.ball_y][self.ball_x] = 'O'

        # Draw score
        score_str = f"Player 1: {self.score1}  Player 2: {self.score2}"
        print(score_str.center(self.width))

        # Draw board
        for row in board:
            print(''.join(row))


    def _update_ball(self):
        """
        Updates the ball's position.
        """
        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy

        # Bounce off top and bottom walls
        if self.ball_y <= 0 or self.ball_y >= self.height - 1:
            self.ball_dy *= -1

        # Bounce off paddles
        if self.ball_x <= 2 and self.paddle1_pos <= self.ball_y <= self.paddle1_pos + self.paddle_length - 1:
            self.ball_dx *= -1
        elif self.ball_x >= self.width - 3 and self.paddle2_pos <= self.ball_y <= self.paddle2_pos + self.paddle_length - 1:
            self.ball_dx *= -1

        # Score and reset ball position
        if self.ball_x <= 0:
            self.score2 += 1
            self.ball_x = self.width // 2
            self.ball_y = self.height // 2
            self.ball_dx = self.ball_speed_x * random.choice([-1, 1])
            self.ball_dy = self.ball_speed_y * random.choice([-1, 1])
        elif self.ball_x >= self.width - 1:
            self.score1 += 1
            self.ball_x = self.width // 2
            self.ball_y = self.height // 2
            self.ball_dx = self.ball_speed_x * random.choice([-1, 1])
            self.ball_dy = self.ball_speed_y * random.choice([-1, 1])

    def _update_paddles(self, player1_move, player2_move):
        """
        Updates the paddle positions based on player input.

        Args:
            player1_move (str): 'up' or 'down' for player 1.
            player2_move (str): 'up' or 'down' for player 2.
        """
        if player1_move == 'up' and self.paddle1_pos > 0:
            self.paddle1_pos -= 1
        elif player1_move == 'down' and self.paddle1_pos < self.height - self.paddle_length - 1:
            self.paddle1_pos += 1

        if player2_move == 'up' and self.paddle2_pos > 0:
            self.paddle2_pos -= 1
        elif player2_move == 'down' and self.paddle2_pos < self.height - self.paddle_length - 1:
            self.paddle2_pos += 1

    def play(self):
        """
        Runs the main game loop.
        """
        while not self.game_over:
            self._draw_board()

            # Get player input
            player1_move = input("Player 1 (w/s): ").lower()
            player2_move = input("Player 2 (up/down): ").lower()

            # Validate player input
            if player1_move not in ('w', 's', ''):
                player1_move = ''  # Ignore invalid input
            if player2_move not in ('up', 'down', ''):
                player2_move = ''  # Ignore invalid input

            # Convert player 1 input to 'up' and 'down'
            if player1_move == 'w':
                player1_move = 'up'
            elif player1_move == 's':
                player1_move = 'down'

            self._update_paddles(player1_move, player2_move)
            self._update_ball()

            # Check for game over (optional)
            if self.score1 >= 10 or self.score2 >= 10:
                self.game_over = True

            time.sleep(0.05)  # Control game speed

        self._draw_board()
        print("Game Over!")
        if self.score1 > self.score2:
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")


if __name__ == '__main__':
    game = Pong()
    game.play()