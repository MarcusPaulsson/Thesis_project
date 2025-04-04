def min_time(d, k, a, b, t):
    if d <= k:
        return d * a
    else:
        return (d // k) * (k * a + t) + min(d % k, k) * b

d, k, a, b, t = map(int, input().split())
print(min_time(d, k, a, b, t))