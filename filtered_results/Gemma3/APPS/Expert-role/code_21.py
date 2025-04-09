def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    min_idx = a.index(1)
    max_idx = a.index(n)
    
    max_dist = abs(min_idx - max_idx)
    
    for i in range(n):
        temp_a = a[:]
        temp_a[min_idx], temp_a[i] = temp_a[i], temp_a[min_idx]
        
        new_min_idx = temp_a.index(1)
        new_max_idx = temp_a.index(n)
        
        max_dist = max(max_dist, abs(new_min_idx - new_max_idx))
        
    for i in range(n):
        temp_a = a[:]
        temp_a[max_idx], temp_a[i] = temp_a[i], temp_a[max_idx]
        
        new_min_idx = temp_a.index(1)
        new_max_idx = temp_a.index(n)
        
        max_dist = max(max_dist, abs(new_min_idx - new_max_idx))
        
    print(max_dist)

solve()