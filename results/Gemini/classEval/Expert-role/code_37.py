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
        key_len = len(self.key)
        for i, char in enumerate(plaintext):
            key_char = self.key[i % key_len]
            shift = ord(key_char) - ord('a')
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
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.rail_fence_cipher("abc", 2)
        'acb'

        """
        if rails <= 1:
            return plain_text
        fence = [[] for _ in range(rails)]
        rail = 0
        direction = 1  # 1 for down, -1 for up

        for char in plain_text:
            fence[rail].append(char)
            rail += direction

            if rail == rails:
                rail = rails - 2
                direction = -1
            elif rail == -1:
                rail = 1
                direction = 1

        ciphertext = "".join("".join(rail) for rail in fence)
        return ciphertext