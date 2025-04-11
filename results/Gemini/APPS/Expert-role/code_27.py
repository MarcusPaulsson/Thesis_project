def solve():
    n = int(input())
    s = input()
    
    ans = n
    
    for i in range(1, n // 2 + 1):
        prefix = s[:i]
        if s[:2*i].startswith(prefix):
            ans = min(ans, n - i + 1)
            
    print(ans)

solve()