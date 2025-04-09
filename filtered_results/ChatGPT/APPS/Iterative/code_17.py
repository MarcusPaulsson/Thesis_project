n, k, t = map(int, input().split())

if t <= k:
    result = t
elif t <= n:
    result = k
else:
    result = max(0, n + k - t)

print(result)