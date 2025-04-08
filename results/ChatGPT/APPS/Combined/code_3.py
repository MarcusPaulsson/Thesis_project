def max_painted_sections(n, q, painters):
    # Create an array to track the painted sections
    painted = [0] * (n + 1)

    # Function to calculate the number of painted sections
    def calculate_painted_count(exclude_indices):
        painted_count = [0] * (n + 1)
        for i in range(q):
            if i not in exclude_indices:
                l, r = painters[i]
                for j in range(l, r + 1):
                    painted_count[j] += 1
        return sum(1 for x in painted_count if x > 0)

    max_count = 0

    # Try excluding each pair of painters
    for i in range(q):
        for j in range(i + 1, q):
            painted_count = calculate_painted_count({i, j})
            max_count = max(max_count, painted_count)

    return max_count

# Read input
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Get the result and print it
result = max_painted_sections(n, q, painters)
print(result)