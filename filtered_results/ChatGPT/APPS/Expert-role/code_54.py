def find_minimum_D(n, a):
    min_a = min(a)
    max_a = max(a)
    
    if min_a == max_a:
        return 0
    
    # Calculate the difference
    diff = max_a - min_a
    
    # If the difference is odd, we cannot split it evenly into two parts
    if diff % 2 != 0:
        return -1
    
    # The required D is half of the difference
    D = diff // 2
    return D

# Reading input
n = int(input())
a = list(map(int, input().split()))

# Finding and printing the result
result = find_minimum_D(n, a)
print(result)