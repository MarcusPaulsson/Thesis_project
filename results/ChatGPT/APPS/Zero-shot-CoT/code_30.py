def min_traps(m, x):
    # Since GCD(x, m) = 1, the x-mouse will visit all rooms
    # The number of unique rooms visited is equal to the number of steps
    # it takes to return to the starting room, which is m.
    # The number of traps needed is m - 1, but we can place a trap in room 0
    # and then we need to cover the remaining m - 1 rooms.
    
    # The number of traps needed is m - 1 + 1 (for room 0)
    return m

# Read input
m, x = map(int, input().split())
# Output the result
print(min_traps(m, x))