n, k, t = map(int, input().split())

if t <= k:
    print(t)
elif t <= n:
    print(k)
elif t <= n + k:
    print(n + k - t)