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
            key_char = key[i % key_length]
            shift = ord(key_char.lower()) - ord('a')
            if 'a' <= char <= 'z':
                shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            elif 'A' <= char <= 'Z':
                shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            else:
                shifted_char = char
            ciphertext += shifted_char
        return ciphertext

    def rail_fence_cipher(self, plain_text, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param rails: Number of rails to use for the fence
        :return: The ciphertext, str.
        """
        if rails <= 1:
            return plain_text

        fence = [["" for _ in range(len(plain_text))] for _ in range(rails)]
        rail = 0
        down = True

        for col in range(len(plain_text)):
            fence[rail][col] = plain_text[col]

            if rail == rails - 1:
                down = False
            elif rail == 0:
                down = True

            if down:
                rail += 1
            else:
                rail -= 1

        cipher_text = ""
        for row in fence:
            cipher_text += "".join(row)

        return cipher_text.replace("","")