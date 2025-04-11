def min_traps(m, x):
    # Since GCD(x, m) = 1, x is coprime to m
    # The number of distinct rooms visited is equal to m - 1
    # The number of traps needed is equal to the number of distinct rooms visited
    # which is m - 1, plus one for room 0.
    return m

m, x = map(int, input().split())
print(min_traps(m, x))