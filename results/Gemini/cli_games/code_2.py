import random

class RockPaperScissors:
    """
    A class to represent the Rock-Paper-Scissors game.
    """

    def __init__(self):
        """
        Initializes the game.
        """
        self.choices = ["rock", "paper", "scissors"]
        self.player_score = 0
        self.computer_score = 0
        self.rounds = 0

    def get_player_choice(self):
        """
        Gets the player's choice from the command line.
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
        """
        return random.choice(self.choices)

    def determine_winner(self, player_choice, computer_choice):
        """
        Determines the winner of a round.
        """
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
            return "tie"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            return "player"
        else:
            print("Computer wins!")
            return "computer"

    def play_round(self):
        """
        Plays a single round of the game.
        """
        self.rounds += 1
        print(f"\nRound {self.rounds}:")
        player_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        winner = self.determine_winner(player_choice, computer_choice)

        if winner == "player":
            self.player_score += 1
        elif winner == "computer":
            self.computer_score += 1

    def display_score(self):
        """
        Displays the current score.
        """
        print("\n--- Score ---")
        print(f"You: {self.player_score}")
        print(f"Computer: {self.computer_score}")

    def play_game(self):
        """
        Plays the entire game.
        """
        print("Welcome to Rock-Paper-Scissors!")
        while True:
            self.play_round()
            self.display_score()

            play_again = input("Play again? (yes/no): ").lower()
            if play_again != "yes":
                break

        print("\nThanks for playing!")

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()