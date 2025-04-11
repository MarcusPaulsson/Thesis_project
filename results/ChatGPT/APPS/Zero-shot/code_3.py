def max_painted_sections(n, q, painters):
    # Create a list to keep track of painted sections
    painted = [0] * (n + 1)

    # Function to calculate the number of painted sections with a given set of painters
    def calculate_painted(painter_indices):
        temp_painted = [0] * (n + 1)
        for i in painter_indices:
            l, r = painters[i]
            for j in range(l, r + 1):
                temp_painted[j] = 1
        return sum(temp_painted)

    max_sections = 0

    # Try removing each pair of painters
    for i in range(q):
        for j in range(i + 1, q):
            # Get the indices of the remaining painters
            remaining_painters = [k for k in range(q) if k != i and k != j]
            painted_sections = calculate_painted(remaining_painters)
            max_sections = max(max_sections, painted_sections)

    return max_sections

# Input reading
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Output the result
print(max_painted_sections(n, q, painters))