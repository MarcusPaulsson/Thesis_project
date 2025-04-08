def find_grandpas_sofa(d, n, m, sofas, counts):
    cnt_l, cnt_r, cnt_t, cnt_b = counts
    positions = []

    # Collect sofa positions and their indices
    for idx, (x1, y1, x2, y2) in enumerate(sofas):
        positions.append((min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2), idx + 1))

    # Check each sofa and count its neighbors
    for x1, y1, x2, y2, index in positions:
        left_count = right_count = top_count = bottom_count = 0
        
        for x3, y3, x4, y4, other_index in positions:
            if index == other_index:
                continue
            
            if x2 < x3:  # Current sofa is to the left of another sofa
                left_count += 1
            elif x1 > x4:  # Current sofa is to the right of another sofa
                right_count += 1
            elif y2 < y3:  # Current sofa is above another sofa
                top_count += 1
            elif y1 > y4:  # Current sofa is below another sofa
                bottom_count += 1
        
        # Check if counts match
        if (left_count == cnt_l and right_count == cnt_r and
                top_count == cnt_t and bottom_count == cnt_b):
            return index

    return -1

# Input reading
d = int(input())
n, m = map(int, input().split())
sofas = [tuple(map(int, input().split())) for _ in range(d)]
counts = tuple(map(int, input().split()))

# Find and print the result
result = find_grandpas_sofa(d, n, m, sofas, counts)
print(result)