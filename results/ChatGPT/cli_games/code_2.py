import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.score = {'player': 0, 'computer': 0}

    def get_computer_choice(self):
        return random.choice(self.choices)

    def get_player_choice(self):
        choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        while choice not in self.choices and choice != 'quit':
            print("Invalid choice. Please try again.")
            choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        return choice

    def determine_winner(self, player, computer):
        if player == computer:
            return "It's a tie!"
        elif (player == 'rock' and computer == 'scissors') or \
             (player == 'paper' and computer == 'rock') or \
             (player == 'scissors' and computer == 'paper'):
            self.score['player'] += 1
            return "You win!"
        else:
            self.score['computer'] += 1
            return "Computer wins!"

    def play(self):
        print("Welcome to Rock-Paper-Scissors!")
        while True:
            player_choice = self.get_player_choice()
            if player_choice == 'quit':
                break
            computer_choice = self.get_computer_choice()
            print(f"Computer chose: {computer_choice}")
            result = self.determine_winner(player_choice, computer_choice)
            print(result)
            print(f"Score - You: {self.score['player']} | Computer: {self.score['computer']}")
        print("Thanks for playing!")

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play()