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
            if char.isalpha():
                start = ord('a') if char.islower() else ord('A')
                shifted_char = chr((ord(char) - start + shift) % 26 + start)
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
            if char.isalpha():
                key_char = key[i % key_length]
                key_shift = ord(key_char.lower()) - ord('a')
                start = ord('a') if char.islower() else ord('A')
                shifted_char = chr((ord(char) - start + key_shift) % 26 + start)
            else:
                shifted_char = char
            ciphertext += shifted_char
        return ciphertext

    def rail_fence_cipher(self,plain_text, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.rail_fence_cipher("abc", 2)
        'acb'

        """
        rail = [""] * rails
        direction = 1
        row = 0

        for char in plain_text:
            rail[row] += char
            row += direction

            if row == rails:
                row = rails - 2
                direction = -1
            elif row == -1:
                row = 1
                direction = 1

        return "".join(rail)