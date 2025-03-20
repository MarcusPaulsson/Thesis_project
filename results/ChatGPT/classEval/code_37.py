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
        result = ""
        for char in plaintext:
            if char.isalpha():
                shift_base = ord('a') if char.islower() else ord('A')
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            else:
                result += char
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
        ciphertext = []
        key_length = len(self.key)
        for i, char in enumerate(plaintext):
            if char.isalpha():
                shift_base = ord('a') if char.islower() else ord('A')
                key_char = self.key[i % key_length].lower()
                shift = ord(key_char) - ord('a')
                ciphertext.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
            else:
                ciphertext.append(char)
        return ''.join(ciphertext)

    def rail_fence_cipher(self, plaintext, rails):
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
            return plaintext

        rail = [['\n' for _ in range(len(plaintext))]
                for _ in range(rails)]
        
        dir_down = None
        row, col = 0, 0

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

        result = []
        for r in rail:
            for c in r:
                if c != '\n':
                    result.append(c)
        return ''.join(result)