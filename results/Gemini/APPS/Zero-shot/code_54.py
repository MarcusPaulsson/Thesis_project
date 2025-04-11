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
        diff = abs(distinct_values[0] - distinct_values[1])
        if diff % 2 == 0:
            print(diff // 2)
        else:
            print(diff)
        return

    if len(distinct_values) == 3:
        v1, v2, v3 = distinct_values
        if v2 - v1 == v3 - v2:
            print(v2 - v1)
        else:
            print(-1)
        return


solve()