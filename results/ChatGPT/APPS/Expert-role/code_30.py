def minimum_traps(m, x):
    # Since GCD(x, m) = 1, the x-mouse will visit all rooms in the cycle
    # The number of unique rooms visited is equal to m
    # The number of traps needed is equal to the number of unique rooms visited
    return m

m, x = map(int, input().split())
print(minimum_traps(m, x))