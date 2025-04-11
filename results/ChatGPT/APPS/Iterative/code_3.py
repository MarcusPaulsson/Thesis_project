def max_painted_sections(n, q, painters):
    # Create a list to store the painted sections count
    painted_count = [0] * (n + 1)

    # Function to calculate the number of painted sections with a specific set of painters
    def count_painted(painter_indices):
        painted = [0] * (n + 1)
        for index in painter_indices:
            l, r = painters[index]
            for j in range(l, r + 1):
                painted[j] = 1
        return sum(painted)

    max_sections = 0

    # Try every combination of q - 2 painters
    from itertools import combinations
    for indices in combinations(range(q), q - 2):
        max_sections = max(max_sections, count_painted(indices))

    return max_sections

# Read input
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Get the result and print it
result = max_painted_sections(n, q, painters)
print(result)