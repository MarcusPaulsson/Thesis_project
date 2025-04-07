class DecryptionUtils:
    """
    This is a class that provides methods for decryption, including the Caesar cipher, Vigenere cipher, and Rail Fence cipher.
    """

    def __init__(self, key="default_key"):
        """
        Initializes the decryption utility with a key.
        :param key: The key to use for decryption, str. Defaults to "default_key" if None is provided.
        """
        self.key = key

    def caesar_decipher(self, ciphertext, shift):
        """
        Deciphers the given ciphertext using the Caesar cipher.

        Handles non-alphabetic characters and maintains case.

        :param ciphertext: The ciphertext to decipher, str.
        :param shift: The shift to use for decryption, int.
        :return: The deciphered plaintext, str.
        """
        if not isinstance(ciphertext, str):
            raise TypeError("Ciphertext must be a string.")
        if not isinstance(shift, int):
            raise TypeError("Shift must be an integer.")

        plaintext = ""
        for char in ciphertext:
            if 'a' <= char <= 'z':
                plaintext += chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            elif 'A' <= char <= 'Z':
                plaintext += chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            else:
                plaintext += char
        return plaintext

    def vigenere_decipher(self, ciphertext):
        """
        Deciphers the given ciphertext using the Vigenere cipher.

        Handles non-alphabetic characters and maintains case.  Key is repeated as needed.

        :param ciphertext: The ciphertext to decipher, str.
        :return: The deciphered plaintext, str.
        """
        if not isinstance(ciphertext, str):
            raise TypeError("Ciphertext must be a string.")
        if not isinstance(self.key, str):
            raise TypeError("Key must be a string.")

        plaintext = ""
        key = self.key.lower()  # Ensure key is lowercase for consistency
        key_length = len(key)
        key_index = 0

        for char in ciphertext:
            if 'a' <= char <= 'z':
                shift = ord(key[key_index % key_length]) - ord('a')
                plaintext += chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
                key_index += 1
            elif 'A' <= char <= 'Z':
                shift = ord(key[key_index % key_length]) - ord('a')
                plaintext += chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
                key_index += 1
            else:
                plaintext += char
        return plaintext

    def rail_fence_decipher(self, encrypted_text, rails):
        """
        Deciphers the given ciphertext using the Rail Fence cipher.

        Handles invalid rail values.

        :param encrypted_text: The ciphertext to decipher, str.
        :param rails: The number of rails to use for decryption, int.
        :return: The deciphered plaintext, str.
        """
        if not isinstance(encrypted_text, str):
            raise TypeError("Encrypted text must be a string.")
        if not isinstance(rails, int):
            raise TypeError("Rails must be an integer.")
        if rails <= 0:
            raise ValueError("Rails must be a positive integer.")
        if rails >= len(encrypted_text):
            return encrypted_text # If rails >= length, the ciphertext is the plaintext

        rail = [['' for _ in range(len(encrypted_text))] for _ in range(rails)]

        # Mark the positions where characters will be placed
        row = 0
        direction = 1  # 1 for down, -1 for up
        for col in range(len(encrypted_text)):
            rail[row][col] = '*'
            row += direction

            if row == rails - 1:
                direction = -1
            elif row == 0:
                direction = 1

        # Fill the rail matrix with the encrypted text
        index = 0
        for i in range(rails):
            for j in range(len(encrypted_text)):
                if rail[i][j] == '*':
                    rail[i][j] = encrypted_text[index]
                    index += 1

        # Read the rail matrix in a zig-zag manner to get the plaintext
        plaintext = ""
        row = 0
        direction = 1
        for col in range(len(encrypted_text)):
            plaintext += rail[row][col]
            row += direction

            if row == rails - 1:
                direction = -1
            elif row == 0:
                direction = 1

        return plaintext