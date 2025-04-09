def max_painted_sections(n, q, painters):
    # Create an array to represent the painting sections
    painted = [0] * (n + 1)

    # Function to calculate painted sections with all painters
    def calculate_painted(painters_to_consider):
        painted_count = [0] * (n + 1)
        for l, r in painters_to_consider:
            for section in range(l, r + 1):
                painted_count[section] += 1
        return sum(1 for count in painted_count if count > 0)

    max_sections = 0

    # Try removing each pair of painters
    for i in range(q):
        for j in range(i + 1, q):
            # Create a new list of painters excluding the i-th and j-th painters
            remaining_painters = [painters[k] for k in range(q) if k != i and k != j]
            # Calculate the number of painted sections with the remaining painters
            painted_sections = calculate_painted(remaining_painters)
            max_sections = max(max_sections, painted_sections)

    return max_sections

# Input reading
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Calculate and print the result
result = max_painted_sections(n, q, painters)
print(result)