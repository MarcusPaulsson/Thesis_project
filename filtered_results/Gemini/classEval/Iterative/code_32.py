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
        plaintext = ''
        key_len = len(key)
        key = key.lower()  # Ensure key is lowercase for consistent shifting
        for i, char in enumerate(ciphertext):
            if 'a' <= char <= 'z':
                key_char = key[i % key_len]
                key_shift = ord(key_char) - ord('a')
                start = ord('a')
                decrypted_char = chr((ord(char) - start - key_shift) % 26 + start)
            elif 'A' <= char <= 'Z':
                key_char = key[i % key_len]
                key_shift = ord(key_char) - ord('a')
                start = ord('A')
                decrypted_char = chr((ord(char) - start - key_shift) % 26 + start)

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
        """
        n = len(encrypted_text)
        rail = [['' for _ in range(n)] for _ in range(rails)]

        # Mark the positions of the rail fence
        row, col = 0, 0
        direction = 1  # 1 for down, -1 for up

        for i in range(n):
            rail[row][col] = '*'
            col += 1

            row += direction
            if row == rails:
                row = rails - 2
                direction = -1
            elif row == -1:
                row = 1
                direction = 1

        # Fill the rail fence with the encrypted text
        index = 0
        for i in range(rails):
            for j in range(n):
                if rail[i][j] == '*' and index < n:
                    rail[i][j] = encrypted_text[index]
                    index += 1

        # Read the rail fence in the same pattern to get the plaintext
        result = ""
        row, col = 0, 0
        direction = 1

        for i in range(n):
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