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
        >>> d = DecryptionUtils('key')
        >>> d.vigenere_decipher('ifmmp')
        'ybocl'

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
            shifted_char = chr((ord(char) - ord(start) - key_shift) % 26 + ord(start))
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
        length = len(encrypted_text)
        fence = [['' for _ in range(length)] for _ in range(rails)]
        rail = 0
        direction = 1  # 1 for down, -1 for up

        # Mark the positions where characters will be placed
        for i in range(length):
            fence[rail][i] = '*'
            rail += direction
            if rail == rails - 1 or rail == 0:
                direction *= -1

        # Fill the fence with the encrypted text
        index = 0
        for i in range(rails):
            for j in range(length):
                if fence[i][j] == '*':
                    fence[i][j] = encrypted_text[index]
                    index += 1

        # Read the fence in a zigzag manner to get the plaintext
        plaintext = ''
        rail = 0
        direction = 1
        for i in range(length):
            plaintext += fence[rail][i]
            rail += direction
            if rail == rails - 1 or rail == 0:
                direction *= -1

        return plaintext