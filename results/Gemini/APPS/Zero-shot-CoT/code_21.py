def solve():
    n = int(input())
    a = list(map(int, input().split()))

    pos_min = a.index(1)
    pos_max = a.index(n)

    ans = 0
    ans = max(ans, abs(0 - pos_min))
    ans = max(ans, abs(n - 1 - pos_min))
    ans = max(ans, abs(0 - pos_max))
    ans = max(ans, abs(n - 1 - pos_max))
    
    print(ans)

solve()