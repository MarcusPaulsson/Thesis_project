def solve():
    n = int(input())
    s = input()
    
    ans = n
    
    for i in range(1, n // 2 + 1):
        prefix = s[:i]
        if s[:2*i].startswith(prefix) and s.startswith(prefix * 2):
            
            
            
            ops = i + 1 + (n - 2*i)
            ans = min(ans, ops)
        elif s[:i] == s[i:2*i] and  2*i <= n:
            ops = i + 1 + (n-2*i)
            ans = min(ans, ops)
            
    print(ans)

solve()