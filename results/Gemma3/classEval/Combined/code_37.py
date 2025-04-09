class EncryptionUtils:
    """
    This is a class that provides methods for encryption, including the Caesar cipher, Vigenere cipher, and Rail Fence cipher.
    """

    def __init__(self, key):
        """
        Initializes the class with a key.
        :param key: The key to use for encryption, str.
        """
        self.key = key

    def caesar_cipher(self, plaintext, shift):
        """
        Encrypts the plaintext using the Caesar cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param shift: The number of characters to shift each character in the plaintext, int.
        :return: The ciphertext, str.
        """
        result = ''
        for char in plaintext:
            if 'a' <= char <= 'z':
                start = ord('a')
                shifted_char = chr((ord(char) - start + shift) % 26 + start)
            elif 'A' <= char <= 'Z':
                start = ord('A')
                shifted_char = chr((ord(char) - start + shift) % 26 + start)
            else:
                shifted_char = char
            result += shifted_char
        return result

    def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        """
        key = self.key
        result = ''
        key_len = len(key)
        for i, char in enumerate(plaintext):
            if 'a' <= char <= 'z':
                start = ord('a')
                key_char = key[i % key_len]
                key_shift = ord(key_char.lower()) - ord('a')
                shifted_char = chr((ord(char) - start + key_shift) % 26 + start)
            elif 'A' <= char <= 'Z':
                start = ord('A')
                key_char = key[i % key_len]
                key_shift = ord(key_char.lower()) - ord('a')
                shifted_char = chr((ord(char) - start + key_shift) % 26 + start)
            else:
                shifted_char = char
            result += shifted_char
        return result

    def rail_fence_cipher(self, plain_text, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plain_text: The plaintext to encrypt, str.
        :param rails: The number of rails to use, int.
        :return: The ciphertext, str.
        """
        if rails <= 1:
            return plain_text

        rail_matrix = [['' for _ in range(len(plain_text))] for _ in range(rails)]
        row, direction = 0, 1

        for i, char in enumerate(plain_text):
            rail_matrix[row][i] = char

            if row == 0:
                direction = 1
            elif row == rails - 1:
                direction = -1

            row += direction

        ciphertext = ''.join([''.join(row) for row in rail_matrix])
        return ciphertext