def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    nice_indices = []
    for j in range(n):
        temp_a = a[:j] + a[j+1:]
        
        if not temp_a:
            continue
        
        total_sum = sum(temp_a)
        
        for k in range(len(temp_a)):
            if temp_a[k] == total_sum - temp_a[k]:
                nice_indices.append(j + 1)
                break
            
    print(len(nice_indices))
    print(*nice_indices)

solve()