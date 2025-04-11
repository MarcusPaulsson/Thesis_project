def can_reach_end(n, m, d, c):
    river = [0] * n  # Initialize the river array

    # If the maximum jump distance allows reaching the end directly
    if d >= n + 1:
        position = 0
        for i in range(m):
            for j in range(c[i]):
                river[position] = i + 1
                position += 1
        return "YES", river

    position = 0  # Start placing platforms
    for i in range(m):
        # Place the platform at the current position
        for j in range(c[i]):
            if position < n:
                river[position] = i + 1
                position += 1
        
        # Move to the next available position after placing the current platform
        position += d  # Jump to the next possible position

    # Check if we have filled the river correctly
    if position <= n:
        return "YES", river
    else:
        return "NO", []

# Input reading
n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Function call and output
result, river = can_reach_end(n, m, d, c)
print(result)
if result == "YES":
    print(" ".join(map(str, river)))