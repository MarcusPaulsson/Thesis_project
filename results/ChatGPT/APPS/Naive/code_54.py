def find_minimum_d(n, a):
    min_a = min(a)
    max_a = max(a)
    
    # If all elements are the same
    if min_a == max_a:
        return 0
    
    # Check the case where max_a - min_a can be divided by 2
    if (max_a - min_a) % 2 == 0:
        D = (max_a - min_a) // 2
        return D
    else:
        return -1

# Read input
n = int(input())
a = list(map(int, input().split()))

# Get the result and print it
result = find_minimum_d(n, a)
print(result)