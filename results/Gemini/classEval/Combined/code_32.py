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
        """
        result = ''
        for char in ciphertext:
            if 'a' <= char <= 'z':
                start = ord('a')
                shifted_char = chr((ord(char) - start - shift) % 26 + start)
            elif 'A' <= char <= 'Z':
                start = ord('A')
                shifted_char = chr((ord(char) - start - shift) % 26 + start)
            else:
                shifted_char = char
            result += shifted_char
        return result

    def vigenere_decipher(self, ciphertext):
        """
        Deciphers the given ciphertext using the Vigenere cipher
        :param ciphertext: The ciphertext to decipher,str.
        :return: The deciphered plaintext,str.
        """
        key = self.key
        result = ''
        key_length = len(key)
        for i, char in enumerate(ciphertext):
            if 'a' <= char <= 'z':
                start = ord('a')
                key_char = key[i % key_length]
                key_shift = ord(key_char) - ord('a')
                shifted_char = chr((ord(char) - start - key_shift) % 26 + start)
            elif 'A' <= char <= 'Z':
                start = ord('A')
                key_char = key[i % key_length]
                key_shift = ord(key_char.lower()) - ord('a')
                shifted_char = chr((ord(char) - start - key_shift) % 26 + start)
            else:
                shifted_char = char
            result += shifted_char
        return result

    def rail_fence_decipher(self, encrypted_text, rails):
        """
        Deciphers the given ciphertext using the Rail Fence cipher
        :param encrypted_text: The ciphertext to decipher,str.
        :param rails: The number of rails to use for decryption,int.
        :return: The deciphered plaintext,str.
        """
        text_length = len(encrypted_text)
        rail = [['' for _ in range(text_length)] for _ in range(rails)]

        # Mark the positions where characters will be placed
        row, col = 0, 0
        direction = 1  # 1 for down, -1 for up

        for i in range(text_length):
            rail[row][col] = '*'
            col += 1

            row += direction
            if row == rails:
                row = rails - 2
                direction = -1
            elif row == -1:
                row = 1
                direction = 1

        # Fill the marked positions with the encrypted text
        index = 0
        for i in range(rails):
            for j in range(text_length):
                if rail[i][j] == '*' and index < text_length:
                    rail[i][j] = encrypted_text[index]
                    index += 1

        # Read the text in a zig-zag manner to decrypt
        result = ""
        row, col = 0, 0
        direction = 1

        for i in range(text_length):
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