def max_painted_sections(n, q, painters):
    # Function to calculate painted sections with hired painters
    def painted_length(active_painters):
        painted = [0] * (n + 1)
        for l, r in active_painters:
            for i in range(l, r + 1):
                painted[i] = 1
        return sum(painted)

    max_sections = 0

    # Try excluding each pair of painters
    for i in range(q):
        for j in range(i + 1, q):
            active_painters = [painters[k] for k in range(q) if k != i and k != j]
            max_sections = max(max_sections, painted_length(active_painters))

    return max_sections

# Input reading
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Calculate and print the maximum number of painted sections
print(max_painted_sections(n, q, painters))