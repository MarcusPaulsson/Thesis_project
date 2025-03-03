import random

def get_player_choice():
    """Gets the player's choice (rock, paper, or scissors) from the command line."""
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
    """Randomly selects the computer's choice (rock, paper, or scissors)."""
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

def play_again():
    """Asks the player if they want to play again."""
    while True:
        answer = input("Play again? (yes/no): ").lower()
        if answer in ["yes", "no"]:
            return answer == "yes"
        else:
            print("Invalid input. Please enter yes or no.")

def play_game():
    """Main function to play the Rock-Paper-Scissors game."""
    print("Welcome to Rock-Paper-Scissors!")

    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)
        print(result)

        if not play_again():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()