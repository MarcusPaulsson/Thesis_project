def minimum_traps(m, x):
    # Since GCD(x, m) = 1, the number of distinct rooms visited is equal to m
    # The x-mouse will visit all rooms in m steps, so we need to place traps in m - 1 rooms
    # The only room we can skip is room 0, as it will always be visited.
    
    return m

m, x = map(int, input().split())
print(minimum_traps(m, x))