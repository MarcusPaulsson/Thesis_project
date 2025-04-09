def solve():
    n = int(input())
    s = input()
    
    ans = n
    for i in range(1, n // 2 + 1):
        if s.startswith(s[:i] * 2):
            ans = min(ans, i + 1 + (n - 2*i))
        elif s[:2*i].startswith(s[:i]):
            ans = min(ans, i + 1 + (n - 2*i))
            
    print(ans)

solve()