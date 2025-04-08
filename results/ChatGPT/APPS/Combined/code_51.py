from collections import Counter

def find_x_y(n, divisors):
    divisor_count = Counter(divisors)
    
    x, y = 1, 1

    for d, count in divisor_count.items():
        if count == 2:
            x *= d
            y *= d
        else:
            if x % d != 0:
                x *= d
            else:
                y *= d
    
    return x, y

# Input reading
n = int(input().strip())
divisors = list(map(int, input().strip().split()))

# Finding x and y
x, y = find_x_y(n, divisors)

# Output result
print(x, y)