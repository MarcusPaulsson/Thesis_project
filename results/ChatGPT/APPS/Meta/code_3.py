def max_painted_sections(n, q, painters):
    # Create a list to store the coverage of each section
    coverage = [0] * (n + 1)

    # Count the coverage for each painter
    for l, r in painters:
        for i in range(l, r + 1):
            coverage[i] += 1

    # Calculate the total painted sections with all painters
    total_painted = sum(1 for i in range(1, n + 1) if coverage[i] > 0)

    # If we hire q - 2 painters, we need to find the two painters that cover the most sections
    max_loss = 0

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
            max_loss = max(max_loss, total_painted - painted_after_removal)

    # The maximum painted sections after hiring q - 2 painters
    return total_painted - max_loss

# Read input
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Get the result and print it
result = max_painted_sections(n, q, painters)
print(result)