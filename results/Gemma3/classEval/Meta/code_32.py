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
                shifted_char = chr((ord(char) - start - shift) % 26 + start)
            elif 'A' <= char <= 'Z':
                start = ord('A')
                shifted_char = chr((ord(char) - start - shift) % 26 + start)
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
        key_len = len(self.key)
        for i, char in enumerate(ciphertext):
            if 'a' <= char <= 'z':
                key_char = self.key[i % key_len]
                key_shift = ord(key_char) - ord('a')
                decrypted_char = chr((ord(char) - ord('a') - key_shift) % 26 + ord('a'))
            elif 'A' <= char <= 'Z':
                key_char = self.key[i % key_len]
                key_shift = ord(key_char) - ord('a')
                decrypted_char = chr((ord(char) - ord('A') - key_shift) % 26 + ord('A'))
            else:
                decrypted_char = char
            plaintext += decrypted_char
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
        n = len(encrypted_text)
        fence = [['' for _ in range(n)] for _ in range(rails)]
        row, direction = 0, 1

        for col in range(n):
            fence[row][col] = '*'
            if row == 0:
                direction = 1
            elif row == rails - 1:
                direction = -1
            row += direction

        index = 0
        for i in range(rails):
            for j in range(n):
                if fence[i][j] == '*' and index < n:
                    fence[i][j] = encrypted_text[index]
                    index += 1

        result = ''
        row, direction = 0, 1
        for col in range(n):
            result += fence[row][col]
            if row == 0:
                direction = 1
            elif row == rails - 1:
                direction = -1
            row += direction

        return result