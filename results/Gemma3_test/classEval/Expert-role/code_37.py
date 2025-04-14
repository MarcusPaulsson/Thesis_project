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
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'

        """
        key_len = len(self.key)
        key_as_int = [ord(i) for i in self.key]
        plaintext_as_int = [ord(i) for i in plaintext]
        ciphertext = ''
        for i in range(len(plaintext_as_int)):
            value = (plaintext_as_int[i] + key_as_int[i % key_len]) % 26
            ciphertext += chr(value + ord('a'))
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
        fence = [['' for _ in range(len(plain_text))] for _ in range(rails)]
        rail = 0
        direction = 1

        for i, char in enumerate(plain_text):
            fence[rail][i] = char

            rail += direction

            if rail == rails - 1 or rail == 0:
                direction *= -1

        ciphertext = ''.join([''.join(row) for row in fence])
        return ciphertext