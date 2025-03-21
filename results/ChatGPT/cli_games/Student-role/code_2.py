import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.wins = 0
        self.losses = 0
        self.ties = 0

    def play_round(self, user_choice):
        if user_choice not in self.choices:
            return "Invalid choice! Please choose rock, paper, or scissors."

        computer_choice = random.choice(self.choices)
        result = self.determine_winner(user_choice, computer_choice)
        return f"You chose {user_choice}, Computer chose {computer_choice}. {result}"

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            self.ties += 1
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            self.wins += 1
            return "You win!"
        else:
            self.losses += 1
            return "You lose!"

    def get_score(self):
        return f"Wins: {self.wins}, Losses: {self.losses}, Ties: {self.ties}"

def main():
    game = RockPaperScissors()
    while True:
        user_input = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        if user_input == 'quit':
            print("Thanks for playing!")
            break
        result = game.play_round(user_input)
        print(result)
        print(game.get_score())

if __name__ == "__main__":
    main()