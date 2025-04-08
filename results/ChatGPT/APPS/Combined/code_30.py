def minimum_traps(m, x):
    # The number of unique rooms visited by the x-mouse is equal to m,
    # and we need traps in all rooms except room 0.
    return m - 1

# Read input
m, x = map(int, input().split())
# Calculate and print the minimum number of traps needed
print(minimum_traps(m, x))