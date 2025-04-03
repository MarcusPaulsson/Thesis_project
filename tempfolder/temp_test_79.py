def get_divisors(n):
    divisors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.append(n)
    return divisors

def solve_case(n):
    divisors = get_divisors(n)
    divisors.sort()
    
    # To make sure no two adjacent numbers are coprime, we can place them in a specific order
    if len(divisors) == 2:
        # Only 2 divisors, they must be non-coprime already
        return divisors, 0
    
    # For more than 2 divisors, we can arrange them in a way to minimize moves
    order = []
    for i in range(len(divisors)):
        if i % 2 == 0:
            order.append(divisors[i])
    
    for i in range(len(divisors)):
        if i % 2 == 1:
            order.append(divisors[i])
    
    # If order is such that all adjacent pairs are not coprime, we need 0 moves
    moves_needed = 0
    
    # Check if all adjacent are not coprime
    for i in range(len(order)):
        a = order[i]
        b = order[(i + 1) % len(order)]
        if gcd(a, b) == 1:
            moves_needed += 1

    return order, moves_needed

from math import gcd
import sys

input = sys.stdin.read
data = input().split()
t = int(data[0])
results = []

for i in range(1, t + 1):
    n = int(data[i])
    order, moves = solve_case(n)
    results.append(f"{' '.join(map(str, order))}\n{moves}")

print("\n".join(results))