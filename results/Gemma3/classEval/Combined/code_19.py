class ChandrasekharSieve:
    """
    This is a class that uses the Chandrasekhar's Sieve method to find all prime numbers within the range
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
        """
        if self.n < 2:
            return []

        limit = self.n + 1
        is_prime = [True] * limit
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(self.n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, limit, i):
                    is_prime[j] = False

        primes = [i for i in range(2, limit) if is_prime[i]]
        return primes

    def get_primes(self):
        """
        Get the list of generated prime numbers.
        :return: list, a list of prime numbers
        """
        return self.primes