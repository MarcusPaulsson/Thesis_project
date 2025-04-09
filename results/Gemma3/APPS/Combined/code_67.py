def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    nice_indices = []
    for j in range(n):
        temp_a = a[:j] + a[j+1:]
        
        total_sum = sum(temp_a)
        
        is_good = False
        for k in range(len(temp_a)):
            if temp_a[k] == total_sum - temp_a[k]:
                is_good = True
                break
        
        if is_good:
            nice_indices.append(j + 1)
            
    print(len(nice_indices))
    print(*nice_indices)

solve()