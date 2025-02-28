import random

def get_player_choice():
    """Gets the player's choice from the command line."""
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
    """Generates a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
    """Determines the winner of the game."""
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_again():
    """Asks the player if they want to play again."""
    while True:
        choice = input("Play again? (yes/no): ").lower()
        if choice in ["yes", "no"]:
            return choice == "yes"
        else:
            print("Invalid input. Please enter yes or no.")

def main():
    """The main function that runs the game."""
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)
        print(result)

        if not play_again():
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()