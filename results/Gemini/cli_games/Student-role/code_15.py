import random
import time

class Boggle:
    """
    Represents a Boggle game.
    """

    def __init__(self, size=4, time_limit=180):
        """
        Initializes a Boggle game.

        Args:
            size (int): The size of the Boggle board (e.g., 4 for a 4x4 board).
            time_limit (int): The time limit for the game in seconds.
        """
        self.size = size
        self.time_limit = time_limit
        self.board = self.generate_board()
        self.words = set()  # Store valid words found by the player
        self.start_time = None
        self.end_time = None
        self.dictionary = self.load_dictionary("words.txt") # Load a dictionary file

    def load_dictionary(self, filepath):
      """Loads a dictionary from a text file.

      Args:
          filepath (str): The path to the dictionary file (one word per line).

      Returns:
          set: A set containing all words from the dictionary.
      """
      try:
          with open(filepath, 'r') as f:
              words = set(word.strip().upper() for word in f)
          return words
      except FileNotFoundError:
          print(f"Error: Dictionary file '{filepath}' not found.")
          return set()

    def generate_board(self):
        """
        Generates a random Boggle board.

        Returns:
            list[list[str]]: A 2D list representing the Boggle board.
        """
        dice = [
            "RIFOBX", "IFEHES", "DISEAS", "UIHMNU", "MHLRNO", "DLINOR",
            "HZLNOR", "AFSIRSY", "PORSEU", "TLAEPY", "GNILRU", "WABPDQ",
            "LNSEDT", "XLDERA", "QUMBMI", "AAEEGN"
        ]
        board = []
        random.shuffle(dice)
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(random.choice(dice[i * self.size + j]))
            board.append(row)
        return board

    def print_board(self):
        """
        Prints the Boggle board to the console.
        """
        for row in self.board:
            print(" ".join(row))

    def is_valid_word(self, word):
        """
        Checks if a word is a valid word in the dictionary.

        Args:
            word (str): The word to check.

        Returns:
            bool: True if the word is valid, False otherwise.
        """
        return word.upper() in self.dictionary and len(word) >= 3

    def find_word(self, word):
      """
      Checks if a word can be found on the Boggle board using adjacency rules (no reusing letters).

      Args:
          word (str): The word to search for.

      Returns:
          bool: True if the word is found, False otherwise.
      """

      def solve(row, col, word_index, path):
          if word_index == len(word):
              return True  # Found the entire word

          if row < 0 or row >= self.size or col < 0 or col >= self.size or (row, col) in path or self.board[row][col].upper() != word[word_index].upper():
              return False  # Invalid move

          # Explore neighbors
          neighbors = [
              (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
              (row, col - 1), (row, col + 1),
              (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)
          ]

          for nr, nc in neighbors:
              if solve(nr, nc, word_index + 1, path + [(row, col)]):
                  return True

          return False  # No path found from this cell

      # Check all cells on the board as starting points
      for row in range(self.size):
          for col in range(self.size):
              if solve(row, col, 0, []):
                  return True

      return False

    def play(self):
        """
        Plays the Boggle game.
        """
        print("Welcome to Boggle!")
        self.print_board()
        self.start_time = time.time()
        self.end_time = self.start_time + self.time_limit

        while time.time() < self.end_time:
            remaining_time = int(self.end_time - time.time())
            print(f"Time remaining: {remaining_time} seconds")
            word = input("Enter a word (or type 'quit' to end): ").strip()

            if word.lower() == "quit":
                break

            if self.is_valid_word(word) and self.find_word(word):
                if word.upper() not in self.words:
                    self.words.add(word.upper())
                    print("Valid word!")
                else:
                    print("You already found that word.")
            else:
                print("Invalid word.")

        print("Time's up!")
        self.end_game()

    def end_game(self):
        """
        Ends the Boggle game and displays the results.
        """
        print("Game Over!")
        print("Words you found:")
        for word in sorted(self.words):
            print(word)

        score = self.calculate_score()
        print(f"Your score: {score}")

    def calculate_score(self):
        """
        Calculates the player's score based on the words they found.

        Returns:
            int: The player's score.
        """
        score = 0
        for word in self.words:
            word_length = len(word)
            if word_length == 3 or word_length == 4:
                score += 1
            elif word_length == 5:
                score += 2
            elif word_length == 6:
                score += 3
            elif word_length == 7:
                score += 5
            elif word_length >= 8:
                score += 11
        return score


if __name__ == "__main__":
    # Create a dummy words.txt file if it doesn't exist.
    try:
        with open("words.txt", "r") as f:
            pass  # File exists, do nothing
    except FileNotFoundError:
        with open("words.txt", "w") as f:
            f.write("CAT\n")
            f.write("DOG\n")
            f.write("TEA\n")
            f.write("EAT\n")
            f.write("RAIN\n")
            f.write("TRAIN\n")
            f.write("EXAMPLE\n")
            f.write("ANOTHER\n")
            f.write("DICTIONARY\n")

    game = Boggle(size=4, time_limit=60)  # Adjust size and time limit as needed
    game.play()