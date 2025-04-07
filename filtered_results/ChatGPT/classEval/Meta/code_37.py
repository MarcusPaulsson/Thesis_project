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
        result = []
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
                shift = ord(self.key[key_index % key_length].lower()) - ord('a')
                shift_base = ord('A') if char.isupper() else ord('a')
                result.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
                key_index += 1
            else:
                result.append(char)

        return ''.join(result)

    def rail_fence_cipher(self, plaintext, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param rails: The number of rails, int.
        :return: The ciphertext, str.
        """
        rail = [['' for _ in range(len(plaintext))] for _ in range(rails)]
        row, direction = 0, 1

        for char in plaintext:
            rail[row].append(char)
            if row == 0:
                direction = 1
            elif row == rails - 1:
                direction = -1
            row += direction

        ciphertext = ''.join(''.join(r) for r in rail)
        return ciphertext.replace('', '')