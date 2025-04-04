def can_cross_river(n, m, d, platforms):
    # Total length of platforms
    total_length = sum(platforms)
    
    # If the maximum jump distance is greater than or equal to the width of the river, it's always possible
    if d >= n + 1:
        return True, [0] * n + [1]  # All cells can be platform 1

    # Create an array to represent the river cells
    river = [0] * n
    current_position = 0

    # Try placing platforms in a way that maximizes the distance they cover
    for i in range(m):
        platform_length = platforms[i]
        # Place the platform at the furthest possible position
        river[current_position:current_position + platform_length] = [i + 1] * platform_length
        current_position += platform_length
        
        # Ensure we leave space for the next platform
        if i < m - 1:
            current_position += d  # Leave a gap of d cells for the jump

    # If the last platform does not reach the end, fill the remaining cells
    if current_position < n:
        river[current_position:] = [0] * (n - current_position)

    # Now check if we can actually jump to the end
    last_jump_position = 0
    for pos in range(n):
        if river[pos] != 0:  # There's a platform here
            if pos <= last_jump_position + d:  # Can jump to this position
                last_jump_position = pos + (river[pos] == 0)  # Jump to this platform
            if last_jump_position >= n:  # We can reach the end
                return True, river

    return False, []

# Input reading
n, m, d = map(int, input().split())
platforms = list(map(int, input().split()))

# Check if crossing is possible and get the configuration
is_possible, configuration = can_cross_river(n, m, d, platforms)

# Output the result
if is_possible:
    print("YES")
    print(" ".join(map(str, configuration)))
else:
    print("NO")