def max_painted_sections(n, q, painters):
    def painted_count(excluded):
        painted = [0] * (n + 1)
        for i in range(q):
            if i == excluded:
                continue
            l, r = painters[i]
            for j in range(l, r + 1):
                painted[j] = 1
        return sum(painted)

    max_sections = 0
    for i in range(q):
        max_sections = max(max_sections, painted_count(i))
    
    return max_sections

# Input reading
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Output the result
print(max_painted_sections(n, q, painters))