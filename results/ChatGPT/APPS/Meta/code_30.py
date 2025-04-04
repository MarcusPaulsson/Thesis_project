def minimum_traps(m, x):
    # Since GCD(x, m) = 1, x has a multiplicative inverse mod m
    # The minimum number of traps needed is the number of distinct rooms the mouse visits
    # which is equal to the order of x modulo m.
    
    traps = 0
    visited = set()
    current_room = 0
    
    while current_room not in visited:
        visited.add(current_room)
        current_room = (current_room * x) % m
        traps += 1
    
    return traps

# Input reading
m, x = map(int, input().split())
# Output the result
print(minimum_traps(m, x))