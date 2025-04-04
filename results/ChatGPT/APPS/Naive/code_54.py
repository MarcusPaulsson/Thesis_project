def minimum_D(n, a):
    min_a = min(a)
    max_a = max(a)
    
    if min_a == max_a:
        return 0
    
    # The possible values for D that can balance the elements
    # D should be (max_a - min_a) / 2
    D = (max_a - min_a) / 2
    
    if (max_a - min_a) % 2 != 0:
        return -1
    
    return int(D)

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(minimum_D(n, a))