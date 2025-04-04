def max_painted_sections(n, q, painters):
    # Initialize a list to store the painted sections count
    painted_sections = [0] * (n + 1)

    # Function to calculate painted sections with a given set of painters
    def count_painted(painter_indices):
        painted = [0] * (n + 1)
        for i in painter_indices:
            l, r = painters[i]
            for j in range(l, r + 1):
                painted[j] = 1
        return sum(painted)

    # We will try to exclude each pair of painters to maximize the painted sections
    max_painted = 0
    for i in range(q):
        for j in range(i + 1, q):
            # Generate indices of painters to include
            painter_indices = [k for k in range(q) if k != i and k != j]
            painted_count = count_painted(painter_indices)
            max_painted = max(max_painted, painted_count)

    return max_painted

# Read input
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Calculate and print the result
print(max_painted_sections(n, q, painters))