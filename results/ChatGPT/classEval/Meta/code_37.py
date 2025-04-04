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
                ciphertext += chr((ord(char) - shift_base + shift) % 26 + shift_base)
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
                shift = ord(self.key[i % key_length].lower()) - ord('a')
                shift_base = ord('a') if char.islower() else ord('A')
                ciphertext += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            else:
                ciphertext += char
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
        rail = [['\n' for i in range(len(plain_text))]
                for j in range(rails)]
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

        ciphertext = ""
        for i in range(rails):
            for j in range(len(plain_text)):
                if rail[i][j] != '\n':
                    ciphertext += rail[i][j]
        
        return ciphertext