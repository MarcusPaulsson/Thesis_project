def solve():
    n = int(input())
    s = input()
    
    ans = n
    
    for i in range(1, n // 2 + 1):
        prefix = s[:i]
        if s.startswith(prefix * 2):
            ans = min(ans, n - i)
        elif s[:2*i].startswith(prefix):
            if s.startswith(prefix):
                ans = min(ans, n - i)
    
    print(ans)

solve()