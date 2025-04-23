def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    min_index = a.index(1)
    max_index = a.index(n)
    
    max_dist = abs(min_index - max_index)
    
    for i in range(n):
        temp_a = a[:]
        temp_a[min_index], temp_a[i] = temp_a[i], temp_a[min_index]
        
        new_min_index = temp_a.index(1)
        new_max_index = temp_a.index(n)
        
        max_dist = max(max_dist, abs(new_min_index - new_max_index))
        
    for i in range(n):
        temp_a = a[:]
        temp_a[max_index], temp_a[i] = temp_a[i], temp_a[max_index]
        
        new_min_index = temp_a.index(1)
        new_max_index = temp_a.index(n)
        
        max_dist = max(max_dist, abs(new_min_index - new_max_index))
        
    print(max_dist)

solve()