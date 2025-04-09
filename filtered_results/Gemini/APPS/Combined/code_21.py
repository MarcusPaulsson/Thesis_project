def solve():
    n = int(input())
    a = list(map(int, input().split()))

    pos_min = a.index(1)
    pos_max = a.index(n)

    ans = max(pos_min, pos_max, n - 1 - pos_min, n - 1 - pos_max)

    print(ans)

solve()