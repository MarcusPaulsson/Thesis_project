def max_painted_sections(n, q, painters):
    # Sort painters by their left boundary
    painters.sort(key=lambda x: x[0])
    
    # Initialize the maximum number of painted sections
    max_painted = 0
    
    # Iterate over all possible pairs of painters to exclude
    for i in range(q):
        for j in range(i + 1, q):
            # Calculate the number of painted sections if painters i and j are excluded
            painted = 0
            for k in range(q):
                if k != i and k != j:
                    # Find the intersection of the remaining painters' sections
                    l = max(painted + 1, painters[k][0])
                    r = min(n, painters[k][1])
                    if l <= r:
                        painted += r - l + 1
            # Update the maximum number of painted sections
            max_painted = max(max_painted, painted)
    
    return max_painted

# Read input
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Print the result
print(max_painted_sections(n, q, painters))