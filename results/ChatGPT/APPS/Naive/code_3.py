def max_painted_sections(n, q, painters):
    # Create a list to track the coverage of each section
    coverage = [0] * (n + 1)

    # Function to calculate the number of painted sections
    def calculate_painted_sections(painter_list):
        temp_coverage = [0] * (n + 1)
        for l, r in painter_list:
            for i in range(l, r + 1):
                temp_coverage[i] = 1
        return sum(temp_coverage)

    # Try removing each pair of painters and calculate the painted sections
    max_sections = 0
    for i in range(q):
        for j in range(i + 1, q):
            # Create a list of painters excluding the i-th and j-th
            selected_painters = [painters[k] for k in range(q) if k != i and k != j]
            painted_sections = calculate_painted_sections(selected_painters)
            max_sections = max(max_sections, painted_sections)

    return max_sections

# Input reading
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Output the result
print(max_painted_sections(n, q, painters))