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
        ciphertext = ""
        for char in plaintext:
            if 'a' <= char <= 'z':
                shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            elif 'A' <= char <= 'Z':
                shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            else:
                shifted_char = char
            ciphertext += shifted_char
        return ciphertext

    def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        """
        ciphertext = ""
        key = self.key
        key_length = len(key)
        for i, char in enumerate(plaintext):
            if 'a' <= char <= 'z':
                key_char = key[i % key_length]
                shift = ord(key_char) - ord('a')
                shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            elif 'A' <= char <= 'Z':
                key_char = key[i % key_length]
                shift = ord(key_char.lower()) - ord('a')
                shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            else:
                shifted_char = char
            ciphertext += shifted_char
        return ciphertext

    def rail_fence_cipher(self, plain_text, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param rails: The number of rails to use, int.
        :return: The ciphertext, str.
        """
        if rails <= 1:
            return plain_text

        rail = [['' for _ in range(len(plain_text))]
                for _ in range(rails)]

        dir_down = False
        row, col = 0, 0

        for i in range(len(plain_text)):
            if row == 0 or row == rails - 1:
                dir_down = not dir_down

            rail[row][col] = plain_text[i]
            col += 1

            if dir_down:
                row += 1
            else:
                row -= 1

        result = ""
        for i in range(rails):
            for j in range(len(plain_text)):
                if rail[i][j] != '':
                    result += rail[i][j]
        return result