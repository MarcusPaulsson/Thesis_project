def find_grandpas_sofa(d, n, m, sofas, counts):
    cnt_l, cnt_r, cnt_t, cnt_b = counts
    # Create lists to store the sofas positions
    positions = []
    
    for i in range(d):
        x1, y1, x2, y2 = sofas[i]
        positions.append((min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))
    
    # Initialize the counts for each sofa
    left_counts = [0] * d
    right_counts = [0] * d
    top_counts = [0] * d
    bottom_counts = [0] * d
    
    # Calculate counts for each sofa
    for i in range(d):
        x1, y1, x2, y2 = positions[i]
        for j in range(d):
            if i != j:
                x1_j, y1_j, x2_j, y2_j = positions[j]
                
                # Check if j is to the left of i
                if x2_j < x1:  # sofa j is to the left of sofa i
                    left_counts[i] += 1
                # Check if j is to the right of i
                elif x1_j > x2:  # sofa j is to the right of sofa i
                    right_counts[i] += 1
                # Check if j is above i
                elif y2_j < y1:  # sofa j is above sofa i
                    top_counts[i] += 1
                # Check if j is below i
                elif y1_j > y2:  # sofa j is below sofa i
                    bottom_counts[i] += 1
    
    # Find the matching sofa
    for i in range(d):
        if (left_counts[i] == cnt_l and 
            right_counts[i] == cnt_r and 
            top_counts[i] == cnt_t and 
            bottom_counts[i] == cnt_b):
            return i + 1  # Return 1-based index
    
    return -1  # No matching sofa found

# Read input
d = int(input().strip())
n, m = map(int, input().strip().split())
sofas = [tuple(map(int, input().strip().split())) for _ in range(d)]
counts = tuple(map(int, input().strip().split()))

# Get the result
result = find_grandpas_sofa(d, n, m, sofas, counts)

# Print the result
print(result)