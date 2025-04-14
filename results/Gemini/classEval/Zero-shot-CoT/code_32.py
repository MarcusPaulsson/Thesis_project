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
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            elif 'A' <= char <= 'Z':
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            else:
                decrypted_char = char
            plaintext += decrypted_char
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
        for i, char in enumerate(ciphertext):
            if 'a' <= char <= 'z':
                key_char = key[i % key_length]
                shift = ord(key_char) - ord('a')
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            elif 'A' <= char <= 'Z':
                key_char = key[i % key_length]
                shift = ord(key_char.lower()) - ord('a')
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
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
        length = len(encrypted_text)
        rail = [['\n' for i in range(length)] for j in range(rails)]

        dir_down = None
        row, col = 0, 0

        for i in range(length):
            if row == 0:
                dir_down = True
            if row == rails - 1:
                dir_down = False

            rail[row][col] = '*'
            col += 1

            if dir_down:
                row += 1
            else:
                row -= 1

        index = 0
        for i in range(rails):
            for j in range(length):
                if rail[i][j] == '*' and index < length:
                    rail[i][j] = encrypted_text[index]
                    index += 1

        result = ""
        row, col = 0, 0
        dir_down = None

        for i in range(length):
            if row == 0:
                dir_down = True
            if row == rails - 1:
                dir_down = False

            result += rail[row][col]
            col += 1

            if dir_down:
                row += 1
            else:
                row -= 1
        return result