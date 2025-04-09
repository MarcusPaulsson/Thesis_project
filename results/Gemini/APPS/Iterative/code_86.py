def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print("NO")
        return

    a = [i + 1 for i in range(k)]
    remaining = n - sum(a)

    add = remaining // k
    rem = remaining % k

    for i in range(k):
        a[i] += add

    for i in range(k):
        if i < rem:
            a[k - 1 - i] += 1

    for i in range(k - 1):
        if not (a[i] < a[i+1] <= 2 * a[i]):
            print("NO")
            return

    print("YES")
    print(*a)

solve()