def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    w = list(map(int, input().split()))

    a.sort()
    w.sort()

    happiness = 0
    
    # Assign maximums
    l, r = 0, n - 1
    for i in range(k):
        if w[i] == 1:
            happiness += 2 * a[r]
            r -= 1

    # Assign remaining
    l = 0
    for i in range(k - 1, -1, -1):
        if w[i] > 1:
            happiness += a[r]
            happiness += a[l]
            r -= 1
            l += w[i] - 1

    print(happiness)


t = int(input())
for _ in range(t):
    solve()