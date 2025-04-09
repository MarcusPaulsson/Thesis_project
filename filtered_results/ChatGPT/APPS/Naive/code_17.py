def standing_spectators(n, k, t):
    if t <= k:
        return t
    elif t <= n:
        return k
    else:
        return n + k - t

# Read input
n, k, t = map(int, input().split())
# Output the result
print(standing_spectators(n, k, t))