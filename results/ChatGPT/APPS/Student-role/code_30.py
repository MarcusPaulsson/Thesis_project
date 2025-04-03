def minimum_traps(m, x):
    # Since GCD(x, m) = 1, the x-mouse will visit all rooms by moving through them
    # The number of distinct rooms visited corresponds to Euler's Totient function φ(m)
    # which is the count of numbers up to m that are coprime to m.
    
    # To find the number of traps needed, we can just consider the number of rooms
    # that will be visited in one cycle.
    
    visited_rooms = 0
    room = 0
    
    while True:
        visited_rooms += 1
        room = (room * x) % m
        if room == 0:
            break
            
    return visited_rooms

# Read input
m, x = map(int, input().split())
# Output the result
print(minimum_traps(m, x))