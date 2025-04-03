from collections import Counter

def find_x_y(n, divisors):
    counter = Counter(divisors)
    gcd = 1
    
    # Finding the GCD of the numbers that appear twice
    for d in counter:
        if counter[d] == 2:
            gcd *= d
    
    x = gcd
    y = 1
    
    # Finding the other number using the divisors
    for d in counter:
        if counter[d] == 1:
            y *= d

    return x, y

# Read input
n = int(input())
divisors = list(map(int, input().split()))

# Get x and y
x, y = find_x_y(n, divisors)

# Print output
print(x, y)