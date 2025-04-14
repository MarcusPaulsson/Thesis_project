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
        key = self.key
        key_length = len(key)
        for i, char in enumerate(ciphertext):
            if 'a' <= char <= 'z':
                key_char = key[i % key_length]
                shift = ord(key_char) - ord('a')
                start = ord('a')
                shifted_char = chr((ord(char) - start - shift) % 26 + start)
            elif 'A' <= char <= 'Z':
                key_char = key[i % key_length]
                shift = ord(key_char.lower()) - ord('a')
                start = ord('A')
                shifted_char = chr((ord(char) - start - shift) % 26 + start)
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
        text_length = len(encrypted_text)
        rail_matrix = [['' for _ in range(text_length)] for _ in range(rails)]
        rail = 0
        direction = 1  # 1 for down, -1 for up

        # Mark the positions in the rail matrix
        for col in range(text_length):
            rail_matrix[rail][col] = '*'
            rail += direction
            if rail == rails - 1 or rail == 0:
                direction *= -1

        # Fill the rail matrix with the encrypted text
        index = 0
        for i in range(rails):
            for j in range(text_length):
                if rail_matrix[i][j] == '*':
                    rail_matrix[i][j] = encrypted_text[index]
                    index += 1

        # Read the rail matrix in a zig-zag manner to get the plaintext
        plaintext = ''
        rail = 0
        direction = 1
        for col in range(text_length):
            plaintext += rail_matrix[rail][col]
            rail += direction
            if rail == rails - 1 or rail == 0:
                direction *= -1

        return plaintext