def minimum_traps(m, x):
    # Since GCD(x, m) = 1, x has an inverse modulo m
    # The number of distinct rooms visited by the x-mouse is the order of x mod m
    # which is equal to m since GCD(x, m) = 1.
    
    # We can place traps in a way to catch the x-mouse effectively.
    # We need to find the minimum number of traps, which is equal to the size of the cycle.
    
    # To find the cycle size, we can use the fact that the order of x modulo m is m.
    # The minimum number of traps needed is m / gcd(x, m) since GCD(x, m) = 1, it simplifies to m.
    
    # Since we need to catch the mouse in the cycle created by its movements,
    # We can iterate until we cycle back to the starting position.
    
    visited = set()
    current = 0
    count = 0
    
    while current not in visited:
        visited.add(current)
        current = (current * x) % m
        count += 1
    
    return count

# Input reading
m, x = map(int, input().split())
# Output the minimum number of traps needed
print(minimum_traps(m, x))