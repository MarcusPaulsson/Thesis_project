def minimum_traps(m, x):
    # Since GCD(x, m) = 1, the sequence will visit all m rooms.
    # The number of distinct rooms visited corresponds to the order of x modulo m.
    
    # The minimum number of traps needed is equal to the number of distinct
    # rooms the x-mouse can visit before repeating, which is m.
    
    return m - 1  # We can put traps in m-1 rooms.

# Input reading
m, x = map(int, input().strip().split())

# Output the result
print(minimum_traps(m, x))