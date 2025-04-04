def minimum_traps(m, x):
    # Since GCD(x, m) = 1, the movements of the x-mouse will cover all rooms
    # except the one where it starts, and it will cycle through all rooms.
    # The minimum number of traps needed is m - 1.
    
    return m - 1

# Read input
m, x = map(int, input().split())
# Print the result
print(minimum_traps(m, x))