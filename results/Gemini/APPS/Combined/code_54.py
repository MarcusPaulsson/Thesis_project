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
        diff = unique_values[1] - unique_values[0]
        if diff % 2 == 0:
            print(diff // 2)
        else:
            print(diff)
        return

    if len(unique_values) == 3:
        x, y, z = unique_values
        if y - x == z - y:
            print(y - x)
        else:
            print(-1)
        return

solve()