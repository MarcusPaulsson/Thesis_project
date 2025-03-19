import random
import time

class Boggle:
    """
    A class to represent the Boggle game.
    """

    def __init__(self, size=4, time_limit=180, dictionary_file="words.txt"):
        """
        Initializes the Boggle game.

        Args:
            size (int): The size of the Boggle board (default: 4).
            time_limit (int): The time limit for the game in seconds (default: 180).
            dictionary_file (str): The path to the dictionary file (default: "words.txt").
        """
        self.size = size
        self.time_limit = time_limit
        self.dictionary = self.load_dictionary(dictionary_file)
        self.board = self.generate_board()
        self.found_words = set()
        self.start_time = None
        self.game_over = False

    def load_dictionary(self, dictionary_file):
        """
        Loads the dictionary from a file.

        Args:
            dictionary_file (str): The path to the dictionary file.

        Returns:
            set: A set of words from the dictionary.
        """
        try:
            with open(dictionary_file, "r") as f:
                words = set(word.strip().upper() for word in f)
            return words
        except FileNotFoundError:
            print(f"Error: Dictionary file '{dictionary_file}' not found.")
            exit()

    def generate_board(self):
        """
        Generates the Boggle board.

        Returns:
            list: A 2D list representing the Boggle board.
        """
        dice = [
            "AAEEGN", "ELRTTY", "AOOTTW", "ABBJOO",
            "EHRTVW", "CIMOTU", "DISTTY", "EIOSST",
            "DELRVY", "ACHOPS", "HIMNQU", "EEINSV",
            "EEGHNW", "AFFKPS", "HLNNRZ", "DEILRX"
        ]
        board = []
        random.shuffle(dice)
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(random.choice(dice[i * self.size + j]))
            board.append(row)
        return board

    def display_board(self):
        """
        Displays the Boggle board in the console.
        """
        print("Boggle Board:")
        for row in self.board:
            print(" ".join(row))
        print()

    def is_valid_word(self, word):
        """
        Checks if a word is valid.

        Args:
            word (str): The word to check.

        Returns:
            bool: True if the word is valid, False otherwise.
        """
        word = word.upper()
        if len(word) < 3:
            return False
        if word in self.found_words:
            return False
        if word not in self.dictionary:
            return False
        return True

    def find_word_on_board(self, word):
        """
        Checks if a word can be found on the Boggle board.

        Args:
            word (str): The word to find.

        Returns:
            bool: True if the word can be found, False otherwise.
        """
        word = word.upper()
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == word[0]:
                    if self.search_word(word, row, col, 0, set()):
                        return True
        return False

    def search_word(self, word, row, col, index, visited):
        """
        Recursively searches for the word on the board.

        Args:
            word (str): The word to search for.
            row (int): The current row.
            col (int): The current column.
            index (int): The current index in the word.
            visited (set): A set of visited coordinates.

        Returns:
            bool: True if the word is found, False otherwise.
        """
        if index == len(word):
            return True

        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            return False

        if (row, col) in visited:
            return False

        if self.board[row][col] != word[index]:
            return False

        visited.add((row, col))

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                new_row = row + dr
                new_col = col + dc
                if self.search_word(word, new_row, new_col, index + 1, visited.copy()):
                    return True

        return False

    def play(self):
        """
        Runs the Boggle game.
        """
        self.start_time = time.time()
        self.display_board()

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

            if self.is_valid_word(word) and self.find_word_on_board(word):
                self.found_words.add(word.upper())
                print("Valid word!")
            else:
                print("Invalid word.")

        self.end_game()

    def end_game(self):
        """
        Ends the game and displays the results.
        """
        print("\nGame Over!")
        print("Words you found:")
        for word in sorted(self.found_words):
            print(word)
        print(f"\nTotal score: {len(self.found_words)}")


if __name__ == "__main__":
    game = Boggle()
    game.play()