def solve():
    n = int(input())
    a = list(map(int, input().split()))

    mn = float('inf')
    mx = float('-inf')

    for i in range(n):
        if a[i] == -1:
            if i > 0 and a[i-1] != -1:
                mn = min(mn, a[i-1])
                mx = max(mx, a[i-1])
            if i < n - 1 and a[i+1] != -1:
                mn = min(mn, a[i+1])
                mx = max(mx, a[i+1])

    if mn == float('inf'):
        k = 0
    else:
        k = (mn + mx) // 2

    b = []
    for x in a:
        if x == -1:
            b.append(k)
        else:
            b.append(x)

    m = 0
    for i in range(n - 1):
        m = max(m, abs(b[i] - b[i+1]))

    print(m, k)


t = int(input())
for _ in range(t):
    solve()