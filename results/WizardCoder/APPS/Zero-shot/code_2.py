import random

class Game:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']

    def get_player_choice(self):
        player_choice = input("Enter your choice (rock, paper, scissors): ")
        if player_choice in self.choices:
            return player_choice
        else:
            print('Invalid input!')
            return None
    
    def get_computer_choice(self):
        computer_choice = random.choice(self.choices)
        return computer_choice
    
    def determine_winner(self, player_choice, computer_choice):
        if (player_choice == 'rock' and computer_choice == 'scissors') or (player_choice == 'paper' and computer_choice == 'rock') or (player_choice == 'scissors' and computer_choice == 'paper'):
            return f"Player wins! {player_choice} beats {computer_choice}"
        elif player_choice == computer_choice:
            return "It's a tie!"
        else:
            return f"Computer wins! {computer_choice} beats {player_choice}"
    
    def play(self):
        player_wins = 0
        computer_wins = 0
        while True:
            player_choice = self.get_player_choice()
            if not player_choice:
                continue
            computer_choice = self.get_computer_choice()
            print(f"Computer chose {computer_choice}")
            winner = self.determine_winner(player_choice, computer_choice)
            print(winner)
            if 'Player' in winner:
                player_wins += 1
            elif 'Computer' in winner:
                computer_wins += 1
            else:
                continue # tie game
            break
        
        print(f"Final Score:")
        print(f"Player: {player_wins}")
        print(f"Computer: {computer_wins}")

game = Game()
game.play()