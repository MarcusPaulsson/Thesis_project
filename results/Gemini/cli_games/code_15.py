import random
import time

class Boggle:
    """
    A class to represent and play the Boggle game.
    """

    def __init__(self, size=4, dictionary_file="words.txt"):
        """
        Initializes the Boggle game.

        Args:
            size (int): The size of the Boggle board (default is 4).
            dictionary_file (str): The path to the dictionary file (default is "words.txt").
        """
        self.size = size
        self.board = [['' for _ in range(size)] for _ in range(size)]
        self.dictionary = self.load_dictionary(dictionary_file)
        self.words_found = set()
        self.game_over = False
        self.start_time = None
        self.time_limit = 180  # 3 minutes

    def load_dictionary(self, dictionary_file):
        """
        Loads the dictionary from the given file.

        Args:
            dictionary_file (str): The path to the dictionary file.

        Returns:
            set: A set of words from the dictionary.
        """
        try:
            with open(dictionary_file, "r") as f:
                return set(word.strip().upper() for word in f)
        except FileNotFoundError:
            print(f"Error: Dictionary file '{dictionary_file}' not found.")
            exit(1)

    def generate_board(self):
        """
        Generates a random Boggle board. Uses standard Boggle dice for letter distribution.
        """
        dice = [
            "RIFOBX", "IFEHEE", "ENSIEU", "UTDNIO",
            "HMQUOB", "LNWODJ", "AREVLD", "HOSPNI",
            "TLESRA", "ATOOET", "HLNRZD", "NNIAEE",
            "DGNOTU", "AACIOT", "AIOEFR", "EEIHNS"
        ]

        if self.size != 4:  # Generalization for different sizes would require appropriate dice
            print("Warning: Using standard dice for non-4x4 board. Letter distribution may be inaccurate.")

        for i in range(self.size):
            for j in range(self.size):
                die = random.choice(dice)
                self.board[i][j] = random.choice(die)

    def print_board(self):
        """
        Prints the current Boggle board to the console.
        """
        print("Boggle Board:")
        for row in self.board:
            print(" ".join(row))
        print()

    def is_valid_word(self, word):
        """
        Checks if a word is valid according to Boggle rules and the dictionary.

        Args:
            word (str): The word to check.

        Returns:
            bool: True if the word is valid, False otherwise.
        """
        if len(word) < 3:
            return False
        if word not in self.dictionary:
            return False
        if word in self.words_found:
            return False
        return True

    def find_word_on_board(self, word):
        """
        Checks if a word can be found on the Boggle board using adjacent letters.

        Args:
            word (str): The word to search for.

        Returns:
            bool: True if the word can be found, False otherwise.
        """

        def search(row, col, word_index, path):
            """
            Recursive helper function to search for the word.
            """
            if word_index == len(word):
                return True

            if row < 0 or row >= self.size or col < 0 or col >= self.size:
                return False

            if self.board[row][col] != word[word_index]:
                return False

            if (row, col) in path:
                return False  # Prevent cycles

            new_path = path + [(row, col)]

            # Explore adjacent cells
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue #Skip current cell

                    if search(row + dr, col + dc, word_index + 1, new_path):
                        return True

            return False

        for row in range(self.size):
            for col in range(self.size):
                if search(row, col, 0, []):
                    return True

        return False

    def add_word(self, word):
          """
          Adds a word to the list of found words if it's valid and on the board.
          """
          word = word.upper()
          if self.is_valid_word(word) and self.find_word_on_board(word):
              self.words_found.add(word)
              print(f"Word '{word}' found!")
          else:
              print(f"Word '{word}' is not valid or cannot be found on the board.")

    def calculate_score(self):
        """
        Calculates the player's score based on the length of the words found.
        """
        score = 0
        for word in self.words_found:
            length = len(word)
            if length == 3 or length == 4:
                score += 1
            elif length == 5:
                score += 2
            elif length == 6:
                score += 3
            elif length == 7:
                score += 5
            elif length >= 8:
                score += 11
        return score

    def play_game(self):
        """
        The main game loop.
        """
        self.generate_board()
        self.print_board()
        self.words_found = set()
        print("Game started! You have 3 minutes to find words.")
        self.start_time = time.time()

        while not self.game_over:
            elapsed_time = time.time() - self.start_time
            remaining_time = self.time_limit - elapsed_time

            if remaining_time <= 0:
                self.game_over = True
                print("Time's up!")
                break

            print(f"Time remaining: {int(remaining_time)} seconds")
            word = input("Enter a word (or type 'quit' to end): ").strip()

            if word.lower() == "quit":
                self.game_over = True
                break

            self.add_word(word)

        score = self.calculate_score()
        print("\nGame Over!")
        print("Words found:", ", ".join(sorted(self.words_found)))
        print("Your score:", score)

if __name__ == "__main__":
    game = Boggle()
    game.play_game()