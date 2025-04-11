from collections import Counter
import sys
import math

def find_x_y(divisors):
    count = Counter(divisors)
    # The largest number in the list must be either x or y
    max_divisor = max(divisors)
    
    # Calculate the product of all unique divisors
    product = 1
    for d in count:
        product *= d ** (count[d] // 2)
    
    # The two numbers x and y can be derived from the product and the largest divisor
    x = product * (max_divisor // math.gcd(product, max_divisor))
    y = product * (max_divisor // (x // max_divisor))
    
    return x, y

n = int(input().strip())
divisors = list(map(int, input().strip().split()))

x, y = find_x_y(divisors)
print(x, y)