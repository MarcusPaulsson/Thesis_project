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
        Generate prime numbers up to the specified limit using the Chandrasekhar sieve algorithm.
        :return: list, a list of prime numbers
        >>> cs = ChandrasekharSieve(20)
        >>> cs.generate_primes()
        [2, 3, 5, 7, 11, 13, 17, 19]
        """
        if self.n < 2:
            return []

        is_prime = [True] * (self.n + 1)
        is_prime[0], is_prime[1] = False, False  # 0 and 1 are not prime numbers
        
        for i in range(2, int(self.n**0.5) + 1):
            if is_prime[i]:
                for multiple in range(i * i, self.n + 1, i):
                    is_prime[multiple] = False

        return [num for num, prime in enumerate(is_prime) if prime]

    def get_primes(self):
        """
        Get the list of generated prime numbers.
        :return: list, a list of prime numbers
        >>> cs = ChandrasekharSieve(20)
        >>> cs.get_primes()
        [2, 3, 5, 7, 11, 13, 17, 19]
        """
        return self.primes