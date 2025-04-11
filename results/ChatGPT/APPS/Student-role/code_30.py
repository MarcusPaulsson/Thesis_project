def minimum_traps(m, x):
    # Since GCD(x, m) = 1, the x-mouse will visit all rooms in a cycle of length m
    # The number of traps needed is equal to m - 1 (all rooms except room 0)
    return m

m, x = map(int, input().split())
print(minimum_traps(m, x))