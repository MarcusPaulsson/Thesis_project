import random

class RockPaperScissors:
    """
    A class representing the Rock-Paper-Scissors game.
    """

    def __init__(self):
        """
        Initializes the game with the possible choices and sets the scores to zero.
        """
        self.choices = ["rock", "paper", "scissors"]
        self.player_score = 0
        self.computer_score = 0

    def get_player_choice(self):
        """
        Prompts the player for their choice and validates the input.

        Returns:
            str: The player's choice (rock, paper, or scissors).
        """
        while True:
            choice = input("Choose rock, paper, or scissors: ").lower()
            if choice in self.choices:
                return choice
            else:
                print("Invalid choice. Please choose rock, paper, or scissors.")

    def get_computer_choice(self):
        """
        Generates a random choice for the computer.

        Returns:
            str: The computer's choice (rock, paper, or scissors).
        """
        return random.choice(self.choices)

    def determine_winner(self, player_choice, computer_choice):
        """
        Determines the winner of a round based on the player's and computer's choices.

        Args:
            player_choice (str): The player's choice.
            computer_choice (str): The computer's choice.

        Returns:
            str: A message indicating the result of the round (win, lose, or tie).
        """
        if player_choice == computer_choice:
            return "It's a tie!"
        elif (
            (player_choice == "rock" and computer_choice == "scissors")
            or (player_choice == "paper" and computer_choice == "rock")
            or (player_choice == "scissors" and computer_choice == "paper")
        ):
            self.player_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "You lose!"

    def display_scores(self):
        """
        Displays the current scores of the player and the computer.
        """
        print(f"Player: {self.player_score}, Computer: {self.computer_score}")

    def play_round(self):
        """
        Plays a single round of the game.
        """
        player_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()

        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        result = self.determine_winner(player_choice, computer_choice)
        print(result)

        self.display_scores()

    def play_game(self):
        """
        Plays the entire game until the player chooses to quit.
        """
        print("Welcome to Rock-Paper-Scissors!")

        while True:
            self.play_round()

            play_again = input("Play again? (yes/no): ").lower()
            if play_again != "yes":
                print("Thanks for playing!")
                break


if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()