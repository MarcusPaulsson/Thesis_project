import random

def get_player_choice():
    """Gets the player's choice (rock, paper, or scissors)."""
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    """Generates a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
    """Determines the winner of the game."""
    print(f"You chose: {player_choice}")
    print(f"The computer chose: {computer_choice}")

    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Plays a single round of Rock-Paper-Scissors."""
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)
    print(result)

def main():
    """Main function to run the game."""
    while True:
        play_game()
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    main()