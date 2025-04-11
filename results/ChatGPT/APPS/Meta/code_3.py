def max_painted_sections(n, q, painters):
    # Create an array to keep track of painted sections
    painted = [0] * (n + 1)

    # Function to calculate the number of painted sections
    def calculate_painted(painters_to_consider):
        painted_count = [0] * (n + 1)
        for l, r in painters_to_consider:
            for i in range(l, r + 1):
                painted_count[i] = 1
        return sum(painted_count)

    # Try removing each pair of painters and calculate the painted sections
    max_sections = 0
    for i in range(q):
        for j in range(i + 1, q):
            # Create a list of painters excluding the i-th and j-th
            painters_to_consider = [painters[k] for k in range(q) if k != i and k != j]
            max_sections = max(max_sections, calculate_painted(painters_to_consider))

    return max_sections

# Read input
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Get the result and print it
result = max_painted_sections(n, q, painters)
print(result)