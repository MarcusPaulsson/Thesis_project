def min_D_to_equalize(n, a):
    min_a = min(a)
    max_a = max(a)
    
    if max_a - min_a > 2 * (max_a - min_a) // 2:
        return -1
    
    if max_a == min_a:
        return 0
    
    return (max_a - min_a + 1) // 2

n = int(input())
a = list(map(int, input().split()))
print(min_D_to_equalize(n, a))