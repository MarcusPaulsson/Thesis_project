class ChandrasekharSieve:
    """
    This class implements the Chandrasekhar's Sieve method to find all prime numbers up to a specified limit.
    """

    def __init__(self, n):
        """
        Initialize the ChandrasekharSieve class with the given limit.
        
        :param n: int, the upper limit for generating prime numbers
        """
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
        sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

        for start in range(2, int(self.n**0.5) + 1):
            if sieve[start]:
                for multiple in range(start * start, self.n + 1, start):
                    sieve[multiple] = False

        return [num for num, is_prime in enumerate(sieve) if is_prime]

    def get_primes(self):
        """
        Retrieve the list of generated prime numbers.
        
        :return: list, a list of prime numbers
        """
        return self.primes