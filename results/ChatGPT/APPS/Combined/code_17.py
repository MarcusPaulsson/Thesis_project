def standing_spectators(n, k, t):
    if t <= k:
        return t
    elif t <= n:
        return k
    else:
        return n + k - t

# Read input values
n, k, t = map(int, input().strip().split())
# Print the result
print(standing_spectators(n, k, t))