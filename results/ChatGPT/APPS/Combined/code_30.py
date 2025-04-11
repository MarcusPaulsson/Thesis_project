def minimum_traps(m, x):
    # The number of traps needed is equal to the number of unique rooms
    # visited before returning to the starting point, which is m - 1.
    return m - 1

# Read input
m, x = map(int, input().split())
# Output the result
print(minimum_traps(m, x))