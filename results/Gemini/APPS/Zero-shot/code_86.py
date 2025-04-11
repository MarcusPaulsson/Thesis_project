def solve():
    n, k = map(int, input().split())

    if k == 1:
        if n >= 1:
            print("YES")
            print(n)
        else:
            print("NO")
        return

    if k * (k + 1) // 2 > n:
        print("NO")
        return

    a = [0] * k
    for i in range(k):
        a[i] = i + 1

    remaining = n - k * (k + 1) // 2

    for i in range(k - 1, -1, -1):
        add = min(remaining, 2 * a[i] - a[i] - 1)
        a[i] += add
        remaining -= add

    if remaining > 0:
        print("NO")
        return

    for i in range(k - 1):
        if not (a[i] < a[i+1] <= 2 * a[i]):
            print("NO")
            return

    print("YES")
    print(*a)

solve()