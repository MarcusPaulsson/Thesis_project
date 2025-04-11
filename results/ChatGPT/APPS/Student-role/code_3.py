def max_painted_sections(n, q, painters):
    # Create a list to track the coverage of each section
    coverage = [0] * (n + 1)

    # Count the coverage for each painter
    for l, r in painters:
        for i in range(l, r + 1):
            coverage[i] += 1

    # Calculate the total painted sections with all painters
    total_painted = sum(1 for i in range(1, n + 1) if coverage[i] > 0)

    # If we hire q - 2 painters, we need to find the two painters that cover the most sections
    # and remove their coverage from the total painted sections
    max_painted = total_painted

    for i in range(q):
        # Temporarily remove the coverage of the i-th painter
        l_i, r_i = painters[i]
        for j in range(l_i, r_i + 1):
            coverage[j] -= 1

        # Calculate the new number of painted sections
        painted_after_removal = sum(1 for k in range(1, n + 1) if coverage[k] > 0)
        max_painted = max(max_painted, painted_after_removal)

        # Restore the coverage of the i-th painter
        for j in range(l_i, r_i + 1):
            coverage[j] += 1

    return max_painted

# Read input
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Get the result and print it
result = max_painted_sections(n, q, painters)
print(result)