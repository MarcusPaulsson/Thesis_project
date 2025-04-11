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
        diff = abs(unique_vals[0] - unique_vals[1])
        if diff % 2 == 0:
            print(diff // 2)
        else:
            print(diff)
        return

    if len(unique_vals) == 3:
        x, y, z = unique_vals
        if y - x == z - y:
            print(y - x)
        else:
            print(-1)
        return

solve()