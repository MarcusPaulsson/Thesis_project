class DecryptionUtils:
    """
    This class provides methods for decryption, including the Caesar cipher, Vigenere cipher, and Rail Fence cipher.
    """

    def __init__(self, key):
        """
        Initializes the decryption utility with a key.
        :param key: The key to use for decryption, str.
        """
        self.key = key.lower()  # Normalize the key to lowercase for consistency

    def caesar_decipher(self, ciphertext, shift):
        """
        Deciphers the given ciphertext using the Caesar cipher.
        :param ciphertext: The ciphertext to decipher, str.
        :param shift: The shift to use for decryption, int.
        :return: The deciphered plaintext, str.
        >>> d = DecryptionUtils('key')
        >>> d.caesar_decipher('ifmmp', 1)
        'hello'
        """
        plaintext = []
        for char in ciphertext:
            if char.isalpha():
                base = ord('a') if char.islower() else ord('A')
                new_char = chr((ord(char) - base - shift) % 26 + base)
                plaintext.append(new_char)
            else:
                plaintext.append(char)
        return ''.join(plaintext)

    def vigenere_decipher(self, ciphertext):
        """
        Deciphers the given ciphertext using the Vigenere cipher.
        :param ciphertext: The ciphertext to decipher, str.
        :return: The deciphered plaintext, str.
        >>> d = DecryptionUtils('key')
        >>> d.vigenere_decipher('ifmmp')
        'hello'
        """
        plaintext = []
        key_length = len(self.key)
        key_index = 0

        for char in ciphertext:
            if char.isalpha():
                shift = (ord(self.key[key_index]) - ord('a')) % 26
                base = ord('a') if char.islower() else ord('A')
                new_char = chr((ord(char) - base - shift) % 26 + base)
                plaintext.append(new_char)
                key_index = (key_index + 1) % key_length  # Only increment for letters
            else:
                plaintext.append(char)
        return ''.join(plaintext)

    def rail_fence_decipher(self, encrypted_text, rails):
        """
        Deciphers the given ciphertext using the Rail Fence cipher.
        :param encrypted_text: The ciphertext to decipher, str.
        :param rails: The number of rails to use for decryption, int.
        :return: The deciphered plaintext, str.
        >>> d = DecryptionUtils('key')
        >>> d.rail_fence_decipher('Hoo!el,Wrdl l', 3)
        'Hello, World!'
        """
        if rails <= 0:
            raise ValueError("Number of rails must be greater than 0")

        length = len(encrypted_text)
        rail = [['' for _ in range(length)] for _ in range(rails)]
        dir_down = False
        row, col = 0, 0

        for i in range(length):
            if row == 0 or row == rails - 1:
                dir_down = not dir_down
            rail[row][col] = encrypted_text[i]
            col += 1
            row += 1 if dir_down else -1

        result = []
        for i in range(rails):
            for j in range(length):
                if rail[i][j] != '':
                    result.append(rail[i][j])

        return ''.join(result)