import random

class RockPaperScissors:
    """
    A class to represent the Rock-Paper-Scissors game.
    """

    def __init__(self):
        """
        Initializes the game with a list of possible choices and scores.
        """
        self.choices = ["rock", "paper", "scissors"]
        self.player_score = 0
        self.computer_score = 0

    def get_player_choice(self):
        """
        Gets the player's choice from the command line.
        Ensures the input is valid.

        Returns:
            str: The player's choice (rock, paper, or scissors).
        """
        while True:
            choice = input("Enter your choice (rock, paper, or scissors): ").lower()
            if choice in self.choices:
                return choice
            else:
                print("Invalid choice. Please enter rock, paper, or scissors.")

    def get_computer_choice(self):
        """
        Generates a random choice for the computer.

        Returns:
            str: The computer's choice (rock, paper, or scissors).
        """
        return random.choice(self.choices)

    def determine_winner(self, player_choice, computer_choice):
        """
        Determines the winner of the round based on the choices.

        Args:
            player_choice (str): The player's choice.
            computer_choice (str): The computer's choice.

        Returns:
            str: A message indicating the outcome of the round.
        """
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            return "It's a tie!"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            self.player_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "Computer wins!"

    def display_score(self):
         """
         Displays the current score.
         """
         print(f"Score: You - {self.player_score}, Computer - {self.computer_score}")


    def play_round(self):
        """
        Plays a single round of the game.
        """
        player_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(player_choice, computer_choice)
        print(result)
        self.display_score()


    def play_game(self):
        """
        Plays the game until the player chooses to quit.
        """
        print("Welcome to Rock-Paper-Scissors!")
        while True:
            self.play_round()
            play_again = input("Play again? (y/n): ").lower()
            if play_again != "y":
                print("Thanks for playing!")
                break


if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()