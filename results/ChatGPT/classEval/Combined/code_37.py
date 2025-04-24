class EncryptionUtils:
    """
    This class provides methods for encryption, including the Caesar cipher, Vigenere cipher, and Rail Fence cipher.
    """

    def __init__(self, key: str):
        """
        Initializes the class with a key.
        :param key: The key to use for encryption, str.
        """
        self.key = key.lower()  # Store the key in lowercase for consistent processing

    def caesar_cipher(self, plaintext: str, shift: int) -> str:
        """
        Encrypts the plaintext using the Caesar cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param shift: The number of characters to shift each character in the plaintext, int.
        :return: The ciphertext, str.
        """
        shift %= 26  # Normalize shift to be within 0-25
        ciphertext = []

        for char in plaintext:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                new_char = chr((ord(char) - base + shift) % 26 + base)
                ciphertext.append(new_char)
            else:
                ciphertext.append(char)

        return ''.join(ciphertext)

    def vigenere_cipher(self, plaintext: str) -> str:
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        """
        ciphertext = []
        key_length = len(self.key)
        key_index = 0

        for char in plaintext:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                key_char = self.key[key_index % key_length]
                shift = ord(key_char) - ord('a')
                new_char = chr((ord(char) - base + shift) % 26 + base)
                ciphertext.append(new_char)
                key_index += 1
            else:
                ciphertext.append(char)

        return ''.join(ciphertext)

    def rail_fence_cipher(self, plaintext: str, rails: int) -> str:
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param rails: The number of rails to use, int.
        :return: The ciphertext, str.
        """
        if rails <= 1:
            return plaintext

        rail = [''] * rails
        direction_down = False
        row = 0

        for char in plaintext:
            rail[row] += char
            if row == 0 or row == rails - 1:
                direction_down = not direction_down
            row += 1 if direction_down else -1

        return ''.join(rail)