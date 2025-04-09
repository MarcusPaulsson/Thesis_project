def can_cross_river(n, m, d, c):
    result = [0] * n
    current_position = 0

    for i in range(m):
        platform_length = c[i]
        start_position = current_position + 1

        # Place the platform in the result array
        for j in range(platform_length):
            if start_position + j < n:
                result[start_position + j] = i + 1  # 1-based index

        # Update the current position to the end of the current platform
        current_position = start_position + platform_length - 1

        # Check if we can reach the next platform
        if i < m - 1 and (current_position + 1 + d < n):
            return "NO"

    return "YES", result

# Read input values
n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Call the function and get the result
result = can_cross_river(n, m, d, c)

# Print the result
if result == "NO":
    print(result)
else:
    print(result[0])
    print(' '.join(map(str, result[1])))