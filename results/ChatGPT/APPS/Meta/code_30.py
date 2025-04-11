def minimum_traps(m, x):
    # Since GCD(x, m) = 1, the mouse will visit all rooms in a cycle.
    # The number of unique rooms visited is equal to the number of steps
    # until it returns to the starting room, which is m.
    
    # The number of traps needed is m - 1 (for all rooms except room 0)
    # plus 1 for room 0 itself.
    return m

# Read input
m, x = map(int, input().split())
# Output the result
print(minimum_traps(m, x))