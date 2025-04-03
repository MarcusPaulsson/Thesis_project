def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    s = set()
    ans = 0
    
    for x in a:
        while x % 2 == 0:
            if x not in s:
                s.add(x)
                ans += 1
            x //= 2
    
    print(ans)

t = int(input())
for _ in range(t):
    solve()