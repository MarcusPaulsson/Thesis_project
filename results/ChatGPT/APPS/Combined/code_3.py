def max_painted_sections(n, q, painters):
    # Create a function to calculate the number of painted sections
    def calculate_painted(painter_indices):
        painted = [0] * (n + 1)
        for index in painter_indices:
            l, r = painters[index]
            painted[l:r + 1] = [1] * (r - l + 1)  # Mark painted sections
        return sum(painted)

    max_sections = 0
    
    # Iterate over all pairs of painters to remove
    for i in range(q):
        for j in range(i + 1, q):
            painter_indices = [k for k in range(q) if k != i and k != j]
            max_sections = max(max_sections, calculate_painted(painter_indices))

    return max_sections

# Read input
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Get result and print
result = max_painted_sections(n, q, painters)
print(result)