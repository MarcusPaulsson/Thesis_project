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
        ciphertext = []
        for char in plaintext:
            if char.isalpha():
                shift_base = ord('A') if char.isupper() else ord('a')
                new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
                ciphertext.append(new_char)
            else:
                ciphertext.append(char)
        return ''.join(ciphertext)

    def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        """
        ciphertext = []
        key_length = len(self.key)
        key_index = 0
        
        for char in plaintext:
            if char.isalpha():
                shift_base = ord('A') if char.isupper() else ord('a')
                key_char = self.key[key_index % key_length].lower()
                shift = ord(key_char) - ord('a')
                new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
                ciphertext.append(new_char)
                key_index += 1
            else:
                ciphertext.append(char)
        return ''.join(ciphertext)

    def rail_fence_cipher(self, plain_text, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plain_text: The plaintext to encrypt, str.
        :param rails: The number of rails, int.
        :return: The ciphertext, str.
        """
        if rails <= 1 or rails >= len(plain_text):
            return plain_text
        
        fence = [''] * rails
        direction_down = False
        row = 0

        for char in plain_text:
            fence[row] += char
            if row == 0 or row == rails - 1:
                direction_down = not direction_down
            row += 1 if direction_down else -1
        
        return ''.join(fence)