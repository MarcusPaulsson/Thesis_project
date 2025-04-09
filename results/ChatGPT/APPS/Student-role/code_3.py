def max_painted_sections(n, q, painters):
    def painted_length(painters):
        painted = [0] * (n + 1)
        for l, r in painters:
            painted[l] += 1
            if r + 1 <= n:
                painted[r + 1] -= 1
        for i in range(1, n + 1):
            painted[i] += painted[i - 1]
        return sum(1 for x in painted[1:] if x > 0)

    max_sections = 0
    for i in range(q):
        for j in range(i + 1, q):
            selected_painters = [painters[k] for k in range(q) if k != i and k != j]
            max_sections = max(max_sections, painted_length(selected_painters))

    return max_sections

# Input reading
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Output the result
print(max_painted_sections(n, q, painters))