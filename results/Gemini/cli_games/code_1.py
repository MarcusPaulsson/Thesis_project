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
        if not guess.isalpha():
            print("Invalid input. Please enter a letter.")
        elif len(guess) != 1:
            print("Please enter only one letter at a time.")
        elif guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        else:
            return guess

def play_hangman(word_list):
    """Plays a game of Hangman."""
    word = choose_word(word_list)
    guessed_letters = set()
    incorrect_guesses = 0
    max_guesses = 6  # You can adjust the number of allowed incorrect guesses.

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))
    print(f"You have {max_guesses} guesses.")

    while incorrect_guesses < max_guesses:
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print("Correct guess!")
            display = display_word(word, guessed_letters)
            print(display)

            if "_" not in display:
                print("Congratulations! You guessed the word:", word)
                return

        else:
            incorrect_guesses += 1
            print("Incorrect guess.")
            print(f"You have {max_guesses - incorrect_guesses} guesses remaining.")
            print(display_word(word, guessed_letters)) # Show progress even after incorrect guess

        if incorrect_guesses == max_guesses:
            print("You ran out of guesses. The word was:", word)
            return

def main():
    """Main function to start the game."""
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"] # Add more words!
    play_hangman(word_list)

if __name__ == "__main__":
    main()