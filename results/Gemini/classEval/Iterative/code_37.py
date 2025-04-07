class EncryptionUtils:
    """
    This class provides methods for encryption, including the Caesar cipher, Vigenere cipher, and Rail Fence cipher.
    """

    def __init__(self, key):
        """
        Initializes the class with a key.
        :param key: The key to use for encryption, str.  Should be non-empty for Vigenere.
        :raises ValueError: if key is empty for Vigenere cipher.
        """
        self.key = key
        if not self.key and hasattr(self, 'vigenere_cipher'):
            raise ValueError("Key cannot be empty for Vigenere cipher.")


    def caesar_cipher(self, plaintext, shift):
        """
        Encrypts the plaintext using the Caesar cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param shift: The number of characters to shift each character in the plaintext, int.
                      Can be positive or negative.
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
                key_shift = ord(key_char.lower()) - ord('a')
                shifted_char = chr(((ord(char) - ord('a') + key_shift) % 26) + ord('a'))
            elif 'A' <= char <= 'Z':
                key_char = key[i % key_length]
                key_shift = ord(key_char.lower()) - ord('a')
                shifted_char = chr(((ord(char) - ord('A') + key_shift) % 26) + ord('A'))
            else:
                shifted_char = char
            ciphertext += shifted_char
        return ciphertext

    def rail_fence_cipher(self, plain_text, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plain_text: The plaintext to encrypt, str.
        :param rails: The number of rails to use, int. Must be at least 2.
        :return: The ciphertext, str.
        :raises ValueError: if rails is less than 2.
        """
        if rails < 2:
            raise ValueError("Number of rails must be at least 2.")

        fence = [["" for _ in range(len(plain_text))] for _ in range(rails)]
        rail = 0
        down = True

        for col in range(len(plain_text)):
            fence[rail][col] = plain_text[col]

            if rail == rails - 1:
                down = False
            elif rail == 0:
                down = True

            rail += 1 if down else -1

        ciphertext = ""
        for row in fence:
            ciphertext += "".join(row)

        ciphertext = ciphertext.replace("","")
        return ciphertext