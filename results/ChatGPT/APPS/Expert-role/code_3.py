def max_painted_sections(n, q, painters):
    def painted_length(excluded_indices):
        painted = [0] * (n + 1)
        for i in range(q):
            if i not in excluded_indices:
                l, r = painters[i]
                for j in range(l, r + 1):
                    painted[j] = 1
        return sum(painted)

    max_sections = 0
    for i in range(q):
        for j in range(i + 1, q):
            excluded_indices = {i, j}
            max_sections = max(max_sections, painted_length(excluded_indices))

    return max_sections

# Input reading
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Get the result and print it
result = max_painted_sections(n, q, painters)
print(result)