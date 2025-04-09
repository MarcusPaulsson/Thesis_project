def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print("NO")
        return

    a = [i + 1 for i in range(k)]
    remaining = n - k * (k + 1) // 2

    for i in range(k):
        a[i] += remaining // k

    remaining %= k

    for i in range(k - 1, k - 1 - remaining, -1):
        a[i] += 1

    for i in range(k - 1):
        if a[i + 1] > 2 * a[i]:
            diff = a[i + 1] - 2 * a[i]
            a[i + 1] -= diff
            a[k - 1] += diff
            if a[i+1] > 2* a[i]:
                print("NO")
                return
    
    is_valid = True
    for i in range(k - 1):
        if not (a[i] < a[i+1] <= 2 * a[i]):
            is_valid = False
            break

    if is_valid:
        print("YES")
        print(*a)
    else:
        print("NO")

solve()