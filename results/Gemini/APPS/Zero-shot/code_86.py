def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print("NO")
        return

    a = [i + 1 for i in range(k)]
    remaining = n - sum(a)
    
    if remaining == 0:
        print("YES")
        print(*a)
        return

    increment = remaining // k
    a = [x + increment for x in a]
    remaining -= increment * k

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