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
        plaintext = ''
        for char in ciphertext:
            if 'a' <= char <= 'z':
                start = 'a'
            elif 'A' <= char <= 'Z':
                start = 'A'
            else:
                plaintext += char
                continue

            shifted_char = chr((ord(char) - ord(start) - shift) % 26 + ord(start))
            plaintext += shifted_char
        return plaintext

    def vigenere_decipher(self, ciphertext):
        """
        Deciphers the given ciphertext using the Vigenere cipher
        :param ciphertext: The ciphertext to decipher,str.
        :return: The deciphered plaintext,str.
        """
        plaintext = ''
        key_len = len(self.key)
        for i, char in enumerate(ciphertext):
            if 'a' <= char <= 'z':
                start = 'a'
            elif 'A' <= char <= 'Z':
                start = 'A'
            else:
                plaintext += char
                continue

            key_char = self.key[i % key_len]
            key_shift = ord(key_char) - ord('a') if 'a' <= key_char <= 'z' else ord(key_char) - ord('A')
            decrypted_char = chr((ord(char) - ord(start) - key_shift) % 26 + ord(start))
            plaintext += decrypted_char
        return plaintext

    def rail_fence_decipher(self, encrypted_text, rails):
        """
        Deciphers the given ciphertext using the Rail Fence cipher
        :param encrypted_text: The ciphertext to decipher,str.
        :param rails: The number of rails to use for decryption,int.
        :return: The deciphered plaintext,str.
        """
        text_len = len(encrypted_text)
        rail_matrix = [['' for _ in range(text_len)] for _ in range(rails)]
        row, direction = 0, 1

        for col in range(text_len):
            rail_matrix[row][col] = '*'
            if row == 0:
                direction = 1
            elif row == rails - 1:
                direction = -1
            row += direction

        index = 0
        for i in range(rails):
            for j in range(text_len):
                if rail_matrix[i][j] == '*':
                    rail_matrix[i][j] = encrypted_text[index]
                    index += 1

        row, direction = 0, 1
        plaintext = ''
        for col in range(text_len):
            plaintext += rail_matrix[row][col]
            if row == 0:
                direction = 1
            elif row == rails - 1:
                direction = -1
            row += direction

        return plaintext