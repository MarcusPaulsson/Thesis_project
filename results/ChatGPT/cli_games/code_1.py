import random

def choose_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'interface', 'computer', 'science', 'development']
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        """,
        """
           ------
           |    |
           |
           |
           |
           |
        """,
        """
           ------
           |    |
           |
           |
           |
           |
        """
    ]
    return stages[tries]

def play_hangman():
    word = choose_word()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6

    print("Welcome to Hangman!")
    
    while tries > 0 and word_letters != guessed_letters:
        print(display_hangman(tries))
        print("Guessed letters: ", ' '.join(guessed_letters))
        word_display = [letter if letter in guessed_letters else '_' for letter in word]
        print("Current word: ", ' '.join(word_display))

        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word_letters:
            tries -= 1
            print(f"Wrong guess! You have {tries} tries left.")
        else:
            print("Good guess!")

    if word_letters == guessed_letters:
        print(f"Congratulations! You've guessed the word: {word}")
    else:
        print(display_hangman(tries))
        print(f"Sorry, you lost! The word was: {word}")

if __name__ == "__main__":
    play_hangman()