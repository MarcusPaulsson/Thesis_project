def minimum_traps(m, x):
    # Since GCD(x, m) = 1, the sequence will visit all the rooms
    # The number of unique rooms visited is m / GCD(x, m) = m / 1 = m
    # The number of traps needed is m - 1 (all rooms except room 0)
    # Plus we need to trap room 0 to ensure catching the mouse when it starts there
    return m

# Read input
m, x = map(int, input().split())
# Calculate and print the result
print(minimum_traps(m, x))