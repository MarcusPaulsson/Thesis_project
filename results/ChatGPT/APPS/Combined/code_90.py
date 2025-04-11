def can_cross_river(n, m, d, c):
    total_length = sum(c)
    
    # If the maximum jump distance allows reaching the end directly
    if d >= n + 1:
        result = [0] * n
        position = 0
        for i in range(m):
            for j in range(c[i]):
                result[position] = i + 1
                position += 1
        return "YES", result
    
    # Calculate the minimum required gaps between platforms
    min_required_gaps = (m - 1) * (d - 1)
    
    # Check if the total length of platforms and required gaps fit in the river
    if total_length + min_required_gaps > n:
        return "NO", []
    
    # Construct the result array
    result = [0] * n
    position = 0
    for i in range(m):
        # Place the platform
        for j in range(c[i]):
            result[position] = i + 1
            position += 1
        # Add a gap if it's not the last platform
        if i < m - 1:
            position += (d - 1)  # Leave space for the next jump
    
    return "YES", result

# Input reading
n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Function call
result = can_cross_river(n, m, d, c)

# Output result
print(result[0])
if result[0] == "YES":
    print(" ".join(map(str, result[1])))