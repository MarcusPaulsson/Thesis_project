def minimum_D(n, a):
    min_a = min(a)
    max_a = max(a)
    
    if max_a == min_a:
        return 0  # All elements are already equal
    
    diff = max_a - min_a
    
    # Check if the difference is odd
    if diff % 2 != 0:
        return -1  # Impossible to make all equal
    
    D = diff // 2
    
    # Check if we can achieve equal elements with the chosen D
    for value in a:
        if not (min_a <= value + D <= max_a) and not (min_a <= value - D <= max_a):
            return -1
    
    return D

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(minimum_D(n, a))