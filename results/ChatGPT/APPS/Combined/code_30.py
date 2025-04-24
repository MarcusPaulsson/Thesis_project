def minimum_traps(m: int, x: int) -> int:
    """
    Calculate the minimum number of traps needed to catch the x-mouse in a campus with m rooms.
    
    Parameters:
    m (int): The number of rooms.
    x (int): The parameter of the x-mouse.
    
    Returns:
    int: The minimum number of traps required.
    """
    return m - 1

# Read input
m, x = map(int, input().split())
# Output the result
print(minimum_traps(m, x))