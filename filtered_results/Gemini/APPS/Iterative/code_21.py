def solve():
    n = int(input())
    a = list(map(int, input().split()))

    pos_min = a.index(1)
    pos_max = a.index(n)

    ans = max(abs(pos_min - pos_max), abs(pos_max - pos_min))
    
    ans = max(ans, abs(0 - pos_min))
    ans = max(ans, abs(n - 1 - pos_min))
    ans = max(ans, abs(0 - pos_max))
    ans = max(ans, abs(n - 1 - pos_max))
    
    ans = max(abs(0 - pos_min), abs(n - 1 - pos_min), abs(0 - pos_max), abs(n - 1 - pos_max))

    print(ans)

solve()