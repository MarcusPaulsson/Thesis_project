import random
import time
import sys

class Boggle:
    """
    A class to represent a Boggle game.
    """

    def __init__(self, size=4, time_limit=180):
        """
        Initializes a new Boggle game.

        Args:
            size (int): The size of the Boggle board (size x size). Defaults to 4.
            time_limit (int): The time limit for the game in seconds. Defaults to 180.
        """
        self.size = size
        self.time_limit = time_limit
        self.board = self.generate_board()
        self.dictionary = self.load_dictionary("dictionary.txt")  # Ensure dictionary.txt exists
        self.found_words = set()
        self.start_time = 0
        self.game_over = False

    def generate_board(self):
        """
        Generates a random Boggle board.

        Returns:
            list[list[str]]: A 2D list representing the Boggle board.
        """
        dice = [
            "RIFOBX", "IFEHEE", "PTDHIS", "LNNZNH", "TOEUIS", "SIAETI",
            "UMQOJI", "EHIFSE", "ELRTTY", "ACHOPS", "SPHDEE", "VCLPTU",
            "AENNNG", "LETSAS", "BGLRYY", "AAEEGN"
        ]
        if self.size > 4:
            dice = dice + [
                "RIFOBX", "IFEHEE", "PTDHIS", "LNNZNH", "TOEUIS", "SIAETI",
                "UMQOJI", "EHIFSE", "ELRTTY", "ACHOPS", "SPHDEE", "VCLPTU",
                "AENNNG", "LETSAS", "BGLRYY", "AAEEGN"
            ][: self.size * self.size - 16]

        random.shuffle(dice)
        board = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                die = dice[i * self.size + j]
                row.append(random.choice(die))
            board.append(row)
        return board

    def load_dictionary(self, filename="dictionary.txt"):
        """
        Loads a dictionary of valid words from a file.

        Args:
            filename (str): The name of the dictionary file. Defaults to "dictionary.txt".

        Returns:
            set[str]: A set of valid words.
        """
        try:
            with open(filename, "r") as file:
                words = {word.strip().upper() for word in file}
            return words
        except FileNotFoundError:
            print(f"Error: Dictionary file '{filename}' not found.")
            sys.exit(1)

    def print_board(self):
        """
        Prints the Boggle board to the console.
        """
        print("Boggle Board:")
        for row in self.board:
            print(" ".join(row))
        print()

    def is_valid_word(self, word):
        """
        Checks if a word is a valid word in the dictionary and has not been found yet.

        Args:
            word (str): The word to check.

        Returns:
            bool: True if the word is valid, False otherwise.
        """
        word = word.upper()
        return (
            word in self.dictionary
            and word not in self.found_words
            and len(word) >= 3  # Minimum word length
        )

    def find_word_on_board(self, word):
        """
        Checks if a word can be found on the Boggle board using a depth-first search.

        Args:
            word (str): The word to find.

        Returns:
            bool: True if the word is found, False otherwise.
        """
        word = word.upper()
        for row in range(self.size):
            for col in range(self.size):
                if self._find_word_recursive(word, row, col, 0, set()):
                    return True
        return False

    def _find_word_recursive(self, word, row, col, index, visited):
        """
        Recursive helper function for find_word_on_board.

        Args:
            word (str): The word to find.
            row (int): The current row index.
            col (int): The current column index.
            index (int): The current index in the word.
            visited (set[tuple[int, int]]): A set of visited cells.

        Returns:
            bool: True if the word is found, False otherwise.
        """
        if index == len(word):
            return True

        if (
            row < 0
            or row >= self.size
            or col < 0
            or col >= self.size
            or (row, col) in visited
            or self.board[row][col] != word[index]
        ):
            return False

        visited.add((row, col))

        # Explore neighbors
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                if self._find_word_recursive(word, row + dr, col + dc, index + 1, visited.copy()):
                    return True

        return False

    def start_game(self):
        """
        Starts the Boggle game.
        """
        self.found_words = set()
        self.start_time = time.time()
        self.game_over = False

        print("Welcome to Boggle!")
        self.print_board()
        print(f"You have {self.time_limit} seconds to find words.")

        while not self.game_over:
            elapsed_time = time.time() - self.start_time
            remaining_time = max(0, self.time_limit - elapsed_time)
            print(f"Time remaining: {int(remaining_time)} seconds")

            if remaining_time == 0:
                self.end_game()
                break

            word = input("Enter a word (or 'quit' to end): ").strip()

            if word.lower() == "quit":
                self.end_game()
                break

            if self.is_valid_word(word) and self.find_word_on_board(word):
                self.found_words.add(word.upper())
                print("Valid word!")
            else:
                print("Invalid word.")

    def calculate_score(self):
        """
        Calculates the player's score based on the found words.

        Returns:
            int: The player's score.
        """
        score = 0
        for word in self.found_words:
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

    def end_game(self):
        """
        Ends the Boggle game and displays the results.
        """
        self.game_over = True
        print("\nTime's up!")
        print("Words you found:")
        for word in sorted(self.found_words):
            print(word)

        score = self.calculate_score()
        print(f"\nYour score: {score}")

        # Find words the player missed (optional)
        missed_words = self.find_all_words() - self.found_words

        if missed_words:
            print("\nPossible words you missed:")
            for word in sorted(missed_words):
                print(word)


    def find_all_words(self):
        """
        Finds all possible words on the board using the dictionary.  This is very slow and
        should only be called at the end of the game.

        Returns:
            set[str]: A set of all possible words.
        """
        all_words = set()
        for word in self.dictionary:
            if self.find_word_on_board(word):
                all_words.add(word)
        return all_words


if __name__ == "__main__":
    # Example usage:
    game = Boggle(size=4, time_limit=60)  # You can adjust size and time limit
    game.start_game()