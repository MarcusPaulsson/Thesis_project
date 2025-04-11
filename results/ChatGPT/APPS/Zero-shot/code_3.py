def max_painted_sections(n, q, painters):
    # Function to calculate the number of painted sections
    def painted_count(painters_to_consider):
        painted = [0] * (n + 1)
        for l, r in painters_to_consider:
            for i in range(l, r + 1):
                painted[i] = 1
        return sum(painted)

    max_sections = 0

    # Try removing each pair of painters
    for i in range(q):
        for j in range(i + 1, q):
            # Create a list of painters excluding the i-th and j-th
            remaining_painters = [painters[k] for k in range(q) if k != i and k != j]
            max_sections = max(max_sections, painted_count(remaining_painters))

    return max_sections

# Read input
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Get the result and print it
result = max_painted_sections(n, q, painters)
print(result)