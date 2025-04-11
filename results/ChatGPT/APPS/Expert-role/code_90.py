def can_reach_end(n, m, d, c):
    # Calculate the total length of platforms
    total_length = sum(c)
    
    # If the maximum jump distance is greater than or equal to the river width, we can always reach the end
    if d >= n + 1:
        result = [0] * n
        pos = 0
        for i in range(m):
            for j in range(c[i]):
                result[pos] = i + 1
                pos += 1
        return "YES", result
    
    # Check if we can place the platforms such that we can jump across
    result = [0] * n
    pos = 0
    for i in range(m):
        # Place the platform at the current position
        for j in range(c[i]):
            result[pos] = i + 1
            pos += 1
    
    # Check if we can jump from the last position of the last platform to n + 1
    last_platform_end = sum(c)
    if last_platform_end + d >= n + 1:
        return "YES", result
    
    return "NO", []

# Read input
n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Get the result
result = can_reach_end(n, m, d, c)

# Print the result
if result[0] == "NO":
    print("NO")
else:
    print("YES")
    print(" ".join(map(str, result[1])))