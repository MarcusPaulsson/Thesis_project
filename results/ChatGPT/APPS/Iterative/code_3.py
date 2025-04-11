def max_painted_sections(n, q, painters):
    # Create an array to count the coverage of each section
    coverage = [0] * (n + 1)

    # Count the coverage of each section by all painters
    for l, r in painters:
        for i in range(l, r + 1):
            coverage[i] += 1

    # Calculate the total painted sections with all painters
    total_painted = sum(1 for i in range(1, n + 1) if coverage[i] > 0)

    # If we hire q - 2 painters, we need to find the two painters that cover the least sections
    contributions = []
    for l, r in painters:
        contribution = sum(1 for i in range(l, r + 1) if coverage[i] == 1)
        contributions.append(contribution)

    # Sort contributions in ascending order
    contributions.sort()

    # The maximum painted sections we can achieve is total painted minus the contributions of the two least contributing painters
    if len(contributions) >= 2:
        max_painted = total_painted - (contributions[0] + contributions[1])
    else:
        max_painted = total_painted

    return max(max_painted, 0)  # Ensure we don't return negative painted sections

# Input reading
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Output the result
print(max_painted_sections(n, q, painters))