import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.score = {'player': 0, 'computer': 0}

    def get_player_choice(self):
        choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        while choice not in self.choices and choice != 'quit':
            print("Invalid choice. Please try again.")
            choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        return choice

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return 'tie'
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            return 'player'
        else:
            return 'computer'

    def play(self):
        print("Welcome to Rock-Paper-Scissors!")
        while True:
            player_choice = self.get_player_choice()
            if player_choice == 'quit':
                print("Thanks for playing!")
                break
            
            computer_choice = self.get_computer_choice()
            print(f"Computer chose: {computer_choice}")

            winner = self.determine_winner(player_choice, computer_choice)
            if winner == 'tie':
                print("It's a tie!")
            elif winner == 'player':
                print("You win!")
                self.score['player'] += 1
            else:
                print("Computer wins!")
                self.score['computer'] += 1
            
            print(f"Score: Player {self.score['player']} - Computer {self.score['computer']}")

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play()