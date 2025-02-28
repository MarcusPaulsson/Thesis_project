import random

def choose_word(word_list):
    """Chooses a random word from a list of words."""
    return random.choice(word_list).upper()

def display_word(word, guessed_letters):
    """Displays the word with correctly guessed letters and underscores for unguessed letters."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def get_guess(guessed_letters):
    """Gets a valid letter guess from the user."""
    while True:
        guess = input("Guess a letter: ").upper()
        if len(guess) != 1:
            print("Please enter only one letter.")
        elif not guess.isalpha():
            print("Please enter a letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            return guess

def play_hangman(word_list):
    """Plays a game of Hangman."""
    word = choose_word(word_list)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    game_over = False

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while not game_over:
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print("Correct!")
            display = display_word(word, guessed_letters)
            print(display)

            if "_" not in display:
                print("Congratulations! You guessed the word:", word)
                game_over = True
        else:
            incorrect_guesses += 1
            print("Incorrect guess.")
            print(f"You have {max_incorrect_guesses - incorrect_guesses} guesses remaining.")

            if incorrect_guesses >= max_incorrect_guesses:
                print("You ran out of guesses. The word was:", word)
                game_over = True

        print()  # Add a newline for better readability


def main():
    """Main function to start the game."""
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]  # Add more words to the list as desired

    while True:
        play_hangman(word_list)

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()