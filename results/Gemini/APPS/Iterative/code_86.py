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

    for i in range(k):
        add = remaining // k
        a[i] += add
    
    remaining %= k

    for i in range(k - 1, -1, -1):
        if remaining > 0:
            a[i] += 1
            remaining -= 1

    for i in range(k - 1):
        if not (a[i] < a[i+1] <= 2 * a[i]):
            print("NO")
            return
    
    print("YES")
    print(*a)

solve()