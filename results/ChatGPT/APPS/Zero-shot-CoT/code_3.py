def max_painted_sections(n, q, painters):
    # Create a list to track the coverage of each section
    coverage = [0] * (n + 1)

    # Count the coverage for each painter
    for l, r in painters:
        for i in range(l, r + 1):
            coverage[i] += 1

    # Calculate the total painted sections with all painters
    total_painted = sum(1 for i in range(1, n + 1) if coverage[i] > 0)

    # If we hire q - 2 painters, we need to find the two painters to exclude
    max_painted = 0

    for i in range(q):
        # Create a temporary coverage array to simulate excluding the i-th painter
        temp_coverage = coverage[:]
        l_i, r_i = painters[i]
        
        # Remove the coverage of the i-th painter
        for j in range(l_i, r_i + 1):
            temp_coverage[j] -= 1

        # Calculate the painted sections after excluding the i-th painter
        painted_after_exclusion = sum(1 for k in range(1, n + 1) if temp_coverage[k] > 0)
        
        # Update the maximum painted sections
        max_painted = max(max_painted, painted_after_exclusion)

    return max_painted

# Input reading
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Get the result and print it
result = max_painted_sections(n, q, painters)
print(result)