def mexican_wave(n, k, t):
    if t <= k:
        return t
    elif t <= n:
        return k
    else:  # t > n
        return n + k - t

# Read input values
n, k, t = map(int, input().split())
# Print the result
print(mexican_wave(n, k, t))