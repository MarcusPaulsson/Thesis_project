import random

class RockPaperScissors:
    """
    A class to represent the Rock-Paper-Scissors game.
    """

    def __init__(self):
        """
        Initializes the game with player and computer scores set to 0.
        """
        self.player_score = 0
        self.computer_score = 0
        self.choices = ["rock", "paper", "scissors"]

    def get_player_choice(self):
        """
        Gets the player's choice from the command line.
        Validates the input to ensure it's a valid choice.

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
        Determines the winner of the round based on player and computer choices.

        Args:
            player_choice (str): The player's choice.
            computer_choice (str): The computer's choice.

        Returns:
            str: A message indicating the winner of the round.
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

    def play_round(self):
        """
        Plays a single round of the game.
        """
        player_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(player_choice, computer_choice)
        print(result)
        print(f"Score - You: {self.player_score}, Computer: {self.computer_score}")

    def play_game(self, num_rounds=3):
        """
        Plays the entire game for a specified number of rounds.

        Args:
            num_rounds (int): The number of rounds to play (default is 3).
        """
        print("Welcome to Rock-Paper-Scissors!")
        for i in range(num_rounds):
            print(f"\nRound {i+1}:")
            self.play_round()

        print("\nGame Over!")
        if self.player_score > self.computer_score:
            print("You are the ultimate Rock-Paper-Scissors champion!")
        elif self.player_score < self.computer_score:
            print("The computer reigns supreme!")
        else:
            print("It's a draw! A true test of skill.")

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()