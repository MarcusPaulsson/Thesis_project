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
        plaintext = ""
        for char in ciphertext:
            if 'a' <= char <= 'z':
                start = 'a'
                decrypted_char = chr((ord(char) - ord(start) - shift) % 26 + ord(start))
            elif 'A' <= char <= 'Z':
                start = 'A'
                decrypted_char = chr((ord(char) - ord(start) - shift) % 26 + ord(start))
            else:
                decrypted_char = char
            plaintext += decrypted_char
        return plaintext

    def vigenere_decipher(self, ciphertext):
        """
        Deciphers the given ciphertext using the Vigenere cipher
        :param ciphertext: The ciphertext to decipher,str.
        :return: The deciphered plaintext,str.
        """
        plaintext = ""
        key_length = len(self.key)
        for i, char in enumerate(ciphertext):
            if 'a' <= char <= 'z':
                start = 'a'
                key_char = self.key[i % key_length]
                key_shift = ord(key_char) - ord('a')
                decrypted_char = chr((ord(char) - ord(start) - key_shift) % 26 + ord(start))
            elif 'A' <= char <= 'Z':
                start = 'A'
                key_char = self.key[i % key_length]
                key_shift = ord(key_char.lower()) - ord('a')
                decrypted_char = chr((ord(char) - ord(start) - key_shift) % 26 + ord(start))
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
        text_length = len(encrypted_text)
        rail_matrix = [['' for _ in range(text_length)] for _ in range(rails)]
        direction_down = False
        row, col = 0, 0

        for i in range(text_length):
            if row == 0 or row == rails - 1:
                direction_down = not direction_down

            rail_matrix[row][col] = '*'
            col += 1

            if direction_down:
                row += 1
            else:
                row -= 1

        index = 0
        for i in range(rails):
            for j in range(text_length):
                if rail_matrix[i][j] == '*':
                    rail_matrix[i][j] = encrypted_text[index]
                    index += 1

        result = ""
        row, col = 0, 0
        direction_down = False

        for i in range(text_length):
            if row == 0 or row == rails - 1:
                direction_down = not direction_down

            result += rail_matrix[row][col]
            col += 1

            if direction_down:
                row += 1
            else:
                row -= 1

        return result