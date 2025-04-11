def find_x_y(n, divisors):
    from collections import Counter
    
    # Count the occurrences of each divisor
    divisor_count = Counter(divisors)
    
    # Initialize x and y
    x = 1
    y = 1
    
    # Iterate through the counted divisors
    for d, count in divisor_count.items():
        if count == 2:
            # If the divisor appears twice, it is a common divisor
            x *= d
            y *= d
        elif count == 1:
            # If the divisor appears once, assign it to x or y
            if x < y:
                x *= d
            else:
                y *= d
    
    return x, y

# Input reading
n = int(input().strip())
divisors = list(map(int, input().strip().split()))

# Find x and y
x, y = find_x_y(n, divisors)

# Output the result
print(x, y)