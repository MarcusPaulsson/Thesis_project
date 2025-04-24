def solve():
    n, k = map(int, input().split())

    if k == 1:
        print("YES")
        print(n)
        return

    if k * (k + 1) // 2 > n:
        print("NO")
        return

    a = [i + 1 for i in range(k)]
    remaining = n - sum(a)

    add = remaining // k
    rem = remaining % k

    for i in range(k):
        a[i] += add

    for i in range(k - 1, k - 1 - rem, -1):
        a[i] += 1

    valid = True
    for i in range(k - 1):
        if not (a[i] < a[i+1] <= 2 * a[i]):
            valid = False
            break
    
    if valid:
        print("YES")
        print(*a)
    else:
        print("NO")

solve()