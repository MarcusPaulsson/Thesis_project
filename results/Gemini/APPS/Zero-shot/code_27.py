def solve():
    n = int(input())
    s = input()
    
    ans = n
    
    for i in range(1, n // 2 + 1):
        prefix = s[:i]
        if s.startswith(prefix * 2):
            ans = min(ans, i + 1 + (n - 2 * i))
        elif s.startswith(prefix) and s[i:].startswith(prefix) and len(s[i:]) >= i:
            if s[i:].startswith(prefix):
                ans = min(ans, i+1+len(s) - 2*i)
            
    
    
    for i in range(1, n):
        prefix = s[:i]
        if s.startswith(prefix) and len(prefix) * 2 <= n:
            if s.startswith(prefix + prefix):
                ans = min(ans, len(prefix) + 1 + (n - 2*len(prefix)))
    
    print(ans)

solve()