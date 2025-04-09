def minimum_traps(m, x):
    # Since GCD(x, m) = 1, the x-mouse will visit all unique rooms before returning to the start.
    # Therefore, to catch the mouse, we need traps in all but one room.
    return m - 1

# Read input
m, x = map(int, input().strip().split())
# Output result
print(minimum_traps(m, x))