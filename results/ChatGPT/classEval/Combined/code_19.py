class ChandrasekharSieve:
    """
    This class uses the Chandrasekhar's Sieve method to find all prime numbers within a specified range.
    """

    def __init__(self, n):
        """
        Initialize the ChandrasekharSieve class with the given limit.
        :param n: int, the upper limit for generating prime numbers
        """
        self.n = n
        self.primes = self.generate_primes()

    def generate_primes(self):
        """
        Generate prime numbers up to the specified limit using the Sieve of Eratosthenes algorithm.
        :return: list, a list of prime numbers
        """
        if self.n < 2:
            return []

        sieve = [True] * (self.n + 1)
        sieve[0], sieve[1] = False, False  # 0 and 1 are not prime numbers

        for start in range(2, int(self.n**0.5) + 1):
            if sieve[start]:
                for multiple in range(start * start, self.n + 1, start):
                    sieve[multiple] = False

        return [num for num, is_prime in enumerate(sieve) if is_prime]

    def get_primes(self):
        """
        Get the list of generated prime numbers.
        :return: list, a list of prime numbers
        """
        return self.primes


# Unit tests
import unittest

class ChandrasekharSieveTestGeneratePrimes(unittest.TestCase):
    def test_generate_primes(self):
        test_cases = [
            (20, [2, 3, 5, 7, 11, 13, 17, 19]),
            (18, [2, 3, 5, 7, 11, 13, 17]),
            (15, [2, 3, 5, 7, 11, 13]),
            (10, [2, 3, 5, 7]),
            (1, [])
        ]
        for n, expected in test_cases:
            with self.subTest(n=n):
                cs = ChandrasekharSieve(n)
                self.assertEqual(cs.generate_primes(), expected)

class ChandrasekharSieveTestGetPrimes(unittest.TestCase):
    def test_get_primes(self):
        test_cases = [
            (20, [2, 3, 5, 7, 11, 13, 17, 19]),
            (18, [2, 3, 5, 7, 11, 13, 17]),
            (15, [2, 3, 5, 7, 11, 13]),
            (10, [2, 3, 5, 7]),
            (1, [])
        ]
        for n, expected in test_cases:
            with self.subTest(n=n):
                cs = ChandrasekharSieve(n)
                self.assertEqual(cs.get_primes(), expected)

class ChandrasekharSieveTest(unittest.TestCase):
    def test_chandrasekhar_sieve(self):
        cs = ChandrasekharSieve(20)
        expected_primes = [2, 3, 5, 7, 11, 13, 17, 19]
        self.assertEqual(cs.generate_primes(), expected_primes)
        self.assertEqual(cs.get_primes(), expected_primes)