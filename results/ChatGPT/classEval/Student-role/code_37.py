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
        return ''.join(chr((ord(char) - 97 + shift) % 26 + 97) if char.islower() else char for char in plaintext)

    def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'
        """
        ciphertext = []
        key_length = len(self.key)
        for i, char in enumerate(plaintext):
            if char.islower():
                shift = ord(self.key[i % key_length]) - 97
                ciphertext.append(chr((ord(char) - 97 + shift) % 26 + 97))
            else:
                ciphertext.append(char)
        return ''.join(ciphertext)

    def rail_fence_cipher(self, plain_text, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param rails: The number of rails to use for the cipher, int.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.rail_fence_cipher("abc", 2)
        'acb'
        """
        rail = [['\n' for _ in range(len(plain_text))] for _ in range(rails)]
        dir_down = False
        row, col = 0, 0

        for char in plain_text:
            if row == 0 or row == rails - 1:
                dir_down = not dir_down

            rail[row][col] = char
            col += 1

            if dir_down:
                row += 1
            else:
                row -= 1

        ciphertext = ''.join(rail[r][c] for r in range(rails) for c in range(len(plain_text)) if rail[r][c] != '\n')
        return ciphertext