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
        self.words_found = set()
        self.start_time = None

    def load_dictionary(self, dictionary_file):
        """
        Loads the dictionary from a file.

        Args:
            dictionary_file (str): The path to the dictionary file.

        Returns:
            set: A set containing all words in the dictionary.
        """
        try:
            with open(dictionary_file, "r") as f:
                words = set(word.strip().upper() for word in f)
            return words
        except FileNotFoundError:
            print(f"Error: Dictionary file '{dictionary_file}' not found.")
            exit(1)

    def generate_board(self):
        """
        Generates a random Boggle board.

        Returns:
            list: A 2D list representing the Boggle board.
        """
        dice = [
            "RIFOBX", "IFEHSE", "DIENPS", "UMNNNH",
            "ETGLRU", "ACDJOV", "ACULMN", "DGILNU",
            "AHIMOR", "EEGHNW", "AFFKPS", "HLNNRZ",
            "DEILRX", "DELRVY", "AISTYB", "CEILPT"
        ]
        board = []
        for _ in range(self.size):
            row = []
            for _ in range(self.size):
                die = random.choice(dice)
                row.append(random.choice(die))
            board.append(row)
        return board

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
        Checks if a word is valid (in the dictionary and not already found).

        Args:
            word (str): The word to check.

        Returns:
            bool: True if the word is valid, False otherwise.
        """
        return (word in self.dictionary and
                word not in self.words_found and
                len(word) >= 3)

    def find_words_recursive(self, row, col, word, visited):
        """
        Recursively finds words on the board starting from a given cell.

        Args:
            row (int): The row of the current cell.
            col (int): The column of the current cell.
            word (str): The current word being formed.
            visited (set): A set of visited cells (row, col).

        """
        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            return

        if (row, col) in visited:
            return

        letter = self.board[row][col]
        new_word = word + letter

        if not any(w.startswith(new_word) for w in self.dictionary):
            return  # Prune search if no word starts with the current prefix

        if self.is_valid_word(new_word):
            self.words_found.add(new_word)

        visited.add((row, col))

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                self.find_words_recursive(row + i, col + j, new_word, visited.copy())
                #visited.remove((row+i, col+j)) #backtrack

    def solve_board(self):
        """
        Finds all possible words on the board.
        """
        for row in range(self.size):
            for col in range(self.size):
                self.find_words_recursive(row, col, "", set())

    def play(self):
        """
        Starts and runs the Boggle game.
        """
        self.print_board()
        self.start_time = time.time()
        print(f"You have {self.time_limit} seconds to find words.  Good luck!")
        print("Enter words (or 'quit' to end):")

        while time.time() - self.start_time < self.time_limit:
            remaining_time = int(self.time_limit - (time.time() - self.start_time))
            print(f"Time remaining: {remaining_time} seconds", end='\r')
            word = input().strip().upper()

            if word == "QUIT":
                break

            if self.is_valid_word(word):
                self.words_found.add(word)
                print("Good!")
            else:
                print("Invalid word. Try again.")

        print("\nTime's up!")
        self.end_game()

    def calculate_score(self):
        """
        Calculates the player's score based on the length of the words found.

        Returns:
            int: The player's score.
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

    def end_game(self):
        """
        Ends the game, displays the results, and calculates the score.
        """
        print("Your words:", ", ".join(sorted(self.words_found)))
        score = self.calculate_score()
        print("Your score:", score)

        self.solve_board()
        print("\nPossible words:", ", ".join(sorted(self.words_found)))

        #Find all words that the player didn't find
        missed_words = [word for word in self.words_found if word not in self.words_found]
        print("\nMissed words:", ", ".join(sorted(missed_words)))

if __name__ == "__main__":
    game = Boggle()
    game.play()