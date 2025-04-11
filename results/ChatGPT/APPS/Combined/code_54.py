def find_minimum_D(n, a):
    min_a = min(a)
    max_a = max(a)
    
    # Check if it's possible to make all elements equal
    if max_a - min_a > 2 * (max_a - min_a) // 2:
        return -1
    
    if max_a == min_a:
        return 0
    
    # Calculate the minimum D
    D = (max_a - min_a + 1) // 2
    return D

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(find_minimum_D(n, a))