def minimum_traps(m, x):
    # Since GCD(x, m) = 1, the sequence will visit all rooms
    # The number of unique rooms visited is equal to the number of steps until we return to the starting room
    # This is equal to m because of the properties of modular arithmetic with coprime numbers
    return m

# Read input
m, x = map(int, input().split())
# Output the result
print(minimum_traps(m, x))