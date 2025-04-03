def min_D_to_equal_elements(n, a):
    min_a = min(a)
    max_a = max(a)
    
    if min_a == max_a:
        return 0
    
    diff = max_a - min_a
    
    if diff % 2 == 0:
        return diff // 2
    else:
        return -1

n = int(input())
a = list(map(int, input().split()))
print(min_D_to_equal_elements(n, a))