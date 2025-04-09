def max_painted_sections(n, q, painters):
    # Create a function to calculate painted sections with given painters
    def painted_length(selected_painters):
        painted = [0] * (n + 1)
        for l, r in selected_painters:
            painted[l] += 1
            if r + 1 <= n:
                painted[r + 1] -= 1
        
        # Calculate the prefix sum to get the actual painted sections
        total_painted = 0
        current_paint = 0
        for i in range(1, n + 1):
            current_paint += painted[i]
            if current_paint > 0:
                total_painted += 1
        
        return total_painted

    max_sections = 0

    # Try removing each pair of painters
    for i in range(q):
        for j in range(i + 1, q):
            # Select all painters except the i-th and j-th
            selected_painters = [painters[k] for k in range(q) if k != i and k != j]
            max_sections = max(max_sections, painted_length(selected_painters))

    return max_sections

# Input reading
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Output result
print(max_painted_sections(n, q, painters))