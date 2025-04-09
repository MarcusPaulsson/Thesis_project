def can_reach_river(n, m, d, lengths):
    total_length = sum(lengths)
    
    # Check if the total length of platforms is greater than the width of the river
    if total_length > n:
        return "NO"
    
    # Initialize the river cells array
    river_cells = [0] * n
    current_position = 0
    
    # Place platforms in the river cells
    for idx in range(m):
        platform_length = lengths[idx]
        # Check if we can place the platform
        if current_position + platform_length > n:
            return "NO"
        
        # Fill the river cells with platform index (1-indexed)
        for j in range(platform_length):
            river_cells[current_position + j] = idx + 1  # 1-indexed platform
        current_position += platform_length
        
        # Add a gap to ensure we can jump to the next platform
        if idx < m - 1:  # No need to add gap after the last platform
            current_position += d
    
    return "YES", river_cells

# Read input
n, m, d = map(int, input().split())
lengths = list(map(int, input().split()))

# Get the result
result = can_reach_river(n, m, d, lengths)

# Print the output
if result == "NO":
    print(result)
else:
    print(result[0])
    print(' '.join(map(str, result[1])))