def minimum_traps(m, x):
    # Since GCD(x, m) = 1, the x-mouse will visit all rooms
    # except for the room 0, which it will visit only if it starts there.
    # The number of unique rooms visited is equal to m - 1.
    
    # The minimum number of traps needed is m - 1 + 1 (for room 0)
    return m

# Read input
m, x = map(int, input().split())
# Output the result
print(minimum_traps(m, x))