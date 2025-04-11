def minimum_traps(m, x):
    # The number of traps needed is equal to m - 1 (for rooms 1 to m-1) + 1 (for room 0)
    return m - 1

m, x = map(int, input().split())
print(minimum_traps(m, x))