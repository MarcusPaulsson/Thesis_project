def max_painted_sections(n, q, painters):
    def calculate_painted(excluded_indices):
        painted_sections = [0] * (n + 1)
        for index in range(q):
            if index not in excluded_indices:
                l, r = painters[index]
                for i in range(l, r + 1):
                    painted_sections[i] = 1
        return sum(painted_sections)

    max_sections = 0

    # Try removing each pair of painters
    for i in range(q):
        for j in range(i + 1, q):
            painted_count = calculate_painted({i, j})
            max_sections = max(max_sections, painted_count)

    return max_sections

# Read input
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Get the result and print it
result = max_painted_sections(n, q, painters)
print(result)