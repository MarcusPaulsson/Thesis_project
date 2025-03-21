import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']

    def get_user_choice(self):
        user_input = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        if user_input in self.choices:
            return user_input
        elif user_input == 'quit':
            return None
        else:
            print("Invalid choice. Please try again.")
            return self.get_user_choice()

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            return "You win!"
        else:
            return "You lose!"

    def play(self):
        while True:
            user_choice = self.get_user_choice()
            if user_choice is None:
                print("Thanks for playing!")
                break
            computer_choice = self.get_computer_choice()
            print(f"Computer chose: {computer_choice}")
            result = self.determine_winner(user_choice, computer_choice)
            print(result)

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play()