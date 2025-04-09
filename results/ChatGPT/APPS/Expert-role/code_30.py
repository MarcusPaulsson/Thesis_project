def min_traps(m, x):
    # Since GCD(x, m) = 1, the sequence will visit m distinct rooms
    # until it returns to the starting position.
    # The number of unique rooms visited is equal to m.
    return m

m, x = map(int, input().split())
print(min_traps(m, x))