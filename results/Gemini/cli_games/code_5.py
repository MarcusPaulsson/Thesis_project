import random

def generate_secret_code(code_length=4, num_colors=6):
    """Generates a secret code with specified length and number of colors."""
    return [random.randint(1, num_colors) for _ in range(code_length)]

def get_user_guess(code_length=4, num_colors=6):
    """Gets a valid guess from the user."""
    while True:
        guess_str = input(f"Enter your guess (length {code_length}, colors 1-{num_colors}, separated by spaces): ")
        try:
            guess = [int(x) for x in guess_str.split()]
            if len(guess) != code_length:
                print(f"Invalid guess length.  Must be {code_length}.")
            elif any(x < 1 or x > num_colors for x in guess):
                print(f"Invalid color. Colors must be between 1 and {num_colors}.")
            else:
                return guess
        except ValueError:
            print("Invalid input.  Please enter numbers separated by spaces.")

def calculate_feedback(secret_code, guess):
    """Calculates the feedback for a guess."""
    correct_position = 0
    correct_color = 0
    temp_secret = secret_code[:]  # Create a copy to avoid modifying the original
    temp_guess = guess[:]

    # Check for correct positions first
    for i in range(len(secret_code)):
        if temp_secret[i] == temp_guess[i]:
            correct_position += 1
            temp_secret[i] = None  # Mark as matched
            temp_guess[i] = None  # Mark as matched

    # Check for correct colors in the wrong positions
    for i in range(len(secret_code)):
        if temp_guess[i] is not None:  # Only check unmatched colors
            if temp_guess[i] in temp_secret:
                correct_color += 1
                temp_secret[temp_secret.index(temp_guess[i])] = None  # Mark as matched

    return correct_position, correct_color

def play_mastermind(code_length=4, num_colors=6, max_attempts=10):
    """Plays a game of Mastermind."""
    secret_code = generate_secret_code(code_length, num_colors)
    attempts = 0

    print("Welcome to Mastermind!")
    print(f"I've generated a secret code with {code_length} colors (1-{num_colors}).")
    print(f"You have {max_attempts} attempts to guess the code.")

    while attempts < max_attempts:
        attempts += 1
        print(f"\nAttempt {attempts}:")
        guess = get_user_guess(code_length, num_colors)
        correct_position, correct_color = calculate_feedback(secret_code, guess)

        print(f"Feedback: {correct_position} correct position(s), {correct_color} correct color(s)")

        if correct_position == code_length:
            print(f"Congratulations! You guessed the code in {attempts} attempts.")
            return

    print(f"\nYou ran out of attempts. The secret code was: {secret_code}")

if __name__ == "__main__":
    play_mastermind()