def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(0)
        return

    distinct_values = sorted(list(set(a)))

    if len(distinct_values) > 3:
        print(-1)
        return

    if len(distinct_values) == 1:
        print(0)
        return

    if len(distinct_values) == 2:
        x, y = distinct_values
        if (x + y) % 2 == 0:
            print((y - x) // 2)
        else:
            print(y - x)
        return

    if len(distinct_values) == 3:
        x, y, z = distinct_values
        if y - x == z - y:
            print(y - x)
        else:
            print(-1)
        return

solve()