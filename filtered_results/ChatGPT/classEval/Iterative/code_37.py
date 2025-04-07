class EncryptionUtils:
    """
    This is a class that provides methods for encryption, including the Caesar cipher, Vigenere cipher, and Rail Fence cipher.
    """

    def __init__(self, key):
        """
        Initializes the class with a key.
        :param key: The key to use for encryption, str.
        """
        self.key = key.lower()  # Ensure key is in lowercase for Vigenere cipher

    def caesar_cipher(self, plaintext, shift):
        """
        Encrypts the plaintext using the Caesar cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param shift: The number of characters to shift each character in the plaintext, int.
        :return: The ciphertext, str.
        """
        result = []
        shift %= 26  # Normalize shift to the range 0-25
        for char in plaintext:
            if char.isalpha():
                shift_base = ord('A') if char.isupper() else ord('a')
                result.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
            else:
                result.append(char)
        return ''.join(result)

    def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        """
        result = []
        key_length = len(self.key)
        key_index = 0

        for char in plaintext:
            if char.isalpha():
                shift_base = ord('A') if char.isupper() else ord('a')
                key_char = self.key[key_index % key_length]
                shift = ord(key_char) - ord('a')
                result.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
                key_index += 1
            else:
                result.append(char)

        return ''.join(result)

    def rail_fence_cipher(self, plain_text, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plain_text: The plaintext to encrypt, str.
        :param rails: The number of rails to use, int.
        :return: The ciphertext, str.
        """
        if rails <= 1:
            return plain_text

        rail = [['\n' for _ in range(len(plain_text))] for _ in range(rails)]
        direction_down = False
        row, col = 0, 0

        for char in plain_text:
            if row == 0 or row == rails - 1:
                direction_down = not direction_down

            rail[row][col] = char
            col += 1

            if direction_down:
                row += 1
            else:
                row -= 1

        result = []
        for r in rail:
            for char in r:
                if char != '\n':
                    result.append(char)

        return ''.join(result)