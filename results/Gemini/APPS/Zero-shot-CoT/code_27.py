def solve():
    n = int(input())
    s = input()
    
    ans = n
    
    for i in range(1, n // 2 + 1):
        prefix = s[:i]
        if s[:2*i] == prefix + prefix:
            ans = min(ans, i + 1 + (n - 2*i))
        elif s.startswith(prefix):
            
            if n >= 2*i and s[:2*i].startswith(prefix):
                
                if s[:i] == s[i:2*i]:
                   
                   pass
                
    for i in range(1, n):
        if s[:i] == s[i:2*i] and 2*i <= n:
            ans = min(ans,i + 1 + (n - 2*i))
            
    print(ans)

solve()