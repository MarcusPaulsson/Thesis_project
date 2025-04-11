def solve():
    n = int(input())
    a = list(map(int, input().split()))

    pos_min = a.index(1)
    pos_max = a.index(n)

    ans = max(abs(pos_min - 0), abs(pos_min - (n - 1)), abs(pos_max - 0), abs(pos_max - (n - 1)))

    print(ans)

solve()