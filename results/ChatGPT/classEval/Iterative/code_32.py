class DecryptionUtils:
    """
    This is a class that provides methods for decryption, including the Caesar cipher, Vigenere cipher, and Rail Fence cipher.
    """

    def __init__(self, key):
        """
        Initializes the decryption utility with a key.
        :param key: The key to use for decryption, str.
        """
        self.key = key.lower()  # Ensure key is in lowercase for consistency

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
        shift = shift % 26  # Normalize shift
        plaintext = []
        for char in ciphertext:
            if char.isalpha():
                base = ord('a') if char.islower() else ord('A')
                shifted = (ord(char) - base - shift) % 26 + base
                plaintext.append(chr(shifted))
            else:
                plaintext.append(char)
        return ''.join(plaintext)

    def vigenere_decipher(self, ciphertext):
        """
        Deciphers the given ciphertext using the Vigenere cipher.
        :param ciphertext: The ciphertext to decipher, str.
        :return: The deciphered plaintext, str.
        >>> d = DecryptionUtils('key')
        >>> d.vigenere_decipher('ifmmp')
        'ybocl'
        """
        plaintext = []
        key_length = len(self.key)
        key_as_int = [ord(i) - ord('a') for i in self.key]
        ciphertext_int = [ord(i) - ord('a') for i in ciphertext.lower() if i.isalpha()]

        for i, char in enumerate(ciphertext):
            if char.isalpha():
                value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
                plaintext.append(chr(value + ord('a')))
            else:
                plaintext.append(char)

        return ''.join(plaintext)

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
        if rails <= 0:
            return encrypted_text

        n = len(encrypted_text)
        rail = [['\n' for _ in range(n)] for _ in range(rails)]
        
        dir_down = None
        row, col = 0, 0

        for i in range(n):
            if row == 0:
                dir_down = True
            if row == rails - 1:
                dir_down = False

            rail[row][col] = encrypted_text[i]
            col += 1

            row += 1 if dir_down else -1

        result = []
        for i in range(rails):
            for j in range(n):
                if rail[i][j] != '\n':
                    result.append(rail[i][j])

        return ''.join(result)