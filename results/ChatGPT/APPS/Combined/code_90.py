def can_reach_end(n, m, d, platforms):
    # Calculate total length of platforms
    total_length = sum(platforms)

    # Calculate minimum required length to place platforms
    min_required_length = (m - 1) * d + total_length
    if min_required_length > n:
        return "NO", []

    # Initialize the river configuration
    river = [0] * n
    current_position = 0

    for platform_index in range(m):
        # Place the platform at the current position
        for j in range(platforms[platform_index]):
            river[current_position] = platform_index + 1  # 1-based index for platforms
            current_position += 1

        # Move the current position forward by the jump distance (d) if not the last platform
        if platform_index < m - 1:
            current_position += d

    return "YES", river

# Read input
n, m, d = map(int, input().split())
platforms = list(map(int, input().split()))

# Get output
result, river_configuration = can_reach_end(n, m, d, platforms)

# Print result
print(result)
if result == "YES":
    print(" ".join(map(str, river_configuration)))