def minimum_D(n, a):
    min_a = min(a)
    max_a = max(a)
    
    if min_a == max_a:
        return 0
    
    difference = max_a - min_a
    if difference % 2 != 0:
        return -1
    
    D = difference // 2
    return D

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(minimum_D(n, a))