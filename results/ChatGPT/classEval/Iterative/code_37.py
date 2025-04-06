class EncryptionUtils:
    """
    This is a class that provides methods for encryption, including the Caesar cipher, Vigenere cipher, and Rail Fence cipher.
    """

    def __init__(self, key):
        """
        Initializes the class with a key.
        :param key: The key to use for encryption, str.
        """
        if not isinstance(key, str) or not key.isalpha():
            raise ValueError("Key must be a string containing only alphabetic characters.")
        self.key = key

    def caesar_cipher(self, plaintext, shift):
        """
        Encrypts the plaintext using the Caesar cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param shift: The number of characters to shift each character in the plaintext, int.
        :return: The ciphertext, str.
        """
        if not isinstance(shift, int):
            raise ValueError("Shift must be an integer.")
        
        ciphertext = ''
        for char in plaintext:
            if char.isalpha():
                shift_base = ord('a') if char.islower() else ord('A')
                shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
                ciphertext += shifted_char
            else:
                ciphertext += char
        return ciphertext

    def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        """
        ciphertext = ''
        key_length = len(self.key)
        key_index = 0

        for char in plaintext:
            if char.isalpha():
                shift_base = ord('a') if char.islower() else ord('A')
                key_char = self.key[key_index % key_length].lower()
                key_shift = ord(key_char) - ord('a')
                shifted_char = chr((ord(char) - shift_base + key_shift) % 26 + shift_base)
                ciphertext += shifted_char
                
                key_index += 1  # Only increment key_index for alphabetic characters
            else:
                ciphertext += char
        return ciphertext

    def rail_fence_cipher(self, plaintext, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param rails: The number of rails for the Rail Fence cipher, int.
        :return: The ciphertext, str.
        """
        if not isinstance(rails, int) or rails <= 0:
            raise ValueError("Rails must be a positive integer.")

        rail = [['\n' for _ in range(len(plaintext))] for _ in range(rails)]
        row, col = 0, 0
        dir_down = True

        for char in plaintext:
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

        ciphertext = ''.join([''.join(r) for r in rail]).replace('\n', '')
        return ciphertext