def min_traps(m, x):
    # Since GCD(x, m) = 1, the x-mouse will visit all m rooms.
    # To catch the x-mouse, we need traps in all rooms except the starting room.
    return m - 1

m, x = map(int, input().split())
print(min_traps(m, x))