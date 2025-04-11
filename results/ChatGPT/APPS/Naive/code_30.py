def minimum_traps(m, x):
    # Since GCD(x, m) = 1, the x-mouse will visit all rooms
    # The number of unique rooms visited is equal to m - 1
    # We need to place traps in the starting room and the rooms it visits
    return m - 1

# Read input
m, x = map(int, input().split())
# Calculate and print the result
print(minimum_traps(m, x))