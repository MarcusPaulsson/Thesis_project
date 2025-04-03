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
                shift_base = ord('a') if char.islower() else ord('A')
                new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
                ciphertext += new_char
            else:
                ciphertext += char
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
        key_length = len(self.key)
        for i, char in enumerate(plaintext):
            if char.isalpha():
                shift_base = ord('a') if char.islower() else ord('A')
                key_char = self.key[i % key_length].lower()
                shift = ord(key_char) - ord('a')
                new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
                ciphertext += new_char
            else:
                ciphertext += char
        return ciphertext

    def rail_fence_cipher(self, plain_text, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param rails: The number of rails, int.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.rail_fence_cipher("abc", 2)
        'acb'
        """
        if rails <= 1:
            return plain_text

        rail = [['\n' for _ in range(len(plain_text))]
                for _ in range(rails)]

        row, col, direction = 0, 0, 1

        for char in plain_text:
            rail[row][col] = char
            col += 1

            if row == 0:
                direction = 1
            elif row == rails - 1:
                direction = -1

            row += direction

        ciphertext = ""
        for r in rail:
            for c in r:
                if c != '\n':
                    ciphertext += c

        return ciphertext