import random
import time

class Boggle:
    """
    A class to represent a Boggle game.
    """

    def __init__(self, size=4, time_limit=180):
        """
        Initializes a Boggle game.

        Args:
            size (int): The size of the Boggle board (default: 4).
            time_limit (int): The time limit for the game in seconds (default: 180).
        """

        self.size = size
        self.time_limit = time_limit
        self.board = self.generate_board()
        self.dictionary = self.load_dictionary("words.txt")  # Ensure words.txt exists in the same directory
        self.words_found = set()
        self.start_time = None
        self.game_over = False

    def generate_board(self):
        """
        Generates a random Boggle board.

        Returns:
            list: A list of lists representing the Boggle board.
        """

        dice = [
            "RIFOBX", "IFEHEE", "ENSIEU", "LUPETD", "AYOBKR",
            "TDOENS", "IMTOCC", "GNWHGE", "LRYTTK", "EOAHIS",
            "XLDERI", "SAPNZI", "UOTOWN", "HSAOFW", "MTOICU", "ETNIAS"
        ]
        random.shuffle(dice)
        board = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(random.choice(dice[i * self.size + j]))
            board.append(row)
        return board

    def load_dictionary(self, filename="words.txt"):
        """
        Loads a dictionary of valid words from a file.

        Args:
            filename (str): The name of the file containing the dictionary (default: "words.txt").

        Returns:
            set: A set of valid words.
        """
        try:
            with open(filename, "r") as f:
                words = set(word.strip().upper() for word in f)
            return words
        except FileNotFoundError:
            print(f"Error: The dictionary file '{filename}' was not found.")
            print("Please ensure 'words.txt' exists in the same directory as the script.")
            exit()


    def print_board(self):
        """
        Prints the Boggle board to the console.
        """

        for row in self.board:
            print(" ".join(row))

    def is_valid_word(self, word):
        """
        Checks if a word is valid according to Boggle rules.

        Args:
            word (str): The word to check.

        Returns:
            bool: True if the word is valid, False otherwise.
        """

        word = word.upper()
        if len(word) < 3:
            return False
        if word in self.words_found:
            return False
        if word not in self.dictionary:
            return False
        return True

    def find_word_on_board(self, word):
        """
        Checks if a word can be found on the Boggle board.

        Args:
            word (str): The word to search for.

        Returns:
            bool: True if the word can be found, False otherwise.
        """

        word = word.upper()

        def search(row, col, index, path):
            if index == len(word):
                return True

            if row < 0 or row >= self.size or col < 0 or col >= self.size:
                return False

            if (row, col) in path:
                return False

            if self.board[row][col] != word[index]:
                return False

            path.add((row, col))
            found = (
                search(row - 1, col - 1, index + 1, path.copy()) or
                search(row - 1, col, index + 1, path.copy()) or
                search(row - 1, col + 1, index + 1, path.copy()) or
                search(row, col - 1, index + 1, path.copy()) or
                search(row, col + 1, index + 1, path.copy()) or
                search(row + 1, col - 1, index + 1, path.copy()) or
                search(row + 1, col, index + 1, path.copy()) or
                search(row + 1, col + 1, index + 1, path.copy())
            )
            path.remove((row, col)) # Backtrack
            return found

        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == word[0]:
                    if search(row, col, 0, set()):
                        return True
        return False

    def play_turn(self):
        """
        Plays a single turn of the game.
        """

        elapsed_time = time.time() - self.start_time
        remaining_time = self.time_limit - elapsed_time

        if remaining_time <= 0:
            print("Time's up!")
            self.game_over = True
            return

        print(f"Time remaining: {int(remaining_time)} seconds")
        word = input("Enter a word: ").strip()

        if not word:
            return

        if self.is_valid_word(word) and self.find_word_on_board(word):
            self.words_found.add(word.upper())
            print("Valid word!")
        else:
            print("Invalid word.")

    def calculate_score(self):
        """
        Calculates the player's score based on the words found.

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
            else:
                score += 11
        return score

    def play_game(self):
        """
        Plays the Boggle game.
        """

        print("Welcome to Boggle!")
        self.print_board()
        self.start_time = time.time()

        while not self.game_over:
            self.play_turn()
            if time.time() - self.start_time >= self.time_limit:
                self.game_over = True

        score = self.calculate_score()
        print("Game over!")
        print(f"Your score: {score}")
        print("Words found:")
        for word in sorted(self.words_found):
            print(word)


if __name__ == "__main__":
    # Create a dummy words.txt file for testing
    with open("words.txt", "w") as f:
        f.write("CAT\n")
        f.write("DOG\n")
        f.write("TEA\n")
        f.write("EAT\n")
        f.write("RAIN\n")
        f.write("TRAIN\n")
        f.write("ELEPHANT\n")
        f.write("COMPUTER\n")


    game = Boggle()
    game.play_game()