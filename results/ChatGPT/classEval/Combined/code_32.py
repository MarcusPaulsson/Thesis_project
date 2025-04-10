class DecryptionUtils:
    """
    This class provides methods for decryption, including the Caesar cipher,
    Vigenere cipher, and Rail Fence cipher.
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
        """
        shift %= 26  # Normalize shift
        deciphered = []

        for char in ciphertext:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                new_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                deciphered.append(new_char)
            else:
                deciphered.append(char)

        return ''.join(deciphered)

    def vigenere_decipher(self, ciphertext):
        """
        Deciphers the given ciphertext using the Vigenere cipher.
        :param ciphertext: The ciphertext to decipher, str.
        :return: The deciphered plaintext, str.
        """
        key_length = len(self.key)
        deciphered = []
        key_index = 0

        for char in ciphertext:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                key_char = self.key[key_index % key_length]
                shift = ord(key_char) - ord('a')
                new_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                deciphered.append(new_char)
                key_index += 1
            else:
                deciphered.append(char)

        return ''.join(deciphered)

    def rail_fence_decipher(self, encrypted_text, rails):
        """
        Deciphers the given ciphertext using the Rail Fence cipher.
        :param encrypted_text: The ciphertext to decipher, str.
        :param rails: The number of rails to use for decryption, int.
        :return: The deciphered plaintext, str.
        """
        length = len(encrypted_text)
        rail = [['' for _ in range(length)] for _ in range(rails)]
        row, col = 0, 0
        dir_down = True

        for char in encrypted_text:
            if row == 0:
                dir_down = True
            if row == rails - 1:
                dir_down = False

            rail[row][col] = '*'
            col += 1

            row += 1 if dir_down else -1

        index = 0
        for i in range(rails):
            for j in range(length):
                if rail[i][j] == '*' and index < len(encrypted_text):
                    rail[i][j] = encrypted_text[index]
                    index += 1

        result = []
        row, col = 0, 0

        for _ in range(length):
            if row == 0:
                dir_down = True
            if row == rails - 1:
                dir_down = False

            if rail[row][col] != '*':
                result.append(rail[row][col])
                col += 1

            row += 1 if dir_down else -1

        return ''.join(result)