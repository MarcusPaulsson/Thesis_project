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
                shift_amount = shift % 26
                base = ord('A') if char.isupper() else ord('a')
                new_char = chr((ord(char) - base + shift_amount) % 26 + base)
                result.append(new_char)
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
                shift_amount = ord(self.key[key_index % key_length].lower()) - ord('a')
                base = ord('A') if char.isupper() else ord('a')
                new_char = chr((ord(char) - base + shift_amount) % 26 + base)
                result.append(new_char)
                key_index += 1
            else:
                result.append(char)

        return ''.join(result)

    def rail_fence_cipher(self, plain_text, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        """
        if rails == 1:
            return plain_text

        rail = [['\n' for _ in range(len(plain_text))]
                for _ in range(rails)]
        dir_down = None
        row, col = 0, 0

        for char in plain_text:
            if row == 0:
                dir_down = True
            if row == rails - 1:
                dir_down = False

            rail[row][col] = char
            col += 1

            if dir_down:
                row += 1
            else:
                row -= 1

        result = []
        for r in range(rails):
            for c in range(len(plain_text)):
                if rail[r][c] != '\n':
                    result.append(rail[r][c])

        return ''.join(result)