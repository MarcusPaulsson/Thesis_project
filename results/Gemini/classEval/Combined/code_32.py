class DecryptionUtils:
    """
    This is a class that provides methods for decryption, including the Caesar cipher, Vigenere cipher, and Rail Fence cipher.
    """

    def __init__(self, key):
        """
        Initializes the decryption utility with a key.
        :param key: The key to use for decryption, str.
        """
        self.key = key

    def caesar_decipher(self, ciphertext, shift):
        """
        Deciphers the given ciphertext using the Caesar cipher.

        :param ciphertext: The ciphertext to decipher, str.
        :param shift: The shift to use for decryption, int.
        :return: The deciphered plaintext, str.

        >>> d = DecryptionUtils('key')
        >>> d.caesar_decipher('ifmmp', 1)
        'hello'
        """
        plaintext = ""
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
        Deciphers the given ciphertext using the Vigenere cipher.

        :param ciphertext: The ciphertext to decipher, str.
        :return: The deciphered plaintext, str.

        >>> d = DecryptionUtils('key')
        >>> d.vigenere_decipher('ifmmp')
        'ybocl'
        """
        plaintext = ""
        key = self.key
        key_length = len(key)
        for i, char in enumerate(ciphertext):
            if 'a' <= char <= 'z':
                start = 'a'
            elif 'A' <= char <= 'Z':
                start = 'A'
            else:
                plaintext += char
                continue

            key_char = key[i % key_length]
            key_shift = ord(key_char.lower()) - ord('a')
            shifted_char = chr((ord(char) - ord(start) - key_shift) % 26 + ord(start))
            plaintext += shifted_char
        return plaintext

    def rail_fence_decipher(self, encrypted_text, rails):
        """
        Deciphers the given ciphertext using the Rail Fence cipher.

        :param encrypted_text: The ciphertext to decipher, str.
        :param rails: The number of rails to use for decryption, int.
        :return: The deciphered plaintext, str.

        >>> d = DecryptionUtils('key')
        >>> d.rail_fence_decipher('Hoo!el,Wrdl l', 3)
        'Hello, World!'
        """
        n = len(encrypted_text)

        # Create the fence (matrix)
        fence = [['' for _ in range(n)] for _ in range(rails)]

        # Mark the rail pattern with '*'
        rail = 0
        down = True
        for i in range(n):
            fence[rail][i] = '*'
            if rail == rails - 1:
                down = False
            elif rail == 0:
                down = True

            if down:
                rail += 1
            else:
                rail -= 1

        # Fill the fence with the encrypted text
        index = 0
        for i in range(rails):
            for j in range(n):
                if fence[i][j] == '*':
                    fence[i][j] = encrypted_text[index]
                    index += 1

        # Read the fence in a zigzag manner to extract the plaintext
        rail = 0
        down = True
        plaintext = ''
        for i in range(n):
            plaintext += fence[rail][i]
            if rail == rails - 1:
                down = False
            elif rail == 0:
                down = True

            if down:
                rail += 1
            else:
                rail -= 1

        return plaintext