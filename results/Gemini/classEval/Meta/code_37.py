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
        >>> e = EncryptionUtils("key")
        >>> e.caesar_cipher("abc", 1)
        'bcd'

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
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'

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
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.rail_fence_cipher("abc", 2)
        'acb'

        """
        if rails <= 1:
            return plain_text

        rail_matrix = [['' for _ in range(len(plain_text))] for _ in range(rails)]
        row, direction = 0, 1

        for col in range(len(plain_text)):
            rail_matrix[row][col] = plain_text[col]

            row += direction

            if row == rails - 1:
                direction = -1
            elif row == 0:
                direction = 1

        ciphertext = ""
        for rail in rail_matrix:
            ciphertext += "".join(rail)

        ciphertext = ciphertext.replace("","") # Remove empty strings

        return ciphertext