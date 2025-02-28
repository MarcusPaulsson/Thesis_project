import random

def choose_word():
    word_list = ["python", "hangman", "challenge", "programming", "software"]
    return random.choice(word_list)

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
           |    
           |    
           |    
           |   
           |
        """,
        """
           ------
           |    
           |    
           |    
           |   
           |
        """,
    ]
    return stages[tries]

def play():
    word = choose_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter.")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word.")
                guessed_letters.append(guess)
                word_completion = "".join(
                    [letter if letter in guessed_letters else "_" for letter in word]
                )
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You've already guessed that word.")
            elif guess != word:
                print(f"{guess} is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid input. Please try again.")

        print(display_hangman(tries))
        print(word_completion)

    if guessed:
        print("Congratulations! You've guessed the word!")
    else:
        print(f"Sorry, you've run out of tries. The word was '{word}'.")

if __name__ == "__main__":
    play()