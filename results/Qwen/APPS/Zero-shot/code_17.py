n, k, t = map(int, input().split())
print(min(t, n) - max(t - k, 0))