def minimum_traps(m, x):
    # Since GCD(x, m) = 1, the x-mouse will visit all rooms
    # in the cycle of length m. We can catch the x-mouse by
    # placing traps at every room that is visited in one full cycle.
    return m

# Read input
m, x = map(int, input().split())

# Output the minimum number of traps needed
print(minimum_traps(m, x))