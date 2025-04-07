import math

class ChandrasekharSieve:
    """
    This is a class that uses the Sieve of Eratosthenes method to find all prime numbers within the range.
    The Sieve of Eratosthenes is often referred to as the Chandrasekhar sieve in some contexts, although
    Chandrasekhar's primary contributions were in astrophysics.
    """

    def __init__(self, n):
        """
        Initialize the ChandrasekharSieve class with the given limit.
        :param n: int, the upper limit for generating prime numbers
        """
        if not isinstance(n, int):
            raise TypeError("n must be an integer")
        if n < 0:
            raise ValueError("n must be a non-negative integer")
        self.n = n
        self.primes = self._generate_primes()

    def _generate_primes(self):
        """
        Generate prime numbers up to the specified limit using the Sieve of Eratosthenes algorithm.
        :return: list, a list of prime numbers
        """
        if self.n < 2:
            return []

        sieve = [True] * (self.n + 1)
        sieve[0] = sieve[1] = False

        for p in range(2, int(math.sqrt(self.n)) + 1):
            if sieve[p]:
                for i in range(p*p, self.n + 1, p):
                    sieve[i] = False

        primes = [p for p in range(2, self.n + 1) if sieve[p]]
        return primes

    def get_primes(self):
        """
        Get the list of generated prime numbers.
        :return: list, a list of prime numbers
        """
        return self.primes

    def __repr__(self):
        return f"ChandrasekharSieve(n={self.n})"