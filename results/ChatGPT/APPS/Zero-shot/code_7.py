n = int(input().strip())
f = list(map(int, input().strip().split()))

# Find the friends who want to give gifts (f_i != 0) and those who have not decided (f_i == 0)
givers = set(range(1, n + 1)) - set(f)
unknowns = [i + 1 for i in range(n) if f[i] == 0]

# Create a mapping of who should give gifts to whom
result = f[:]

# We need to ensure that we can fill in the zeros without giving a gift to oneself
for u in unknowns:
    for g in givers:
        if g != u:
            result[u - 1] = g
            givers.remove(g)
            break

print(' '.join(map(str, result)))