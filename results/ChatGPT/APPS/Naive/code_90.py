def can_cross_river(n, m, d, platforms):
    total_length = sum(platforms)
    if total_length + (m - 1) > n:
        return "NO"

    result = [0] * n
    current_position = 0

    for i in range(m):
        platform_length = platforms[i]
        # Place the platform at the furthest position we can
        start_position = current_position + 1
        end_position = start_position + platform_length - 1
        
        # Check if we can place the platform without exceeding the river width
        if end_position > n:
            return "NO"
        
        # Fill the result array with the platform index
        for j in range(platform_length):
            result[start_position + j - 1] = i + 1
        
        # Update the current position to the end of the current platform
        current_position = end_position

    return "YES\n" + " ".join(map(str, result))

# Input reading
n, m, d = map(int, input().split())
platforms = list(map(int, input().split()))

# Output the result
print(can_cross_river(n, m, d, platforms))