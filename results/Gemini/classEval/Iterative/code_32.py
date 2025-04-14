class DecryptionUtils:
    """
    This is a class that provides methods for decryption, including the Caesar cipher, Vigenere cipher, and Rail Fence cipher.
    """

    def __init__(self, key):
        """
        Initializes the decryption utility with a key.
        :param key: The key to use for decryption,str.
        """
        self.key = key

    def caesar_decipher(self, ciphertext, shift):
        """
        Deciphers the given ciphertext using the Caesar cipher
        :param ciphertext: The ciphertext to decipher,str.
        :param shift: The shift to use for decryption,int.
        :return: The deciphered plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.caesar_decipher('ifmmp', 1)
        'hello'

        """
        plaintext = ''
        for char in ciphertext:
            if 'a' <= char <= 'z':
                start = ord('a')
                shifted_char = chr((ord(char) - start - (shift % 26)) % 26 + start)
            elif 'A' <= char <= 'Z':
                start = ord('A')
                shifted_char = chr((ord(char) - start - (shift % 26)) % 26 + start)
            else:
                shifted_char = char
            plaintext += shifted_char
        return plaintext

    def vigenere_decipher(self, ciphertext):
        """
        Deciphers the given ciphertext using the Vigenere cipher
        :param ciphertext: The ciphertext to decipher,str.
        :return: The deciphered plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.vigenere_decipher('ifmmp')
        'ybocl'

        """
        plaintext = ''
        key = self.key
        key_length = len(key)
        key_index = 0

        for char in ciphertext:
            if 'a' <= char <= 'z':
                key_char = key[key_index % key_length]
                shift = ord(key_char) - ord('a')
                start = ord('a')
                shifted_char = chr((ord(char) - start - shift) % 26 + start)
                key_index += 1
            elif 'A' <= char <= 'Z':
                key_char = key[key_index % key_length]
                shift = ord(key_char.lower()) - ord('a')
                start = ord('A')
                shifted_char = chr((ord(char) - start - shift) % 26 + start)
                key_index += 1
            else:
                shifted_char = char
            plaintext += shifted_char
        return plaintext

    def rail_fence_decipher(self, encrypted_text, rails):
        """
        Deciphers the given ciphertext using the Rail Fence cipher
        :param encrypted_text: The ciphertext to decipher,str.
        :param rails: The number of rails to use for decryption,int.
        :return: The deciphered plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.rail_fence_decipher('Hoo!el,Wrdl l', 3)
        'Hello, World!'

        """
        length = len(encrypted_text)
        rail = [['' for _ in range(length)] for _ in range(rails)]

        # Fill the rail matrix to mark the places with '*'
        row, col = 0, 0
        direction = 1  # 1 for down, -1 for up

        for i in range(length):
            rail[row][col] = '*'
            col += 1

            row += direction

            if row == rails:
                row = rails - 2
                direction = -1
            elif row == -1:
                row = 1
                direction = 1

        # Fill the rail matrix with the encrypted text
        index = 0
        for i in range(rails):
            for j in range(length):
                if rail[i][j] == '*' and index < length:
                    rail[i][j] = encrypted_text[index]
                    index += 1

        # Read the rail matrix in zigzag manner to get the original text
        result = ""
        row, col = 0, 0
        direction = 1

        for i in range(length):
            result += rail[row][col]
            col += 1

            row += direction

            if row == rails:
                row = rails - 2
                direction = -1
            elif row == -1:
                row = 1
                direction = 1

        return result