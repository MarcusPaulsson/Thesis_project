import random

def get_user_choice():
    user_input = input("Enter Rock, Paper, or Scissors (or 'quit' to exit): ").strip().lower()
    if user_input in ['rock', 'paper', 'scissors']:
        return user_input
    elif user_input == 'quit':
        return None
    else:
        print("Invalid choice. Please try again.")
        return get_user_choice()

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    while True:
        user_choice = get_user_choice()
        if user_choice is None:
            print("Thank you for playing!")
            break
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")
        result = determine_winner(user_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    play_game()