def mexican_wave(n, k, t):
    if t < k:
        return t + 1
    elif t < n:
        return k
    else:
        return n - (t - n + 1)

n, k, t = map(int, input().split())
print(mexican_wave(n, k, t))