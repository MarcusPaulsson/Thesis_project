from collections import Counter
import math

def find_x_y(n, divisors):
    counter = Counter(divisors)
    common_divisors = [d for d, count in counter.items() if count > 1]

    gcd = 1
    for d in common_divisors:
        gcd = math.gcd(gcd, d)

    x = gcd
    y = 1
    for d in divisors:
        if d % x == 0:
            y *= d // x

    return (x, y)

n = int(input().strip())
divisors = list(map(int, input().strip().split()))

x, y = find_x_y(n, divisors)
print(x, y)