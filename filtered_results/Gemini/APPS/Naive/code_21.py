def solve():
    n = int(input())
    a = list(map(int, input().split()))

    pos_1 = a.index(1)
    pos_n = a.index(n)

    ans = abs(pos_1 - pos_n)
    
    ans = max(ans, abs(0 - pos_1))
    ans = max(ans, abs(n - 1 - pos_1))
    ans = max(ans, abs(0 - pos_n))
    ans = max(ans, abs(n - 1 - pos_n))

    print(ans)

solve()