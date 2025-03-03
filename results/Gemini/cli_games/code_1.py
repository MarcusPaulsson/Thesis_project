import random

def choose_word():
    """Chooses a random word from a predefined list."""
    words = ["python", "hangman", "programming", "computer", "algorithm", "developer", "software", "interface", "keyboard", "monitor"]
    return random.choice(words)

def display_word(word, guessed_letters):
    """Displays the word with correctly guessed letters and underscores for unguessed letters."""
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

def hangman():
    """Implements the Hangman game logic."""

    word_to_guess = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # Number of incorrect guesses allowed
    game_over = False

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))
    print(f"You have {max_incorrect_guesses} incorrect guesses remaining.")

    while not game_over:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print("Correct guess!")
            displayed_word = display_word(word_to_guess, guessed_letters)
            print(displayed_word)

            if "_" not in displayed_word:
                print("Congratulations! You guessed the word:", word_to_guess)
                game_over = True
        else:
            incorrect_guesses += 1
            print("Incorrect guess.")
            print(f"You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses remaining.")

            # Simple hangman drawing based on incorrect guesses
            if incorrect_guesses == 1:
                print("  O  ")
            elif incorrect_guesses == 2:
                print("  O  ")
                print("  |  ")
            elif incorrect_guesses == 3:
                print("  O  ")
                print(" /|  ")
            elif incorrect_guesses == 4:
                print("  O  ")
                print(" /|\ ")
            elif incorrect_guesses == 5:
                print("  O  ")
                print(" /|\ ")
                print(" /   ")
            elif incorrect_guesses == 6:
                print("  O  ")
                print(" /|\ ")
                print(" / \ ")
                print("You ran out of guesses. The word was:", word_to_guess)
                game_over = True

        if incorrect_guesses >= max_incorrect_guesses:
            game_over = True

if __name__ == "__main__":
    hangman()