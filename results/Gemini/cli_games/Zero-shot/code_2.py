import random

class RockPaperScissors:
    """
    A class to represent the Rock-Paper-Scissors game.
    """

    def __init__(self):
        """
        Initializes the game with possible choices and scores.
        """
        self.choices = ["rock", "paper", "scissors"]
        self.player_score = 0
        self.computer_score = 0

    def get_computer_choice(self):
        """
        Generates a random choice for the computer.

        Returns:
            str: The computer's choice (rock, paper, or scissors).
        """
        return random.choice(self.choices)

    def get_player_choice(self):
        """
        Prompts the player to enter their choice and validates the input.

        Returns:
            str: The player's choice (rock, paper, or scissors), or None if the input is invalid.
        """
        while True:
            choice = input("Enter your choice (rock, paper, or scissors): ").lower()
            if choice in self.choices:
                return choice
            else:
                print("Invalid choice. Please enter rock, paper, or scissors.")

    def determine_winner(self, player_choice, computer_choice):
        """
        Determines the winner of the round based on the player and computer choices.

        Args:
            player_choice (str): The player's choice.
            computer_choice (str): The computer's choice.

        Returns:
            str: "player", "computer", or "tie" indicating the winner of the round.
        """
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            return "tie"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            return "player"
        else:
            return "computer"

    def update_score(self, winner):
        """
        Updates the scores based on the winner of the round.

        Args:
            winner (str): "player", "computer", or "tie".
        """
        if winner == "player":
            self.player_score += 1
            print("You win this round!")
        elif winner == "computer":
            self.computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a tie!")

    def display_score(self):
        """
        Displays the current score.
        """
        print(f"Score: Player - {self.player_score}, Computer - {self.computer_score}")

    def play_round(self):
        """
        Plays a single round of the game.
        """
        player_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        winner = self.determine_winner(player_choice, computer_choice)
        self.update_score(winner)
        self.display_score()

    def play_game(self, num_rounds=3):
        """
        Plays the game for a specified number of rounds.

        Args:
            num_rounds (int): The number of rounds to play.
        """
        print("Welcome to Rock-Paper-Scissors!")
        for round_num in range(1, num_rounds + 1):
            print(f"\nRound {round_num}:")
            self.play_round()

        print("\nGame Over!")
        if self.player_score > self.computer_score:
            print("You win the game!")
        elif self.player_score < self.computer_score:
            print("Computer wins the game!")
        else:
            print("The game is a tie!")

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()