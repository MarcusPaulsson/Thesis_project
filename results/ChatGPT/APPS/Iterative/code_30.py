def min_traps(m, x):
    # Since GCD(x, m) = 1, the x-mouse will visit all rooms except for room 0.
    # Therefore, we need to set traps for all the remaining m-1 rooms.
    return m - 1

# Input reading
m, x = map(int, input().split())
# Output the result
print(min_traps(m, x))