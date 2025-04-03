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
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                shift_base = ord('a') if char.islower() else ord('A')
                deciphered_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
                plaintext += deciphered_char
            else:
                plaintext += char
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
        plaintext = []
        key_length = len(self.key)
        key_as_int = [ord(i) - ord('a') for i in self.key.lower()]
        ciphertext_int = [ord(i) - ord('a') for i in ciphertext.lower()]

        for i in range(len(ciphertext_int)):
            value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
            plaintext.append(chr(value + ord('a')))
        return ''.join(plaintext)

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
        decrypted_text = [''] * rails
        rail = 0
        direction = 1  # 1 means going down, -1 means going up

        for char in encrypted_text:
            decrypted_text[rail] += char
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction *= -1

        return ''.join(decrypted_text)