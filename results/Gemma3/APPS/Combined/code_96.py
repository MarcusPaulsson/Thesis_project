def solve():
    n = int(input())
    q = list(map(int, input().split()))
    
    p = [0] * n
    p[0] = 1
    
    for i in range(n - 1):
        p[i+1] = p[i] + q[i]
        
    
    if any(x < 1 or x > n for x in p):
        print(-1)
        return
    
    seen = set()
    for x in p:
        if x in seen:
            print(-1)
            return
        seen.add(x)
        
    print(*p)

solve()