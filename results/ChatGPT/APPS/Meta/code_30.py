def minimum_traps(m, x):
    # Since GCD(x, m) = 1, we can find the number of unique rooms visited
    # using the property that they form a complete cycle in modular arithmetic.
    visited_rooms = m // gcd(m, x)
    return visited_rooms

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Input
m, x = map(int, input().split())
# Output
print(minimum_traps(m, x))