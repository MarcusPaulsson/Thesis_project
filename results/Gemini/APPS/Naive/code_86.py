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
    
    add = remaining // k
    for i in range(k):
        a[i] += add

    remaining %= k
    
    for i in range(k - 1, -1, -1):
        if remaining > 0:
            a[i] += 1
            remaining -= 1
    
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