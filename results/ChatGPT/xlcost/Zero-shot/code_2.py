def sieve_of_eratosthenes(n):
    # Initialize a list to track prime numbers
    is_prime = [1] * (n + 1)
    is_prime[0] = is_prime[1] = 0  # 0 and 1 are not prime numbers
    primes = []

    for i in range(2, n + 1):
        if is_prime[i]:  # If current number is prime
            primes.append(i)
            for j in range(i * 2, n + 1, i):
                is_prime[j] = 0  # Mark multiples of i as non-prime

    return primes

def construct_array(n):
    primes = sieve_of_eratosthenes(n)
    A = [0] * (n + 1)
    prime_index = 0

    for i in range(1, n + 1):
        if prime_index < len(primes) and A[i] == 0:
            if A[i] == 0 and prime_index < len(primes):
                A[i] = primes[prime_index]
                prime_index += 1
            elif prime_index < len(primes):
                A[i] = primes[prime_index]
                prime_index += 1

    return A

# Driver Code
N = 10**6
resultant_array = construct_array(N)
print(resultant_array)