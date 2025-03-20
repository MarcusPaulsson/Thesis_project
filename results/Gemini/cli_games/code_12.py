import time
import random
import os

class Pong:
    """
    A command-line implementation of the classic Pong game.
    """

    def __init__(self, width=60, height=20, paddle_length=5, ball_speed=1):
        """
        Initializes the Pong game.

        Args:
            width (int): The width of the game board.
            height (int): The height of the game board.
            paddle_length (int): The length of the paddles.
            ball_speed (int): The speed of the ball (number of steps per update).
        """
        self.width = width
        self.height = height
        self.paddle_length = paddle_length
        self.ball_speed = ball_speed

        self.player1_pos = height // 2 - paddle_length // 2
        self.player2_pos = height // 2 - paddle_length // 2
        self.ball_x = width // 2
        self.ball_y = height // 2
        self.ball_dx = random.choice([-1, 1])  # Ball direction in x-axis
        self.ball_dy = random.choice([-1, 1])  # Ball direction in y-axis
        self.player1_score = 0
        self.player2_score = 0
        self.game_over = False
        self.max_score = 10


    def draw_board(self):
        """
        Draws the game board with paddles and the ball.
        """

        os.system('cls' if os.name == 'nt' else 'clear')

        board = [[' ' for _ in range(self.width)] for _ in range(self.height)]

        # Draw paddles
        for i in range(self.paddle_length):
            if 0 <= self.player1_pos + i < self.height:
                board[self.player1_pos + i][0] = '|'
            if 0 <= self.player2_pos + i < self.height:
                board[self.player2_pos + i][self.width - 1] = '|'

        # Draw ball
        board[self.ball_y][self.ball_x] = 'O'

        # Print board
        print("-" * self.width)
        for row in board:
            print("".join(row))
        print("-" * self.width)
        print(f"Player 1: {self.player1_score}  Player 2: {self.player2_score}")


    def update_ball(self):
        """
        Updates the ball's position and handles collisions.
        """
        for _ in range(self.ball_speed):
            new_ball_x = self.ball_x + self.ball_dx
            new_ball_y = self.ball_y + self.ball_dy

            # Check for collisions with top/bottom walls
            if new_ball_y <= 0 or new_ball_y >= self.height - 1:
                self.ball_dy *= -1
                new_ball_y = self.ball_y + self.ball_dy  # Recalculate after bounce

            # Check for collisions with paddles
            if new_ball_x <= 0:
                if self.player1_pos <= new_ball_y <= self.player1_pos + self.paddle_length - 1:
                    self.ball_dx *= -1
                    new_ball_x = self.ball_x + self.ball_dx  # Recalculate after bounce
                else:
                    self.player2_score += 1
                    self.reset_ball()
                    return

            if new_ball_x >= self.width - 1:
                if self.player2_pos <= new_ball_y <= self.player2_pos + self.paddle_length - 1:
                    self.ball_dx *= -1
                    new_ball_x = self.ball_x + self.ball_dx  # Recalculate after bounce
                else:
                    self.player1_score += 1
                    self.reset_ball()
                    return

            self.ball_x = new_ball_x
            self.ball_y = new_ball_y

    def reset_ball(self):
         """Resets the ball to the center after a point is scored."""
         self.ball_x = self.width // 2
         self.ball_y = self.height // 2
         self.ball_dx = random.choice([-1, 1])
         self.ball_dy = random.choice([-1, 1])


    def move_player1(self, direction):
        """
        Moves player 1's paddle.

        Args:
            direction (str): "up" or "down".
        """
        if direction == "up" and self.player1_pos > 0:
            self.player1_pos -= 1
        elif direction == "down" and self.player1_pos + self.paddle_length < self.height:
            self.player1_pos += 1


    def move_player2(self, direction):
        """
        Moves player 2's paddle.

        Args:
            direction (str): "up" or "down".
        """
        if direction == "up" and self.player2_pos > 0:
            self.player2_pos -= 1
        elif direction == "down" and self.player2_pos + self.paddle_length < self.height:
            self.player2_pos += 1


    def check_game_over(self):
        """Checks if the game is over."""
        if self.player1_score >= self.max_score or self.player2_score >= self.max_score:
            self.game_over = True
            return True
        return False

    def play(self):
        """
        Starts and runs the game loop.
        """
        while not self.game_over:
            self.draw_board()

            # Get player input (non-blocking)
            player1_move = input("Player 1 (w/s): ").lower()
            player2_move = input("Player 2 (o/l): ").lower()

            # Move players
            if player1_move == "w":
                self.move_player1("up")
            elif player1_move == "s":
                self.move_player1("down")

            if player2_move == "o":
                self.move_player2("up")
            elif player2_move == "l":
                self.move_player2("down")

            self.update_ball()

            if self.check_game_over():
                self.draw_board()
                if self.player1_score >= self.max_score:
                    print("Player 1 wins!")
                else:
                    print("Player 2 wins!")
                break

            time.sleep(0.05)


if __name__ == "__main__":
    game = Pong()
    game.play()