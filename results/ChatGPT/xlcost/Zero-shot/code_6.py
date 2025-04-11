def power_mod(x, y, p):
    result = 1
    x = x % p
    while y > 0:
        if (y & 1) == 1:  # If y is odd
            result = (result * x) % p
        y = y >> 1  # y = y // 2
        x = (x * x) % p
    return result

def total_ways(N, M):
    MOD = 10**9 + 7
    
    # Number of even indexed boxes
    even_boxes = N // 2
    
    # Number of partitions of even indexed boxes
    partitions = power_mod(2, even_boxes, MOD)
    
    # Number of ways to distribute M distinct objects into even indexed boxes
    ways_to_distribute = power_mod(partitions, M, MOD)
    
    return ways_to_distribute

# Driver Code
N = 10  # number of boxes
M = 5   # number of distinct objects
result = total_ways(N, M)
print(result)