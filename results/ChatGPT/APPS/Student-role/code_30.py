def min_traps(m, x):
    # Since GCD(x, m) = 1, the x-mouse will visit all rooms
    # The number of unique rooms visited is equal to m
    # The minimum number of traps needed is m - 1 (trapping all rooms except room 0)
    return m

m, x = map(int, input().split())
print(min_traps(m, x))