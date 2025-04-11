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
        d = unique_vals[1] - unique_vals[0]
        if d % 2 == 0:
            print(d // 2)
        else:
            print(d)
        return

    if len(unique_vals) == 3:
        if unique_vals[1] - unique_vals[0] == unique_vals[2] - unique_vals[1]:
            print(unique_vals[1] - unique_vals[0])
        else:
            print(-1)
        return

solve()