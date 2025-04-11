from collections import Counter
import sys

def find_x_y(divisors):
    count = Counter(divisors)
    # The largest number must be either x or y
    max_divisor = max(count)
    
    # Remove the largest number from the count
    count[max_divisor] -= 1
    if count[max_divisor] == 0:
        del count[max_divisor]
    
    # Now we need to find the other number
    # The second number must be the product of the remaining divisors
    product = 1
    for d, freq in count.items():
        product *= d ** freq
    
    return max_divisor, product

n = int(input().strip())
divisors = list(map(int, input().strip().split()))

x, y = find_x_y(divisors)
print(x, y)