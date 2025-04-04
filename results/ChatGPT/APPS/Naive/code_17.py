def mexican_wave(n, k, t):
    if t <= k:
        return t
    elif t <= n:
        return k
    else:
        return n + k - t

# Input reading
n, k, t = map(int, input().strip().split())
print(mexican_wave(n, k, t))