def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    min_d = float('inf')
    
    for d in range(101):
        possible = False
        for i in range(1 << n):
            temp_a = []
            for j in range(n):
                if (i >> j) & 1:
                    temp_a.append(a[j] + d)
                elif (i >> j) & 2:
                    temp_a.append(a[j] - d)
                else:
                    temp_a.append(a[j])
            
            if len(set(temp_a)) == 1:
                possible = True
                break
        
        if possible:
            min_d = min(min_d, d)
    
    if min_d == float('inf'):
        print(-1)
    else:
        print(min_d)

solve()