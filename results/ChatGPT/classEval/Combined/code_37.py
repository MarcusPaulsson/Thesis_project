class EncryptionUtils:
    """
    This class provides methods for encryption, including the Caesar cipher, Vigenere cipher, and Rail Fence cipher.
    """

    def __init__(self, key: str):
        """
        Initializes the class with a key.
        :param key: The key to use for encryption, str.
        """
        self.key = key.lower()

    def caesar_cipher(self, plaintext: str, shift: int) -> str:
        """
        Encrypts the plaintext using the Caesar cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param shift: The number of characters to shift each character in the plaintext, int.
        :return: The ciphertext, str.
        """
        result = []
        for char in plaintext:
            if char.isalpha():
                shift_base = ord('A') if char.isupper() else ord('a')
                shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
                result.append(shifted_char)
            else:
                result.append(char)
        return ''.join(result)

    def vigenere_cipher(self, plaintext: str) -> str:
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        """
        result = []
        key_length = len(self.key)
        key_index = 0

        for char in plaintext:
            if char.isalpha():
                shift_base = ord('A') if char.isupper() else ord('a')
                key_char = self.key[key_index % key_length]
                shift = ord(key_char) - ord('a')
                shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
                result.append(shifted_char)
                key_index += 1
            else:
                result.append(char)
        return ''.join(result)

    def rail_fence_cipher(self, plaintext: str, rails: int) -> str:
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param rails: The number of rails, int.
        :return: The ciphertext, str.
        """
        if rails <= 1:
            return plaintext
        
        rail = ['' for _ in range(rails)]
        direction_down = False
        row = 0

        for char in plaintext:
            rail[row] += char
            if row == 0 or row == rails - 1:
                direction_down = not direction_down
            row += 1 if direction_down else -1
        
        return ''.join(rail)

# Unittests
import unittest

class EncryptionUtilsTestCaesarCipher(unittest.TestCase):
    def test_caesar_cipher(self):
        encryption_utils = EncryptionUtils("key")
        self.assertEqual(encryption_utils.caesar_cipher("abc", 1), "bcd")
        self.assertEqual(encryption_utils.caesar_cipher("WORLD", -2), "UMPJB")
        self.assertEqual(encryption_utils.caesar_cipher("", 4), "")
        self.assertEqual(encryption_utils.caesar_cipher("abcxyz", 26), "abcxyz")
        self.assertEqual(encryption_utils.caesar_cipher("abcxyz", 27), "bcdyza")
        self.assertEqual(encryption_utils.caesar_cipher("123", 27), "123")

class EncryptionUtilsTestVigenereCipher(unittest.TestCase):
    def test_vigenere_cipher(self):
        encryption_utils = EncryptionUtils("key")
        self.assertEqual(encryption_utils.vigenere_cipher("abc"), "kfa")
        self.assertEqual(encryption_utils.vigenere_cipher("hello"), "rijvs")
        self.assertEqual(encryption_utils.vigenere_cipher("longkey"), "LpPjOjE")
        self.assertEqual(encryption_utils.vigenere_cipher("Hello, World! 123"), "Rijvs, Uyvjn! 123")
        self.assertEqual(encryption_utils.vigenere_cipher(""), "")

class EncryptionUtilsTestRailFenceCipher(unittest.TestCase):
    def test_rail_fence_cipher(self):
        encryption_utils = EncryptionUtils("key")
        self.assertEqual(encryption_utils.rail_fence_cipher("abc", 2), "acb")
        self.assertEqual(encryption_utils.rail_fence_cipher("hello", 2), "hloel")
        self.assertEqual(encryption_utils.rail_fence_cipher("longkey", 2), "ACEGbdf")
        self.assertEqual(encryption_utils.rail_fence_cipher("Hello, World! 123", 2), "Hlo ol!13el,Wrd 2")
        self.assertEqual(encryption_utils.rail_fence_cipher("", 2), "")
        self.assertEqual(encryption_utils.rail_fence_cipher("abcdefg", 3), "aebdfcg")

class EncryptionUtilsTestMain(unittest.TestCase):
    def test_main(self):
        encryption_utils = EncryptionUtils("key")
        self.assertEqual(encryption_utils.caesar_cipher("abc", 1), "bcd")
        self.assertEqual(encryption_utils.vigenere_cipher("abc"), "kfa")
        self.assertEqual(encryption_utils.rail_fence_cipher("abc", 2), "acb")

if __name__ == "__main__":
    unittest.main()