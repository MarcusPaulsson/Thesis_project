def find_x_y(n, divisors):
    from collections import Counter
    
    # Count the occurrences of each divisor
    count = Counter(divisors)
    
    # The maximum divisor must be either x or y
    max_divisor = max(count)
    
    # Initialize x and y
    x = max_divisor
    y = 1
    
    # Iterate through the divisors to find y
    for d in count:
        if count[d] == 1:  # If the divisor appears only once, it belongs to y
            y *= d
        elif count[d] == 2:  # If it appears twice, it belongs to both x and y
            continue
    
    return x, y

# Input reading
n = int(input())
divisors = list(map(int, input().split()))

# Find x and y
x, y = find_x_y(n, divisors)

# Output the result
print(x, y)