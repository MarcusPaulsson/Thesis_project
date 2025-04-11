def max_painted_sections(n, q, painters):
    # Create a list to store the coverage of each section
    coverage = [0] * (n + 1)

    # Calculate the total coverage with all painters
    for l, r in painters:
        for i in range(l, r + 1):
            coverage[i] += 1

    # Calculate the painted sections with all painters
    total_painted = sum(1 for i in range(1, n + 1) if coverage[i] > 0)

    # To find the maximum painted sections when hiring q - 2 painters
    max_painted = total_painted

    # Check the effect of removing each pair of painters
    for i in range(q):
        for j in range(i + 1, q):
            # Create a temporary coverage array
            temp_coverage = coverage[:]
            l1, r1 = painters[i]
            l2, r2 = painters[j]

            # Remove the coverage of the i-th painter
            for k in range(l1, r1 + 1):
                temp_coverage[k] -= 1
            # Remove the coverage of the j-th painter
            for k in range(l2, r2 + 1):
                temp_coverage[k] -= 1

            # Calculate the painted sections after removing these two painters
            painted_after_removal = sum(1 for k in range(1, n + 1) if temp_coverage[k] > 0)
            max_painted = max(max_painted, painted_after_removal)

    return max_painted

# Read input
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Get the result and print it
result = max_painted_sections(n, q, painters)
print(result)