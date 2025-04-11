def minimum_traps(m, x):
    # Since GCD(x, m) = 1, the x-mouse will visit all rooms in the cycle
    # The number of unique rooms visited is equal to m - 1
    # The number of traps needed is m - 1, plus one for room 0
    return m

m, x = map(int, input().split())
print(minimum_traps(m, x))