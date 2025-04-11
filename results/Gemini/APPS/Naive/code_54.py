def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(0)
        return

    unique_values = sorted(list(set(a)))

    if len(unique_values) > 3:
        print(-1)
        return

    if len(unique_values) == 1:
        print(0)
        return

    if len(unique_values) == 2:
        val1, val2 = unique_values
        d = abs(val1 - val2)
        if d % 2 == 0:
            print(d // 2)
        else:
            print(d // 2)
        return

    if len(unique_values) == 3:
        val1, val2, val3 = unique_values
        if val2 - val1 == val3 - val2:
            print(val2 - val1)
        else:
            print(-1)
        return

solve()