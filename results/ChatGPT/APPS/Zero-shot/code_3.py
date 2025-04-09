def max_painted_sections(n, q, painters):
    painted_sections = [0] * (n + 1)

    # Calculate the range covered by all painters
    for l, r in painters:
        for i in range(l, r + 1):
            painted_sections[i] += 1

    # For each painter, calculate the coverage without that painter
    max_paint = 0
    for i in range(q):
        # Create a temporary painted sections array
        temp_painted = painted_sections[:]
        l, r = painters[i]

        # Remove the coverage of the current painter
        for j in range(l, r + 1):
            temp_painted[j] -= 1

        # Count the number of painted sections after removing the painter
        current_paint = sum(1 for count in temp_painted[1:] if count > 0)
        max_paint = max(max_paint, current_paint)

    return max_paint

# Input reading
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Output the maximum number of painted sections
print(max_painted_sections(n, q, painters))