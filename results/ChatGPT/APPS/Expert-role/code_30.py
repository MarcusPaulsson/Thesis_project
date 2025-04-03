def min_traps(m, x):
    # To catch the x-mouse, we need to cover all reachable rooms.
    # The number of unique rooms visited by the x-mouse is given by Euler's Totient Function.
    # Since GCD(x, m) = 1, we can directly use m - 1 as the number of traps needed.
    
    return m - 1

# Read input
m, x = map(int, input().split())
# Output the result
print(min_traps(m, x))