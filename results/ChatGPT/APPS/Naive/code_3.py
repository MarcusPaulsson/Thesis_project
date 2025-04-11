def max_painted_sections(n, q, painters):
    # Create a list to track the painted sections
    painted = [0] * (n + 1)

    # Function to calculate the number of painted sections
    def calculate_painted(painters_to_consider):
        temp_painted = [0] * (n + 1)
        for l, r in painters_to_consider:
            for i in range(l, r + 1):
                temp_painted[i] = 1
        return sum(temp_painted)

    max_sections = 0

    # Try removing each pair of painters
    for i in range(q):
        for j in range(i + 1, q):
            # Create a list of painters excluding the i-th and j-th
            painters_to_consider = [painters[k] for k in range(q) if k != i and k != j]
            # Calculate the number of painted sections with the remaining painters
            painted_count = calculate_painted(painters_to_consider)
            max_sections = max(max_sections, painted_count)

    return max_sections

# Input reading
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Output the result
print(max_painted_sections(n, q, painters))