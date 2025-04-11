def find_minimum_D(n, a):
    min_a = min(a)
    max_a = max(a)
    
    if min_a == max_a:
        return 0  # All elements are already equal
    
    # The difference between max and min
    diff = max_a - min_a
    
    # If the difference is odd, we cannot make all elements equal
    if diff % 2 != 0:
        return -1
    
    # The minimum D is half the difference
    return diff // 2

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(find_minimum_D(n, a))