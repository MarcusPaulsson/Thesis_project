def standing_spectators(n, k, t):
    if t <= k:
        return t
    elif t <= n:
        return k
    else:
        return n + k - t

# Example usage:
# n, k, t = map(int, input().split())
# print(standing_spectators(n, k, t))