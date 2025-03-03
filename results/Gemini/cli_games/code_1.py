import random

def choose_word(word_list):
    """Chooses a random word from a list of words."""
    return random.choice(word_list).upper()

def display_word(word, guessed_letters):
    """Displays the word with correctly guessed letters and underscores for unguessed letters."""
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

def get_guess(guessed_letters):
    """Gets a valid letter guess from the player."""
    while True:
        guess = input("Guess a letter: ").upper()
        if not guess.isalpha():
            print("Invalid input. Please enter a letter.")
        elif len(guess) != 1:
            print("Please guess only one letter at a time.")
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            return guess

def play_hangman(word_list):
    """Plays a game of Hangman."""
    word = choose_word(word_list)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # You can adjust this
    game_over = False

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    print(display_word(word, guessed_letters))

    while not game_over:
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print("Correct guess!")
            displayed = display_word(word, guessed_letters)
            print(displayed)

            if "_" not in displayed:
                print("Congratulations! You guessed the word:", word)
                game_over = True
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess. You have {max_incorrect_guesses - incorrect_guesses} guesses remaining.")
            print(display_word(word, guessed_letters))

            if incorrect_guesses >= max_incorrect_guesses:
                print("You ran out of guesses. The word was:", word)
                game_over = True

def main():
    """Main function to start the Hangman game."""
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    play_again = True

    while play_again:
        play_hangman(word_list)
        response = input("Play again? (yes/no): ").lower()
        if response != "yes":
            play_again = False
            print("Thanks for playing!")

if __name__ == "__main__":
    main()