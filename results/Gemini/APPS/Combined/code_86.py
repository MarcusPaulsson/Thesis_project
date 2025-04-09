def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print("NO")
        return

    a = [i + 1 for i in range(k)]
    remaining = n - k * (k + 1) // 2

    base = remaining // k
    rem = remaining % k

    for i in range(k):
        a[i] += base

    for i in range(k - 1, k - 1 - rem, -1):
        a[i] += 1
    
    for i in range(k - 1):
        if a[i+1] > 2 * a[i]:
            diff = a[i+1] - 2 * a[i]
            a[i+1] -= diff
            a[k-1] += diff
    
    is_valid = True
    for i in range(k - 1):
        if a[i+1] > 2 * a[i] or a[i] >= a[i+1]:
            is_valid = False
            break
    
    if is_valid:
        print("YES")
        print(*a)
    else:
        print("NO")

solve()