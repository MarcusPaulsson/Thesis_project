def get_divisors(n):
    divisors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.append(n)
    return divisors

def solve(n):
    divisors = get_divisors(n)
    divisors.sort()
    
    # The minimal number of moves needed to ensure no two adjacent numbers are coprime
    moves = 0
    
    # If there are only two divisors, we can directly check and return the result
    if len(divisors) == 2:
        return divisors, 0
    
    # An initial order that ensures we can minimize moves
    # For any composite number, we can arrange them in a way that
    # we have pairs of numbers that share a prime factor
    initial_order = []
    
    # We can create a simple arrangement where we put the smallest prime factor first
    # and then follow it with the other divisors
    prime_factors = []
    for d in divisors:
        if d < n and n % d == 0:
            prime_factors.append(d)
    
    # We can take the first prime factor and alternate with the rest
    if prime_factors:
        initial_order.append(prime_factors[0])
        for d in divisors:
            if d != prime_factors[0]:
                initial_order.append(d)
    
    return initial_order, moves

t = int(input())
for _ in range(t):
    n = int(input())
    order, moves = solve(n)
    print(" ".join(map(str, order)))
    print(moves)