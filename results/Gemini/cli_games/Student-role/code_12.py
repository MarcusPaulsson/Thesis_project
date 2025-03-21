import time
import random
import os

class Pong:
    """
    A command-line Pong game.
    """

    def __init__(self, width=60, height=20, paddle_length=3, max_score=5):
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

        # Initialize game state
        self.ball_x = width // 2
        self.ball_y = height // 2
        self.ball_dx = random.choice([-1, 1])  # Ball direction x
        self.ball_dy = random.choice([-1, 1])  # Ball direction y

        self.paddle1_y = height // 2 - paddle_length // 2  # Player 1 (left)
        self.paddle2_y = height // 2 - paddle_length // 2  # Player 2 (right)

        self.score1 = 0
        self.score2 = 0

        self.game_over = False

    def _draw_board(self):
        """
        Draws the game board in the console.
        """
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console

        # Create the board as a list of strings
        board = []
        for _ in range(self.height):
            board.append([' '] * self.width)

        # Draw paddles
        for i in range(self.paddle_length):
            board[self.paddle1_y + i][0] = '|'
            board[self.paddle2_y + i][self.width - 1] = '|'

        # Draw ball
        board[self.ball_y][self.ball_x] = 'O'

        # Print the board
        print("-" * self.width)
        for row in board:
            print("".join(row))
        print("-" * self.width)

        # Print scores
        print(f"Player 1: {self.score1}  |  Player 2: {self.score2}")


    def _move_ball(self):
        """
        Moves the ball and handles collisions.
        """
        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy

        # Bounce off top and bottom walls
        if self.ball_y <= 0 or self.ball_y >= self.height - 1:
            self.ball_dy *= -1

        # Bounce off paddles
        if self.ball_x == 1 and self.paddle1_y <= self.ball_y < self.paddle1_y + self.paddle_length:
            self.ball_dx *= -1
        elif self.ball_x == self.width - 2 and self.paddle2_y <= self.ball_y < self.paddle2_y + self.paddle_length:
            self.ball_dx *= -1

        # Score points
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
        """
        Resets the ball to the center of the board.
        """
        self.ball_x = self.width // 2
        self.ball_y = self.height // 2
        self.ball_dx = random.choice([-1, 1])
        self.ball_dy = random.choice([-1, 1])


    def _move_paddle1(self, direction):
        """
        Moves paddle 1 up or down.

        Args:
            direction (str): "up" or "down".
        """
        if direction == "up" and self.paddle1_y > 0:
            self.paddle1_y -= 1
        elif direction == "down" and self.paddle1_y + self.paddle_length < self.height:
            self.paddle1_y += 1


    def _move_paddle2(self, direction):
        """
        Moves paddle 2 up or down.

        Args:
            direction (str): "up" or "down".
        """
        if direction == "up" and self.paddle2_y > 0:
            self.paddle2_y -= 1
        elif direction == "down" and self.paddle2_y + self.paddle_length < self.height:
            self.paddle2_y += 1


    def play(self):
        """
        Starts and runs the Pong game.
        """
        print("Welcome to Pong!")
        print("Player 1 (left): 'w' to move up, 's' to move down")
        print("Player 2 (right): 'o' to move up, 'l' to move down")
        print("Press 'q' to quit.")

        while not self.game_over:
            self._draw_board()
            self._move_ball()

            # Get player input
            player1_move = input("Player 1 (w/s): ").lower()
            player2_move = input("Player 2 (o/l): ").lower()

            # Handle player input
            if player1_move == "w":
                self._move_paddle1("up")
            elif player1_move == "s":
                self._move_paddle1("down")
            if player2_move == "o":
                self._move_paddle2("up")
            elif player2_move == "l":
                self._move_paddle2("down")
            elif player1_move == "q" or player2_move == "q":
                print("Quitting the game.")
                self.game_over = True
                break

            time.sleep(0.1)  # Control game speed

        self._draw_board()  # Draw final board
        if self.score1 > self.score2:
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")


if __name__ == "__main__":
    game = Pong()
    game.play()