def max_painted_sections(n, q, painters):
    # Create an array to keep track of the coverage of sections
    coverage = [0] * (n + 1)
    
    # Count the total coverage by all painters
    for l, r in painters:
        for j in range(l, r + 1):
            coverage[j] += 1
    
    # To find the maximum painted sections by omitting 2 painters
    max_sections = 0
    
    for i in range(q):
        for j in range(i + 1, q):
            # Create a temporary coverage array
            temp_coverage = coverage[:]
            # Remove the coverage of the i-th and j-th painters
            l1, r1 = painters[i]
            l2, r2 = painters[j]
            for x in range(l1, r1 + 1):
                temp_coverage[x] -= 1
            for x in range(l2, r2 + 1):
                temp_coverage[x] -= 1
            
            # Count the painted sections after removing these two painters
            painted_sections = sum(1 for k in range(1, n + 1) if temp_coverage[k] > 0)
            max_sections = max(max_sections, painted_sections)
    
    return max_sections

# Input reading
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Output the maximum painted sections
print(max_painted_sections(n, q, painters))