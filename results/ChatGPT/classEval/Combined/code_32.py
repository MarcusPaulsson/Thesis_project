class DecryptionUtils:
    """
    A class that provides methods for decryption, including the Caesar cipher,
    Vigenere cipher, and Rail Fence cipher.
    """

    def __init__(self, key):
        """
        Initializes the decryption utility with a key.
        :param key: The key to use for decryption, str.
        """
        self.key = key.lower()

    def caesar_decipher(self, ciphertext, shift):
        """
        Deciphers the given ciphertext using the Caesar cipher.
        :param ciphertext: The ciphertext to decipher, str.
        :param shift: The shift to use for decryption, int.
        :return: The deciphered plaintext, str.
        """
        shift = shift % 26  # Normalize shift
        plaintext = []
        
        for char in ciphertext:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                decrypted_char = chr((ord(char) - base - shift) % 26 + base)
                plaintext.append(decrypted_char)
            else:
                plaintext.append(char)  # Non-alphabet characters remain unchanged
        
        return ''.join(plaintext)

    def vigenere_decipher(self, ciphertext):
        """
        Deciphers the given ciphertext using the Vigenere cipher.
        :param ciphertext: The ciphertext to decipher, str.
        :return: The deciphered plaintext, str.
        """
        plaintext = []
        key_length = len(self.key)
        key_as_int = [ord(i) - ord('a') for i in self.key if i.isalpha()]
        ciphertext_int = [ord(i) - ord('a') for i in ciphertext.lower() if i.isalpha()]
        
        for i, char in enumerate(ciphertext_int):
            if i < len(key_as_int):
                value = (char - key_as_int[i % key_length]) % 26
                plaintext.append(chr(value + ord('a')))
            else:
                plaintext.append(chr(char + ord('a')))

        return ''.join(plaintext)

    def rail_fence_decipher(self, encrypted_text, rails):
        """
        Deciphers the given ciphertext using the Rail Fence cipher.
        :param encrypted_text: The ciphertext to decipher, str.
        :param rails: The number of rails to use for decryption, int.
        :return: The deciphered plaintext, str.
        """
        if rails <= 0:
            return ""

        rail = [['\n' for _ in range(len(encrypted_text))] for _ in range(rails)]
        direction_down = False
        row, col = 0, 0

        for char in encrypted_text:
            if row == 0 or row == rails - 1:
                direction_down = not direction_down
            rail[row][col] = '*'
            col += 1
            row += 1 if direction_down else -1

        index = 0
        for i in range(rails):
            for j in range(len(encrypted_text)):
                if rail[i][j] == '*' and index < len(encrypted_text):
                    rail[i][j] = encrypted_text[index]
                    index += 1

        result = []
        row, col = 0, 0
        for i in range(len(encrypted_text)):
            if row == 0:
                direction_down = True
            if row == rails - 1:
                direction_down = False

            if rail[row][col] != '\n':
                result.append(rail[row][col])
                col += 1

            row += 1 if direction_down else -1

        return ''.join(result)