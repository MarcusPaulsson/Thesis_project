def find_x_y(n, divisors):
    from collections import Counter
    
    # Count occurrences of each divisor
    divisor_count = Counter(divisors)
    
    # The maximum divisor is either x or y
    x = max(divisor_count)
    divisor_count[x] -= 1  # Remove one occurrence of x
    
    # Now find y by checking the remaining divisors
    y = 1
    for d, count in divisor_count.items():
        if count > 0:
            y *= d ** count
    
    return x, y

# Input reading
n = int(input().strip())
divisors = list(map(int, input().strip().split()))

# Finding x and y
x, y = find_x_y(n, divisors)

# Output the result
print(x, y)