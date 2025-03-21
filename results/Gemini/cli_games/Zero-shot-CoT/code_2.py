import random

class RockPaperScissors:
    """
    A class to represent a Rock-Paper-Scissors game.
    """

    def __init__(self):
        """
        Initializes the game with the available choices and initial scores.
        """
        self.choices = ["rock", "paper", "scissors"]
        self.player_score = 0
        self.computer_score = 0

    def get_player_choice(self):
        """
        Gets the player's choice from the command line.
        Handles invalid inputs.
        """
        while True:
            choice = input("Choose rock, paper, or scissors: ").lower()
            if choice in self.choices:
                return choice
            else:
                print("Invalid choice. Please try again.")

    def get_computer_choice(self):
        """
        Generates a random choice for the computer.
        """
        return random.choice(self.choices)

    def determine_winner(self, player_choice, computer_choice):
        """
        Determines the winner of a round based on the player's and computer's choices.
        """
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
            return "tie"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!")
            return "player"
        else:
            print("Computer wins this round!")
            return "computer"

    def update_score(self, winner):
        """
        Updates the score based on the winner of the round.
        """
        if winner == "player":
            self.player_score += 1
        elif winner == "computer":
            self.computer_score += 1

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