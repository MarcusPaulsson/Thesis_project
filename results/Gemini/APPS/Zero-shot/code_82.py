def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    if n == 2:
        print(p[1], p[0])
        return
    
    p_prime = list(reversed(p))
    print(*p_prime)

t = int(input())
for _ in range(t):
    solve()