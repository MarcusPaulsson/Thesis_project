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
        >>> d = DecryptionUtils('key')
        >>> d.vigenere_decipher('ifmmp')
        'ybocl'

        """
        key = self.key
        plaintext = ''
        key_length = len(key)
        for i in range(len(ciphertext)):
            char = ciphertext[i]
            if 'a' <= char <= 'z':
                key_char = key[i % key_length]
                key_shift = ord(key_char) - ord('a')
                start = ord('a')
                decrypted_char = chr((ord(char) - start - key_shift) % 26 + start)
            elif 'A' <= char <= 'Z':
                key_char = key[i % key_length]
                key_shift = ord(key_char.lower()) - ord('a')
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
        >>> d = DecryptionUtils('key')
        >>> d.rail_fence_decipher('Hoo!el,Wrdl l', 3)
        'Hello, World!'

        """
        length = len(encrypted_text)
        fence = [['' for _ in range(length)] for _ in range(rails)]
        rail = 0
        down = True

        for i in range(length):
            fence[rail][i] = '*'
            if rail == rails - 1:
                down = False
            elif rail == 0:
                down = True

            if down:
                rail += 1
            else:
                rail -= 1

        index = 0
        for i in range(rails):
            for j in range(length):
                if fence[i][j] == '*':
                    fence[i][j] = encrypted_text[index]
                    index += 1

        rail = 0
        down = True
        result = ''
        for i in range(length):
            result += fence[rail][i]
            if rail == rails - 1:
                down = False
            elif rail == 0:
                down = True

            if down:
                rail += 1
            else:
                rail -= 1

        return result