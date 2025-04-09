def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    min_instability = float('inf')
    
    for i in range(n):
        temp_a = a[:i] + a[i+1:]
        instability = max(temp_a) - min(temp_a)
        min_instability = min(min_instability, instability)
        
    print(min_instability)

solve()