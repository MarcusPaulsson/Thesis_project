def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(0)
        return

    unique_vals = sorted(list(set(a)))

    if len(unique_vals) > 3:
        print(-1)
        return

    if len(unique_vals) == 1:
        print(0)
        return

    if len(unique_vals) == 2:
        val1, val2 = unique_vals
        if (val1 + val2) % 2 == 0:
            print((val2 - val1) // 2)
        else:
            print(val2 - val1)
        return

    if len(unique_vals) == 3:
        val1, val2, val3 = unique_vals
        if val2 - val1 == val3 - val2:
            print(val2 - val1)
        else:
            print(-1)
        return

solve()