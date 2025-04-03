def max_painted_sections(n, q, painters):
    # Create an array to keep track of painted sections
    painted = [0] * (n + 1)
    
    # Function to calculate painted sections with given painters
    def count_painted(painters_to_consider):
        temp_painted = [0] * (n + 1)
        for l, r in painters_to_consider:
            for x in range(l, r + 1):
                temp_painted[x] = 1
        return sum(temp_painted)

    max_sections = 0
    
    # Try excluding each pair of painters
    for i in range(q):
        for j in range(i + 1, q):
            # Exclude painters[i] and painters[j]
            selected_painters = [painters[k] for k in range(q) if k != i and k != j]
            painted_sections = count_painted(selected_painters)
            max_sections = max(max_sections, painted_sections)
    
    return max_sections

# Read input
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Get the result and print it
result = max_painted_sections(n, q, painters)
print(result)