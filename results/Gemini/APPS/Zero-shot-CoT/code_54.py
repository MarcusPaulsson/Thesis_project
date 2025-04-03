def solve():
    n = int(input())
    a = list(map(int, input().split()))

    unique_values = sorted(list(set(a)))

    if len(unique_values) > 3:
        print(-1)
        return

    if len(unique_values) == 1:
        print(0)
        return

    if len(unique_values) == 2:
        x, y = unique_values
        d = abs(x - y)
        if d % 2 == 0:
            print(d // 2)
        else:
            print(d)
        return

    if len(unique_values) == 3:
        x, y, z = unique_values
        if y - x == z - y:
            print(y - x)
        else:
            print(-1)
        return

solve()