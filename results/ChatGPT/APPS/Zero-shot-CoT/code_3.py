def max_painted_sections(n, q, painters):
    # Initialize an array to keep track of the coverage of sections
    coverage = [0] * (n + 1)
    
    # Calculate total coverage for all painters
    for l, r in painters:
        for i in range(l, r + 1):
            coverage[i] += 1

    # Find the maximum painted sections when removing 2 painters
    max_sections = 0
    
    for i in range(q):
        # Create a new coverage array to simulate removing the i-th painter
        temp_coverage = coverage[:]
        l_i, r_i = painters[i]
        
        for j in range(l_i, r_i + 1):
            temp_coverage[j] -= 1
        
        for k in range(i + 1, q):
            # Create another coverage array to simulate removing the k-th painter
            final_coverage = temp_coverage[:]
            l_k, r_k = painters[k]
            
            for j in range(l_k, r_k + 1):
                final_coverage[j] -= 1
            
            # Count the sections that are painted
            painted_count = sum(1 for x in range(1, n + 1) if final_coverage[x] > 0)
            max_sections = max(max_sections, painted_count)
    
    return max_sections

# Read input
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Get the result and print it
result = max_painted_sections(n, q, painters)
print(result)