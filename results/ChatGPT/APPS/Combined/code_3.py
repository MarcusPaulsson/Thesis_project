def max_painted_sections(n, q, painters):
    # Create a list to track the coverage of each section
    coverage = [0] * (n + 1)

    # Count the coverage for each painter
    for l, r in painters:
        coverage[l] += 1
        if r + 1 <= n:
            coverage[r + 1] -= 1

    # Calculate the actual coverage using prefix sums
    for i in range(1, n + 1):
        coverage[i] += coverage[i - 1]

    # Calculate the total painted sections with all painters
    total_painted = sum(1 for i in range(1, n + 1) if coverage[i] > 0)

    max_painted = total_painted

    # Try excluding each pair of painters
    for i in range(q):
        for j in range(i + 1, q):
            # Create a temporary coverage array
            temp_coverage = coverage[:]
            l1, r1 = painters[i]
            l2, r2 = painters[j]

            # Remove the coverage of the excluded painters
            for k in range(l1, r1 + 1):
                temp_coverage[k] -= 1
            for k in range(l2, r2 + 1):
                temp_coverage[k] -= 1

            # Count the painted sections after excluding the two painters
            painted_after_exclusion = sum(1 for k in range(1, n + 1) if temp_coverage[k] > 0)
            max_painted = max(max_painted, painted_after_exclusion)

    return max_painted

# Read input
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Get the result and print it
result = max_painted_sections(n, q, painters)
print(result)