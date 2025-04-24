class DecryptionUtils:
    """
    A class that provides methods for decryption, including the Caesar cipher, Vigenere cipher, and Rail Fence cipher.
    """

    def __init__(self, key: str):
        """
        Initializes the decryption utility with a key.
        :param key: The key to use for decryption.
        """
        self.key = key.lower()  # Normalize key to lowercase for consistency

    def caesar_decipher(self, ciphertext: str, shift: int) -> str:
        """
        Deciphers the given ciphertext using the Caesar cipher.
        :param ciphertext: The ciphertext to decipher.
        :param shift: The shift to use for decryption.
        :return: The deciphered plaintext.
        """
        shift %= 26  # Normalize shift to be within 0-25
        plaintext = []

        for char in ciphertext:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                deciphered_char = chr((ord(char) - base - shift) % 26 + base)
                plaintext.append(deciphered_char)
            else:
                plaintext.append(char)

        return ''.join(plaintext)

    def vigenere_decipher(self, ciphertext: str) -> str:
        """
        Deciphers the given ciphertext using the Vigenere cipher.
        :param ciphertext: The ciphertext to decipher.
        :return: The deciphered plaintext.
        """
        plaintext = []
        key_length = len(self.key)
        key_as_int = [ord(i) - ord('a') for i in self.key]
        ciphertext_int = [ord(i) - ord('a') for i in ciphertext.lower() if i.isalpha()]

        for i in range(len(ciphertext_int)):
            value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
            plaintext.append(chr(value + ord('a')))

        return ''.join(plaintext)

    def rail_fence_decipher(self, encrypted_text: str, rails: int) -> str:
        """
        Deciphers the given ciphertext using the Rail Fence cipher.
        :param encrypted_text: The ciphertext to decipher.
        :param rails: The number of rails to use for decryption.
        :return: The deciphered plaintext.
        """
        if rails <= 0:
            raise ValueError("Number of rails must be greater than zero.")

        rail = [['\n' for _ in range(len(encrypted_text))] for _ in range(rails)]
        dir_down = True
        row, col = 0, 0

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
            for j in range(len(encrypted_text)):
                if rail[i][j] == '*' and index < len(encrypted_text):
                    rail[i][j] = encrypted_text[index]
                    index += 1

        result = []
        row, col = 0, 0

        for _ in range(len(encrypted_text)):
            if row == 0:
                dir_down = True
            if row == rails - 1:
                dir_down = False

            if rail[row][col] != '*':
                result.append(rail[row][col])
                col += 1

            row += 1 if dir_down else -1

        return ''.join(result)